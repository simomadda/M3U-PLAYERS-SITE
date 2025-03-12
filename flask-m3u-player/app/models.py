from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)
    episode_number = db.Column(db.Integer, nullable=False)
    m3u8_url = db.Column(db.String(255), nullable=False)
    series = db.relationship('Series', backref=db.backref('episodes', lazy=True))