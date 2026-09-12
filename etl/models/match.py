from dataclasses import dataclass

@dataclass
class Match:
    external_id: int
    date: str
    round: str
    status_description: str
    competition_id: int
    season: int
    home_team_id: int
    away_team_id: int
    score_current: str