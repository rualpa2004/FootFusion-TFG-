from dtos.highlightly.team_dto import TeamDTO
from models.team import Team

def adapt_team(dto: TeamDTO, competition_id: int) -> Team:
    return Team(
        external_id = dto.id,
        name = dto.name,
        logo = dto.logo,
        type = dto.type,
        competition_id = competition_id
    )