from dtos.highlightly.league_dto import LeagueDTO
from models.competition import Competition

def adapt_competition(dto: LeagueDTO) -> Competition:
    return Competition (
        external_id = dto.id,
        name = dto.name,
        logo = dto.logo,
        country_name = dto.country_name,
        country_code = dto.country_code,
        country_logo = dto.country_logo
    )