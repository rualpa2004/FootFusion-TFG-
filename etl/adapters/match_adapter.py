from dtos.highlightly.fixture_dto import FixtureDTO
from models.match import Match

def adapt_match(dto: FixtureDTO) -> Match:
    return Match(
        external_id = dto.id,
        date = dto.date,
        round = dto.round,
        status_description = dto.status_description,
        competition_id = dto.league_id,
        season = dto.season,
        home_team_id = dto.home_team_id,
        away_team_id = dto.away_team_id,
        score_current = dto.score_current
    )