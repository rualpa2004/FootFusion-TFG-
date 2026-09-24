import unicodedata
import re
from dtos.highlightly.fixture_dto import FixtureDTO
from models.match import Match
from repositories.team_repository import find_team_by_highlightly_id, find_all_teams, set_team_highlightly_id

TEAM_ALIASES = {        # Needed to correct language issues
    "rb salzburg": "red bull salzburg",
    "sporting cp": "sporting clube de portugal",
    "bayern munich": "bayern munchen",
    "kairat almaty": "fk kairat",
    "olympiakos piraeus": "pae olympiakos sfp"
}

def _normalize(name):
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    name = name.lower()
    name = re.sub(r"\b(cf|fc|ac|bc|sc|cd|ud|club)\b", "", name)
    name = re.sub(r"[^a-z0-9\s]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name

def _resolve_team_id(highlightly_id, name):
    team = find_team_by_highlightly_id(highlightly_id)
    if team:
        return team["external_id"]

    normalized_target = _normalize(name)
    normalized_target = TEAM_ALIASES.get(normalized_target, normalized_target)
    target_tokens = set(normalized_target.split())

    candidates = find_all_teams()

    for candidate in candidates:
        normalized_candidate = _normalize(candidate["name"])
        candidate_tokens = set(normalized_candidate.split())
        if (target_tokens and (target_tokens <= candidate_tokens or candidate_tokens <= target_tokens)) or (normalized_target in normalized_candidate or normalized_candidate in normalized_target):
            set_team_highlightly_id(candidate["external_id"], highlightly_id)
            return candidate["external_id"]
    
    print(f" Aviso: equipo no encontrado -> {name} (highlightly_id = {highlightly_id})")
    return None

def adapt_match(dto: FixtureDTO) -> Match:
    return Match(
        external_id = dto.id,
        date = dto.date,
        round = dto.round,
        status_description = dto.status_description,
        competition_id = dto.league_id,
        season = dto.season,
        home_team_id = _resolve_team_id(dto.home_team_id, dto.home_team_name),
        away_team_id = _resolve_team_id(dto.away_team_id, dto.away_team_name),
        score_current = dto.score_current
    )