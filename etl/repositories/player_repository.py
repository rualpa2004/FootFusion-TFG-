from dataclasses import asdict
from config.database import get_database
from models.player import Player

def save_player(player: Player):
    db = get_database()
    db.players.update_one(
        {"external_id": player.external_id},
        {"$set": asdict(player)},
        upsert = True
    )