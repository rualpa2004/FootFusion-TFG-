from dataclasses import dataclass

@dataclass
class FootballDataTeamDTO:
    id: int
    name: str
    logo: str
    coach_name: str
    coach_nationality: str

    @staticmethod
    def from_api(data: dict) -> "FootballDataTeamDTO":
        coach = data.get("coach") or {}
        return FootballDataTeamDTO(
            id = data["id"],
            name = data["name"],
            logo = data.get("crest"),
            coach_name = coach.get("name"),
            coach_nationality = coach.get("nationality")
        )