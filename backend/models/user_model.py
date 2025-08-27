from flask_sqlalchemy import SQLAlchemy
from backend import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name, username, password, is_admin=False):
        self.name = name
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f"<User id={self.id} username={self.username} is_admin={self.is_admin}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "is_admin": self.is_admin
        }