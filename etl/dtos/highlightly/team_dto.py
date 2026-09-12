from dataclasses import dataclass

@dataclass
class TeamDTO:
    id: int
    name: str
    logo: str
    type: str

    @staticmethod
    def from_api(data: dict) -> "TeamDTO":
        return TeamDTO(
            id = data["id"],
            name = data["name"],
            logo = data.get("logo"),
            type = data.get("type")
        )