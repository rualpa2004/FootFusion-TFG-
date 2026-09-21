from dataclasses import asdict
from config.database import get_database
from models.team import Team

def save_team(team: Team):
    db = get_database()
    db.teams.update_one(
        {"external_id": team.external_id},
        {"$set": asdict(team)},
        upsert = True
    )

def find_team_by_highlightly_id(highlightly_id):
    db = get_database()
    return db.teams.find_one({"highlightly_id": highlightly_id})

def find_team_by_name(name):
    db = get_database()
    return db.teams.find_one({"name": name})

def set_team_highlightly_id(team_external_id, highlightly_id):
    db = get_database()
    return db.teams.update_one({"external_id": team_external_id}, {"$set": {"highlightly_id": highlightly_id}})

def find_all_teams():
    db = get_database()
    return list(db.teams.find({}))