from dataclasses import asdict
from config.database import get_database
from models.competition import Competition

def save_competition(competition: Competition):
    db = get_database()
    db.competitions.update_one(
        {"external_id": competition.external_id},
        {"$set": asdict(competition)},
        upsert = True
    )