import time
from clients.highlightly_client import HighlightlyClient
from adapters.match_adapter import adapt_match
from adapters.player_match_stats_adapter import adapt_player_match_stats
from dtos.highlightly.fixture_dto import FixtureDTO
from dtos.highlightly.fixture_player_stats_dto import FixturePlayerStatsDTO
from repositories.player_match_stats_repository import save_player_match_stats
from repositories.match_repository import save_match
from repositories.team_repository import find_team_by_highlightly_id
from config.competitions import COMPETITIONS
from collections import defaultdict
from scripts.fixtures_cache import load_fixtures_from_cache, save_box_score_to_cache, load_box_score_from_cache

FINISHED_STATUSES = ["Finished", "Finished AET", "Finished AP", "Finished After Extra Time", "Finished After Penalties"]

client = HighlightlyClient()

def order_rounds(fixtures):     #Function to return rounds grouped and ordered
    grouped = defaultdict(list)
    for fixture_data in fixtures:
        grouped[fixture_data.get("round")].append(fixture_data)

    ordered_round_names = sorted(
        grouped, key=lambda round_name: min(f["date"] for f in grouped[round_name])
    )
    return grouped, ordered_round_names

def process_fixture(competition_name, fixture_data):
    dto = FixtureDTO.from_api(fixture_data)
    match = adapt_match(dto)
    save_match(match)
    if dto.status_description in FINISHED_STATUSES:
        sync_player_stats(competition_name, dto.id, match.external_id)
    time.sleep(8)

def sync_player_stats(competition_name, highlightly_feature_id, match_id):
    box_score = load_box_score_from_cache(competition_name, highlightly_feature_id)
    if box_score is None:
        box_score = client.get_fixture_players(highlightly_feature_id)
        save_box_score_to_cache(competition_name, highlightly_feature_id, box_score)

    for team_entry in box_score:
        team = find_team_by_highlightly_id(team_entry["team"]["id"])
        team_id = team["external_id"] if team else None
        for player_data in team_entry.get("players", []):
            stats_dto = FixturePlayerStatsDTO.from_api(player_data)
            stats = adapt_player_match_stats(stats_dto, match_id, team_id)
            save_player_match_stats(stats)

def run_single_round(competition_name, season, round_name):
    competition = next(c for c in COMPETITIONS if c["name"] == competition_name)
    fixtures = load_fixtures_from_cache(competition["highlightly_id"], season)
    fixtures_by_round, _ = order_rounds(fixtures)

    round_fixtures = fixtures_by_round.get(round_name, [])
    for fixture_data in round_fixtures:
        process_fixture(competition_name, fixture_data)
    print(f"{round_name}: {len(round_fixtures)} partidos")

if __name__ == "__main__":
    run_single_round("Champions League", 2025, "League Stage - 1")