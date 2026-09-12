from dataclasses import dataclass

@dataclass
class Player:
    external_id: int
    name: str
    full_name: str
    photo: str
    birth_date: str
    birth_place: str
    nationality: str
    foot: str
    height: str
    position: str
    team_id: int