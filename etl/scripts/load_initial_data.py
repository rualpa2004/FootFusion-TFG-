import time
from clients.football_data_client import FootballDataClient
from clients.highlightly_client import HighlightlyClient
from dtos.highlightly.league_dto import LeagueDTO
from dtos.footballdata.player_dto import FootballDataPlayerDTO
from dtos.footballdata.team_dto import FootballDataTeamDTO
from adapters.team_adapter import adapt_team_from_footballdata
from adapters.player_adapter import adapt_player_form_footballdata
from adapters.competition_adapter import adapt_competition
from repositories.competition_repository import save_competition
from repositories.player_repository import save_player
from repositories.team_repository import save_team

COMPETITIONS = [
    {"highlightly_id": 2486, "footballdata_code": "CL"},        #Champions League
    {"highlightly_id": 119924, "footballdata_code": "PD"},      #La Liga
    {"highlightly_id": 115669, "footballdata_code": "SA"},      #Serie A
    {"highlightly_id": 67162, "footballdata_code": "BL1"},      #Bundesliga
    {"highlightly_id": 52695, "footballdata_code": "FL1"},      #Ligue 1
    {"highlightly_id": 33973, "footballdata_code": "PL"}        #Premier League
]

highlightly_client = HighlightlyClient()
footballdata_client = FootballDataClient()

def load_competition(highlightly_id, footballdata_code):
    league_data = highlightly_client.get_league_by_id(highlightly_id)[0]
    dto = LeagueDTO.from_api(league_data)
    competition = adapt_competition(dto, footballdata_code)
    save_competition(competition)
    return competition

def load_teams_and_players(competition, season):
    teams_response = footballdata_client.get_teams_by_competition(competition.footballdata_code, season)

    for team_data in teams_response["teams"]:
        team_dto = FootballDataTeamDTO.from_api(team_data)
        team = adapt_team_from_footballdata(team_dto, competition.external_id)
        save_team(team)

        for player_data in team_data.get("squad", []):
            player_dto = FootballDataPlayerDTO.from_api(player_data)
            player = adapt_player_form_footballdata(player_dto, team.external_id)
            save_player(player)

        print(f"Equipo cargado: {team.name} ({len(team_data.get("squad", []))} jugadores)")

def run():
    season = 2025
    for entry in COMPETITIONS:
        competition = load_competition(entry["highlightly_id"], entry["footballdata_code"])
        print(f"Cargando competición: {competition.name}")
        load_teams_and_players(competition, season)
        time.sleep(10)

if __name__ == "__main__":
    run()