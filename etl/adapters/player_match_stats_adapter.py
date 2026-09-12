from dtos.highlightly.fixture_player_stats_dto import FixturePlayerStatsDTO
from models.player_match_stats import PlayerMatchStats

def adapt_player_match_stats(dto: FixturePlayerStatsDTO, match_id: int) -> PlayerMatchStats:
    return PlayerMatchStats(
        player_id = dto.player_id,
        player_name = dto.player_name,
        match_id = match_id,
        minutes_played = dto.minutes_played,
        is_substitute = dto.is_substitute,
        goals = dto.goals,
        assists = dto.assists,
        yellow_cards = dto.yellow_cards,
        red_cards = dto.red_cards
    )