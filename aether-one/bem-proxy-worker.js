/**
 * aci-bem-proxy — Cloudflare Worker
 * BEM data proxy for FinBIF and future CORINE/EEA access
 * 
 * Routes:
 *   /finbif/observations?taxon=MX.47169&bbox=26.5,62.55,27.25,63.3&years=2020-2026
 *   /finbif/species?bbox=...&years=...
 *   /finbif/taxa?id=MX.47169
 *   /status
 *
 * Handles CORS so BEM tools can call from browser/WEM page.
 * 
 * Deploy: wrangler publish
 * Worker name: aci-bem-proxy
 */

const FINBIF_BASE = "https://api.laji.fi";
const FINBIF_TOKEN = "196add350dc78ab9b05d519d274dd5ea861747592cfabb43a22828de262d9fac";

// Rautalammin reitti default bbox
const DEFAULT_BBOX = "26.50,62.55,27.25,63.30";

// BEM indicator species
const INDICATOR_SPECIES = [
  "MX.47169",  // Pteromys volans (liito-orava)
  "MX.37622",  // Ficedula hypoleuca (kirjosieppo)
  "MX.37620",  // Ficedula parva (pikkusieppo)
  "MX.26969",  // Gavia arctica (kuikka)
  "MX.26966",  // Mergus merganser (isokoskelo)
];

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Content-Type": "application/json"
};

function jsonResp(data, status = 200) {
  return new Response(JSON.stringify(data), { status, headers: CORS });
}

function errorResp(msg, status = 500) {
  return jsonResp({ error: msg, status }, status);
}

// Parse bbox string "lng_min,lat_min,lng_max,lat_max"
function parseBbox(bboxStr) {
  const [lng_min, lat_min, lng_max, lat_max] = bboxStr.split(",").map(Number);
  return { lng_min, lat_min, lng_max, lat_max };
}

// Convert bbox to FinBIF coordinate format: "lat_min:lat_max:lng_min:lng_max:WGS84"
function toFinBifCoords(bbox) {
  const b = parseBbox(bbox);
  return `${b.lat_min}:${b.lat_max}:${b.lng_min}:${b.lng_max}:WGS84`;
}

// Parse year range "2020-2026" or single "2026"
function parseYears(yearsStr) {
  if (!yearsStr) return "2020/2026";
  if (yearsStr.includes("-")) {
    return yearsStr.replace("-", "/");
  }
  return yearsStr;
}

async function fetchFinBif(path, params = {}) {
  const url = new URL(`${FINBIF_BASE}${path}`);
  for (const [k, v] of Object.entries(params)) {
    url.searchParams.set(k, v);
  }
  
  const resp = await fetch(url.toString(), {
    headers: {
      "Authorization": `Bearer ${FINBIF_TOKEN}`,
      "Accept": "application/json"
    }
  });
  
  if (!resp.ok) {
    throw new Error(`FinBIF ${resp.status}: ${await resp.text()}`);
  }
  return resp.json();
}

// GET /finbif/observations — single species observation count
async function handleObservations(url) {
  const taxon = url.searchParams.get("taxon") || "MX.47169";
  const bbox = url.searchParams.get("bbox") || DEFAULT_BBOX;
  const years = parseYears(url.searchParams.get("years"));
  
  const data = await fetchFinBif("/warehouse/query/unit/list", {
    taxonId: taxon,
    coordinates: toFinBifCoords(bbox),
    time: years,
    pageSize: 1,
    cache: "true"
  });
  
  return jsonResp({
    taxon,
    bbox,
    years,
    total: data.total || 0,
    source: "FinBIF warehouse"
  });
}

// GET /finbif/species — all indicator species counts
async function handleSpecies(url) {
  const bbox = url.searchParams.get("bbox") || DEFAULT_BBOX;
  const ref_years = parseYears(url.searchParams.get("ref_years") || "2000-2010");
  const cur_years = parseYears(url.searchParams.get("cur_years") || "2020-2026");
  
  const coords = toFinBifCoords(bbox);
  const results = {};
  
  for (const taxon of INDICATOR_SPECIES) {
    try {
      const [ref, cur] = await Promise.all([
        fetchFinBif("/warehouse/query/unit/list", {
          taxonId: taxon, coordinates: coords, time: ref_years,
          pageSize: 1, cache: "true"
        }),
        fetchFinBif("/warehouse/query/unit/list", {
          taxonId: taxon, coordinates: coords, time: cur_years,
          pageSize: 1, cache: "true"
        })
      ]);
      
      results[taxon] = {
        reference: ref.total || 0,
        current: cur.total || 0,
        trend: (ref.total > 0 && cur.total < ref.total * 0.8) ? "declining" :
               (ref.total > 0 && cur.total > ref.total * 1.2) ? "increasing" : "stable"
      };
    } catch (e) {
      results[taxon] = { error: e.message };
    }
  }
  
  return jsonResp({
    bbox,
    ref_years,
    cur_years,
    species: results,
    source: "FinBIF warehouse"
  });
}

// GET /status
function handleStatus() {
  return jsonResp({
    proxy: "aci-bem-proxy",
    version: "0.1",
    routes: [
      "/finbif/observations?taxon=MX.47169&bbox=26.5,62.55,27.25,63.3&years=2020-2026",
      "/finbif/species?bbox=...&ref_years=2000-2010&cur_years=2020-2026",
      "/status"
    ],
    indicator_species: INDICATOR_SPECIES,
    default_bbox: DEFAULT_BBOX,
    instrument: "BEM — Biodiversity Endurance Monitor",
    reference: "https://aethercontinuity.org/supplements/tn-015-biodiversity-endurance-monitor.html"
  });
}

export default {
  async fetch(request) {
    const url = new URL(request.url);
    
    // CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: CORS });
    }
    
    if (request.method !== "GET") {
      return errorResp("Method not allowed", 405);
    }
    
    const path = url.pathname.replace(/\/$/, "");
    
    try {
      if (path === "/status" || path === "") {
        return handleStatus();
      } else if (path === "/finbif/observations") {
        return await handleObservations(url);
      } else if (path === "/finbif/species") {
        return await handleSpecies(url);
      } else {
        return errorResp(`Unknown route: ${path}`, 404);
      }
    } catch (e) {
      return errorResp(e.message);
    }
  }
};
