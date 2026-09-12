from dataclasses import dataclass

@dataclass
class LeagueDTO:
    id: int
    name: str
    logo: str
    country_name: str
    country_code: str
    country_logo: str

    @staticmethod
    def from_api(data: dict) -> "LeagueDTO":
        return LeagueDTO(
            id = data["id"],
            name = data["name"],
            logo = data["logo"],
            country_name = data["country"]["name"],
            country_code = data["country"]["code"],
            country_logo = data["country"]["logo"]
        )