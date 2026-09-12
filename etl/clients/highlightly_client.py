import requests
from config.settings import HIGHLIGHTLY_API_KEY, HIGHLIGHTLY_BASE_URL

class HighlightlyClient:

    def __init__(self):
        self.base_url = HIGHLIGHTLY_BASE_URL
        self.headers = {"x-rapidapi-key": HIGHLIGHTLY_API_KEY}

    ## FUNCTIONS TO CREATE THE URL AND PARAMS FOR THE REQUESTS

    def get_all_leagues(self, season = None, country_name = None, limit = 100, offset = 0):
        url = f"{self.base_url}/leagues"
        params = {"limit": limit, "offset": offset}
        if season:
            params["season"] = season
        if country_name:
            params["country_name"] = country_name
        return self.make_request(url, self.headers, params)

    def get_teams_by_league(self, league_id, season):
        url = f"{self.base_url}/standings"
        params = {"leagueId": league_id, "season": season}
        return self.make_request(url, self.headers, params)

    def get_players_by_team(self, team_id, season, page=1):     ## TODO: IMPLEMENTAR EL MÉTODO PARA SACAR LOS JUGADORES DE UN EQUIPO
        url = f"{self.base_url}/players"
        params = {"team": team_id, "season": season, "page": page}
        return self.make_request(url, self.headers, params)

    def get_fixtures(self, league_id, season, round_name = None, limit = 100, offset = 0):
        url = f"{self.base_url}/matches"
        params = {"league": league_id, "season": season, "limit": limit, "offset": offset}
        response = self.make_request(url, self.headers, params)

        if round_name and isinstance(response, dict) and "data" in response:
            response["data"] = [
                match for match in response["data"]
                if match.get("round") == round_name
            ]
        return response

    def get_fixture_players(self, fixture_id):
        url = f"{self.base_url}/box-score/{fixture_id}"
        return self.make_request(url, self.headers)
    
    def get_fixture_statistics(self, fixture_id):
        url = f"{self.base_url}/statistics/{fixture_id}"
        return self.make_request(url, self.headers)
    
    def get_fixture_lineups(self, fixture_id):
        url = f"{self.base_url}/lineups/{fixture_id}"
        return self.make_request(url, self.headers)

    def get_match_by_id(self, fixture_id):
        url = f"{self.base_url}/matches/{fixture_id}"
        return self.make_request(url, self.headers)

    def get_player_by_id(self, player_id):
        url = f"{self.base_url}/players/{player_id}"
        return self.make_request(url, self.headers)

    def get_player_statistics(self, player_id):
        url = f"{self.base_url}/players/{player_id}/statistics"
        return self.make_request(url, self.headers)

    ## FUNCTION TO MAKE THE REQUESTS AT THE API
    def make_request(self, url, headers = None, params = None):
        response = requests.get(url, headers = headers, params = params)
        response.raise_for_status()
        return response.json()
