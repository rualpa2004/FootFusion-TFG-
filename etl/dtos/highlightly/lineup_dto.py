from dataclasses import dataclass, field

@dataclass
class LineupDTO:
    team_id: int
    formation: str
    starting_players: list = field(default_factory = list)
    substitute_player_ids: list = field(default_factory = list)

    @staticmethod
    def from_api(team_data: dict) -> "LineupDTO":
        starting = [
            player
            for row in team_data.get("initialLineup", [])
            for player in row
        ]
        return LineupDTO(
            team_id = team_data["id"],
            formation = team_data.get("formation"),
            starting_players = [player["name"] for player in starting],
            substitute_player_ids = [substitute["id"] for substitute in team_data.get("substitutes", [])]
        )