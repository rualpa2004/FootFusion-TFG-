from dataclasses import dataclass

@dataclass
class FootballDataTeamDTO:
    id: int
    name: str
    logo: str

    @staticmethod
    def from_api(data: dict) -> "FootballDataTeamDTO":
        return FootballDataTeamDTO(
            id = data["id"],
            name = data["name"],
            logo = data.get("crest")
        )