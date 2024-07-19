from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY,JSON
db = SQLAlchemy()
class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(255),nullable=False, unique=True)
    password=db.Column(db.String(255),nullable=False)
    game=db.relationship("Game",backref="user",lazy=True)
class Game(db.Model):
    __tablename__="game"
    id=db.Column(db.Integer,primary_key=True)
    lastplayed_move=db.Column(JSON)
    player_id=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    player_hand=db.Column(ARRAY(db.String))
    computer_hand=db.Column(ARRAY(db.String))
class Card(db.Model):
    __tablename__="card"
    id=db.Column(db.Integer,primary_key=True)
    suits=db.Column(db.String(255),nullable=False)
    rank=db.Column(db.String(255),nullable=False)
    image=db.Column(db.String(255),nullable=False)
    
def serialize_card(card):
    return {
        "id": card.id,
        "suits": card.suits,
        "rank": card.rank,
        "image": card.image
    }
