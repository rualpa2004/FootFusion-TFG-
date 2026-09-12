from dtos.highlightly.player_dto import PlayerDTO
from models.player import Player

def adapt_player(dto: PlayerDTO, team_id: int) -> Player:
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