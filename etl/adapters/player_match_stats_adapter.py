import unicodedata
import re
from difflib import SequenceMatcher
from dtos.highlightly.fixture_player_stats_dto import FixturePlayerStatsDTO
from models.player_match_stats import PlayerMatchStats
from repositories.player_repository import find_player_by_highlightly_id, find_players_by_team, set_player_highlightly_id

def _normalize(name):       # To normalize the name of the players
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    name = re.sub(r"[^a-zA-Z\s-]", "", name)
    return re.sub(r"\s+", " ", name.lower().strip())

def _extract_surname(normalized_name):      # To extract the surname of the players
    tokens = normalized_name.split(" ")
    if len(tokens) > 1 and len(tokens[0]) <= 2:
        tokens = tokens[1:]
    return " ".join(tokens)

def _resolve_player_id(highlightly_id, name, team_id):      # Function to match the player ids
    player = find_player_by_highlightly_id(highlightly_id)
    if player:
        return player["external_id"]

    if team_id is None:
        print(f" Aviso: jugador no encontrado -> {name} (highlightly_id = {highlightly_id}, equipo no resuelto)")
        return None

    candidates = find_players_by_team(team_id)
    normalized_target = _normalize(name)
    surname_target = _extract_surname(normalized_target)

    for candidate in candidates:
        normalized_candidate = _normalize(candidate["name"])
        if normalized_candidate == normalized_target or surname_target in normalized_candidate:
            set_player_highlightly_id(candidate["external_id"], highlightly_id)
            return candidate["external_id"]

    # This is to match players as a ultimate resource
    best_candidate, best_score = None, 0
    for candidate in candidates:
        score = SequenceMatcher(None, normalized_target, _normalize(candidate["name"])).ratio()
        if score > best_score:
            best_score, best_candidate = score, candidate

    if best_candidate and best_score >= 0.6:
        set_player_highlightly_id(best_candidate["external_id"], highlightly_id)
        return best_candidate["external_id"]
    
    print(f" Aviso: Jugador no encontrado -> {name} (highlightly_id = {highlightly_id}, mejor coincidencia: {best_score:.2f})")
    return None

def adapt_player_match_stats(dto: FixturePlayerStatsDTO, match_id: int, team_id: int) -> PlayerMatchStats:
    return PlayerMatchStats(
        player_id = _resolve_player_id(dto.player_id, dto.player_name, team_id),
        player_name = dto.player_name,
        match_id = match_id,
        minutes_played = dto.minutes_played,
        is_substitute = dto.is_substitute,
        goals = dto.goals,
        assists = dto.assists,
        yellow_cards = dto.yellow_cards,
        red_cards = dto.red_cards
    )