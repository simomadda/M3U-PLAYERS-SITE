from flask_admin import BaseView, expose
from flask import request, redirect, url_for, render_template

class SeriesView(BaseView):
    def __init__(self, mongo, *args, **kwargs):
        super(SeriesView, self).__init__(*args, **kwargs)
        self.mongo = mongo

    @expose('/')
    def index(self):
        series = list(self.mongo.db.series.find())
        return self.render('admin/series_list.html', series=series)

class EpisodesView(BaseView):
    def __init__(self, mongo, *args, **kwargs):
        super(EpisodesView, self).__init__(*args, **kwargs)
        self.mongo = mongo

    @expose('/')
    def index(self):
        episodes = list(self.mongo.db.episodes.find())
        return self.render('admin/episodes_list.html', episodes=episodes)