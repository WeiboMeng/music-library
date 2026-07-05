from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_background = db.Column(db.String(100))
    profession = db.Column(db.String(50))
    active_years = db.Column(db.String(50))
    biography = db.Column(db.Text)
    region = db.Column(db.String(50))
    image = db.Column(db.String(100))

    def __repr__(self):
        return f'<Artist {self.name}>'
    
class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    album = db.Column(db.String(100))
    genre = db.Column(db.String(50))
    released_date = db.Column(db.Date)
    image = db.Column(db.String(100))

    def __repr__(self):
        return f'<Song {self.title}>'
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)