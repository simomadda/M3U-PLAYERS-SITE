from flask import Flask
from flask_pymongo import PyMongo
from flask_admin import Admin
from .m3u8Service import M3U8Service
from .admin_views import AddSeriesView
from .custom_views import SeriesView, EpisodesView

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://medusa:8RB2QKdStaeapkVQ@cluster0.hykx6.mongodb.net/flask_m3u_player'
app.config['SECRET_KEY'] = b'your_generated_secret_key'  # Replace with your generated secret key

mongo = PyMongo(app)

# Ensure collections are created
with app.app_context():
    if 'series' not in mongo.db.list_collection_names():
        mongo.db.create_collection('series')
    if 'episodes' not in mongo.db.list_collection_names():
        mongo.db.create_collection('episodes')

admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
admin.add_view(SeriesView(mongo, name='Series', endpoint='series'))
admin.add_view(EpisodesView(mongo, name='Episodes', endpoint='episodes'))
admin.add_view(AddSeriesView(mongo, name='Add Series', endpoint='add_series'))

m3u8_service = M3U8Service(mongo)

from . import routes

