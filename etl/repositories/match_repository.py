from dataclasses import asdict
from config.database import get_database
from models.match import Match

def save_match(match: Match):
    db = get_database()
    db.matches.update_one(
        {"external_id": match.external_id},
        {"$set": asdict(match)},
        upsert = True
    )