from dataclasses import dataclass

@dataclass
class PlayerMatchStats:
    player_id: int
    player_name: str
    match_id: int
    minutes_played: int
    is_substitute: int
    goals: int
    assists: int
    yellow_cards: int
    red_cards: int