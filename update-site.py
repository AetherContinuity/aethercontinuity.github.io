#!/usr/bin/env python3
"""
ACI Site Maintenance Script
- Regenerates sitemap.xml from all HTML files in the repo
- Checks each folder index for missing entries and prints a report
"""

import os
import re
from datetime import date
from pathlib import Path

BASE_URL = "https://aethercontinuity.org"
TODAY = date.today().isoformat()

# Priority rules by folder and file pattern
PRIORITY_MAP = {
    "root": 1.0,
    "research.html": 0.9,
    "about.html": 0.7,
    "papers": 0.9,
    "supplements": 0.85,
    "tools": 0.75,
}

# Files to exclude from sitemap
EXCLUDE = {
    "index.html",       # folder indexes are listed as folder URLs
    "404.html",
    "README.md",
}

# Internal-only files — never in sitemap
INTERNAL_PATTERNS = [
    r"wp-tbd",
    r"internal",
    r"wireframe",       # design prototypes optional — remove if you want them listed
]


def get_priority(folder: str, filename: str) -> str:
    if filename in PRIORITY_MAP:
        return str(PRIORITY_MAP[filename])
    if folder in PRIORITY_MAP:
        return str(PRIORITY_MAP[folder])
    return "0.7"


def is_internal(path: str) -> bool:
    for pattern in INTERNAL_PATTERNS:
        if re.search(pattern, path, re.IGNORECASE):
            return True
    return False


def get_title(filepath: Path) -> str:
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
        if m:
            return m.group(1).strip()
    except Exception:
        pass
    return filepath.stem


def get_lastmod(filepath: Path) -> str:
    """Use git log date if available, otherwise today."""
    try:
        import subprocess
        result = subprocess.run(
            ["git", "log", "-1", "--format=%as", str(filepath)],
            capture_output=True, text=True
        )
        date_str = result.stdout.strip()
        if date_str:
            return date_str
    except Exception:
        pass
    return TODAY


def collect_html_files(root: Path) -> list[dict]:
    entries = []

    # Root HTML files
    for f in sorted(root.glob("*.html")):
        if f.name in EXCLUDE or is_internal(f.name):
            continue
        priority = get_priority("root", f.name)
        entries.append({
            "url": f"/{f.name}",
            "lastmod": get_lastmod(f),
            "priority": priority,
            "title": get_title(f),
            "folder": "root",
            "filename": f.name,
        })

    # Folder indexes (papers/, supplements/, tools/)
    for folder in ["papers", "supplements", "tools"]:
        folder_path = root / folder
        if not folder_path.exists():
            continue
        # Add folder index URL
        entries.append({
            "url": f"/{folder}/",
            "lastmod": TODAY,
            "priority": "0.8",
            "title": f"{folder.capitalize()} index",
            "folder": folder,
            "filename": "index",
        })
        # Add individual files
        for f in sorted(folder_path.glob("*.html")):
            if f.name in EXCLUDE or is_internal(f.name):
                continue
            entries.append({
                "url": f"/{folder}/{f.name}",
                "lastmod": get_lastmod(f),
                "priority": get_priority(folder, f.name),
                "title": get_title(f),
                "folder": folder,
                "filename": f.name,
            })

    return entries


def generate_sitemap(entries: list[dict], output: Path):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    lines.append("")

    current_folder = None
    for e in entries:
        if e["folder"] != current_folder:
            current_folder = e["folder"]
            label = {
                "root": "Core pages",
                "papers": "Papers",
                "supplements": "Supplements",
                "tools": "Tools",
            }.get(current_folder, current_folder)
            lines.append(f"  <!-- {label} -->")

        lines.append("  <url>")
        lines.append(f"    <loc>{BASE_URL}{e['url']}</loc>")
        lines.append(f"    <lastmod>{e['lastmod']}</lastmod>")
        lines.append(f"    <changefreq>monthly</changefreq>")
        lines.append(f"    <priority>{e['priority']}</priority>")
        lines.append("  </url>")

    lines.append("")
    lines.append("</urlset>")

    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ sitemap.xml written — {len(entries)} URLs")


def check_index_completeness(root: Path, entries: list[dict]):
    """
    For each folder, check which HTML files are not referenced
    in the folder's index.html. Print a warning report.
    """
    print("\n── Index completeness check ──")
    any_missing = False

    for folder in ["papers", "supplements", "tools"]:
        folder_path = root / folder
        index_path = folder_path / "index.html"
        if not folder_path.exists() or not index_path.exists():
            continue

        index_content = index_path.read_text(encoding="utf-8", errors="ignore")
        folder_files = [
            e["filename"] for e in entries
            if e["folder"] == folder and e["filename"] != "index"
        ]

        missing = []
        for filename in folder_files:
            if filename not in index_content:
                missing.append(filename)

        if missing:
            any_missing = True
            print(f"\n⚠  {folder}/index.html — missing entries:")
            for m in missing:
                print(f"   - {m}")
        else:
            print(f"✓  {folder}/index.html — all files referenced")

    if not any_missing:
        print("\nAll indexes are complete.")


if __name__ == "__main__":
    root = Path(__file__).parent.parent  # repo root
    entries = collect_html_files(root)
    generate_sitemap(entries, root / "sitemap.xml")
    check_index_completeness(root, entries)
