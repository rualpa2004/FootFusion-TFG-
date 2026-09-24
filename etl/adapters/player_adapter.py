from dtos.highlightly.player_dto import PlayerDTO
from dtos.footballdata.player_dto import FootballDataPlayerDTO
from models.player import Player

def adapt_player_from_highlightly(dto: PlayerDTO, team_id: int) -> Player:
    return Player(
        external_id = dto.id,
        name = dto.name,
        full_name = dto.full_name,
        photo = dto.photo,
        birth_date = dto.birth_date,
        birth_place = dto.birth_place,
        nationality = dto.nationality,
        foot = dto.foot,
        height = dto.height,
        position = dto.position,
        team_id = team_id
    )

def adapt_player_form_footballdata(dto: FootballDataPlayerDTO, team_id: int) -> Player:
    return Player(
        external_id = dto.id,
        name = dto.name,
        full_name = dto.name,
        photo = None,
        birth_date = dto.date_of_birth,
        birth_place = None,
        nationality = dto.nationality,
        foot = None,
        height = None,
        position = dto.position,
        team_id = team_id
    )