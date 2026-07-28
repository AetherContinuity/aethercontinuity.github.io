// ============================================================
// Karttulanlahti (kalanviljelyallas + vastaanottava lahti) — MNDWI + NDCI
// kesakauden aikasarja
// Google Earth Engine (GEE) JavaScript, code.earthengine.google.com
//
// PIENENNETTY BBOX 2026-07-28: alkuperainen Iisvesi-koko bbox
// (26.167,62.567,27.067,63.467, ~45km x 100km) osoittautui liian
// raskaaksi reduceRegion-laskennalle GEE:n Code Editorissa (pallo
// pyori pitkaan). Kayttajan oma ehdotus: 4x4 km riittaa, keskitettyna
// Karttulanlahden/kalanviljelyaltaan koordinaattiin (62.87688N, 26.98725E,
// muunnettu asteesta 62 52'36.77"N 26 59'14.09"E).
// ============================================================

var bbox = ee.Geometry.Rectangle([26.94773, 62.85886, 27.02677, 62.89490]);

// Sentinel-2 Surface Reflectance Harmonized - GEE:n oma, valmiiksi
// ilmakehakorjattu kokoelma (vastaa Sentinel-2 L2A:ta)
var s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(bbox);

// Pilvimaskaus SCL-kaistalla (sama periaate kuin oma evalscriptimme):
// poistetaan pilvet (SCL 3=varjo, 8/9=pilvi, 10=ohut cirrus)
function maskS2clouds(image) {
  var scl = image.select('SCL');
  var cloudMask = scl.neq(3).and(scl.neq(8)).and(scl.neq(9)).and(scl.neq(10));
  return image.updateMask(cloudMask);
}

// MNDWI = (B3-B11)/(B3+B11) - Xu 2006, sama kaava kuin omassa
// MNDWI_EVALSCRIPT:ssa, EI maskattu pelkkaan veteen (koko bbox:in yli,
// koska tarkoitus on erottaa vesi/maa)
function addMNDWI(image) {
  var mndwi = image.normalizedDifference(['B3', 'B11']).rename('MNDWI');
  return image.addBands(mndwi);
}

// NDCI = (B5-B4)/(B5+B4) - Mishra & Mishra 2012, sama kaava kuin
// omassa NDCI_EVALSCRIPT:ssa, MASKATTU vain vesipikseleihin (SCL==6)
function addNDCI(image) {
  var ndci = image.normalizedDifference(['B5', 'B4']).rename('NDCI');
  var waterMask = image.select('SCL').eq(6);
  return image.addBands(ndci.updateMask(waterMask));
}

// Kesakausi (touko-syyskuu) jokaiselle vuodelle 2018-2025
// (2018 alkaen, koska tama oli vahvistettu turvalliseksi rajaksi
// aiemmassa tyossa - L2A ei systemaattista Euroopassa ennen 2017-05)
var years = ee.List.sequence(2018, 2025);

var yearlyStats = years.map(function(y) {
  y = ee.Number(y);
  var start = ee.Date.fromYMD(y, 5, 1);
  var end = ee.Date.fromYMD(y, 9, 30);

  var yearCollection = s2.filterDate(start, end)
    .map(maskS2clouds)
    .map(addMNDWI)
    .map(addNDCI);

  var count = yearCollection.size();

  var mndwiMean = yearCollection.select('MNDWI').mean()
    .reduceRegion({reducer: ee.Reducer.mean(), geometry: bbox, scale: 20, maxPixels: 1e9, bestEffort: true})
    .get('MNDWI');

  var ndciMean = yearCollection.select('NDCI').mean()
    .reduceRegion({reducer: ee.Reducer.mean(), geometry: bbox, scale: 20, maxPixels: 1e9, bestEffort: true})
    .get('NDCI');

  return ee.Feature(null, {
    'year': y,
    'scene_count': count,
    'MNDWI_mean': mndwiMean,
    'NDCI_mean': ndciMean
  });
});

var resultsFC = ee.FeatureCollection(yearlyStats);

// Tulostaa taulukon Console-valilehdelle (oikea paneeli GEE:ssa)
print('Iisvesi kesakauden MNDWI/NDCI 2018-2025', resultsFC);

// Kartta silmamaaraiseen tarkistukseen etta bbox osuu oikein
Map.centerObject(bbox, 14);
Map.addLayer(bbox, {color: 'red'}, 'Karttulanlahti bbox (4x4km)');

// Yksittainen tuore MNDWI-kuva visuaaliseksi tarkistukseksi
var recent = s2.filterDate('2025-07-01', '2025-09-30')
  .map(maskS2clouds).map(addMNDWI).median();
Map.addLayer(recent.select('MNDWI'), {min: -0.5, max: 0.8, palette: ['8c6e46','789c50','b4d2a0','8cbedc','3c8cc8','1450a0']}, 'MNDWI 2025 kesa');
