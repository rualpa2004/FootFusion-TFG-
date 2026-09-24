from dataclasses import dataclass

@dataclass
class FootballDataPlayerDTO:
    id: int
    name: str
    position: str
    date_of_birth: str
    nationality: str

    @staticmethod
    def from_api(data: dict) -> "FootballDataPlayerDTO":
        return FootballDataPlayerDTO(
            id = data["id"],
            name = data["name"],
            position = data.get("position"),
            date_of_birth = data.get("dateOfBirth"),
            nationality = data.get("nationality")
        )