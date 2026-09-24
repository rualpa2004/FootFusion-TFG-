import json
import os
import time
from clients.highlightly_client import HighlightlyClient
from config.competitions import COMPETITIONS

CACHE_DIR = "cache"

client = HighlightlyClient()

def fetch_all_fixtures(league_id, season):
    all_fixtures = []
    offset = 0
    limit = 100
    while True:
        response = client.get_fixtures(league_id, season, limit = limit, offset = offset)
        fixtures = response.get("data", []) if isinstance(response, dict) else response
        if not fixtures:
            break
        all_fixtures.extend(fixtures)
        if len(fixtures) < limit:
            break
        offset += limit
        time.sleep(4)
    return all_fixtures

def save_to_cache(league_id, season, fixtures):
    os.makedirs(f"{CACHE_DIR}/Competitions", exist_ok=True)
    path = f"{CACHE_DIR}/Competitions/fixtures_{league_id}_{season}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fixtures, f, ensure_ascii=False, indent=2)
    return path

def run(season):
    for competition in COMPETITIONS:
        print(f"Descargando fixtures: {competition['name']}")
        fixtures = fetch_all_fixtures(competition["highlightly_id"], season)
        path = save_to_cache(competition["highlightly_id"], season, fixtures)
        print(f" Guardado en {path} ({len(fixtures)} partidos)")

if __name__ == "__main__":
    run(season = 2025)