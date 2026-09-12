from dataclasses import dataclass

@dataclass
class FixturePlayerStatsDTO:
    player_id: int
    player_name: str
    minutes_played: int
    is_substitute: bool
    goals: int
    assists: int
    yellow_cards: int
    red_cards: int

    @staticmethod
    def from_api(player_data: dict) -> "FixturePlayerStatsDTO":
        stats = player_data["statistics"][0] if player_data.get("statistics") else {}
        return FixturePlayerStatsDTO(
            player_id = player_data["id"],
            player_name = player_data["name"],
            minutes_played = player_data["minutesPlayed"],
            is_substitute = player_data.get("isSubstitute", False),
            goals = stats.get("goalsScored", 0),
            assists = stats.get("assists", 0),
            yellow_cards = stats.get("cardsYellow", 0),
            red_cards = stats.get("cardsRed", 0)
        )