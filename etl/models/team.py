from dataclasses import dataclass

@dataclass
class Team:
    external_id: int
    name: str
    logo: str
    type: str
    competition_id: int
    highlightly_id: int = None
    coach_name: str = None
    coach_nationality: str = None