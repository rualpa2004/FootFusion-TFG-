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