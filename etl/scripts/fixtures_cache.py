import json
import os

CACHE_DIR = "cache"

def load_fixtures_from_cache(league_id, season):
    path = f"{CACHE_DIR}/competitions/fixtures_{league_id}_{season}.json"
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"No hay caché para league_id = {league_id}. Ejecuta primero cache_fixtures.py"
        )
    with open(path, "r", encoding = "utf-8") as f:
        return json.load(f)

def load_box_score_from_cache(competition_name, fixture_id):
    path = f"{CACHE_DIR}/{competition_name}/box_score_{fixture_id}.json"
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding = "utf-8") as f:
        return json.load(f)


def save_box_score_to_cache(competition_name, fixture_id, box_score):
    os.makedirs(f"{CACHE_DIR}/{competition_name}", exist_ok = True)
    path = f"{CACHE_DIR}/{competition_name}/box_score_{fixture_id}.json"
    with open(path, "w", encoding = "utf-8") as f:
        json.dump(box_score, f, ensure_ascii = False, indent = 2)