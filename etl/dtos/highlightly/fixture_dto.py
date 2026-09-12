from dataclasses import dataclass

@dataclass
class FixtureDTO:
    id: int
    date: str
    round: str
    status_description: str
    league_id: int
    season: int
    home_team_id: int
    away_team_id: int
    score_current: str

    @staticmethod
    def from_api(data: dict) -> "FixtureDTO":
        return FixtureDTO(
            id = data["id"],
            date = data["date"],
            round = data.get("round"),
            status_description = data["state"]["description"],
            league_id = data["league"]["id"],
            season = data["league"]["season"],
            home_team_id = data["homeTeam"]["id"],
            away_team_id = data["awayTeam"]["id"],
            score_current = data["state"]["score"].get("current")
        )