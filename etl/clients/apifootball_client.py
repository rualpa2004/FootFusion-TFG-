import requests
from config.settings import APIFOOTBALL_API_KEY, APIFOOTBALL_BASE_URL

class ApiFootballClient:

    def __init__(self):
        self.base_url = APIFOOTBALL_BASE_URL
        self.headers = {"x-apisports-key": APIFOOTBALL_API_KEY}

    ## FUNCTIONS TO CREATE THE URL AND PARAMS FOR THE REQUESTS

    def get_all_leagues(self):
        url = f"{self.base_url}/leagues"
        return self.make_request(url, self.headers)

    def get_teams_by_league(self, league_id, season):
        url = f"{self.base_url}/teams"
        params = {"league": league_id, "season": season}
        return self.make_request(url, self.headers, params)

    def get_players_by_team(self, team_id, season, page=1):
        url = f"{self.base_url}/players"
        params = {"team": team_id, "season": season, "page": page}
        return self.make_request(url, self.headers, params)

    def get_fixtures(self, league_id, season, round_name = None):
        url = f"{self.base_url}/fixtures"
        params = {"league": league_id, "season": season}
        if round_name:
            params["round_name"] = round_name
        return self.make_request(url, self.headers, params)

    def get_fixture_players(self, fixture_id):
        url = f"{self.base_url}/fixtures/players"
        params = {"fixture":fixture_id}
        return self.make_request(url, self.headers, params)
    
    def get_fixture_statistics(self, fixture_id):
        url = f"{self.base_url}/fixtures/statistics"
        params = {"fixture":fixture_id}
        return self.make_request(url, self.headers, params)
    
    def get_fixture_lineups(self, fixture_id):
        url = f"{self.base_url}/fixtures/lineups"
        params = {"fixture":fixture_id}
        return self.make_request(url, self.headers, params)

    ## FUNCTION TO MAKE THE REQUESTS AT THE API
    def make_request(url, headers = None, params = None):
        response = requests.get(url, headers = headers, params = params)
        response.raise_for_status()
        return response.json()
