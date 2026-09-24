from dataclasses import dataclass

@dataclass
class PlayerDTO:
    id: int
    name: str
    full_name: int
    photo: str
    birth_date: str
    birth_place: str
    nationality: str
    foot: str
    height: str
    position: str

    @staticmethod
    def from_api(data: dict) -> "PlayerDTO":
        profile = data.get("profile", {})
        position = profile.get("position", {})
        return PlayerDTO(
            id = data["id"],
            name = data["name"],
            full_name = data.get("fullName"),
            photo = data.get("logo"),
            birth_date = profile.get("birthDate"),
            birth_place = profile.get("birthPlace"),
            nationality = profile.get("citizenship"),
            foot = profile.get("foot"),
            height = profile.get("height"),
            position = position.get("main")
        )