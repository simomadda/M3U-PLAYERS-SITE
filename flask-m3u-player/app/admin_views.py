from flask import request, redirect, url_for, render_template
from flask_admin import BaseView, expose
from .m3u8Service import M3U8Service

class AddSeriesView(BaseView):
    def __init__(self, mongo, *args, **kwargs):
        super(AddSeriesView, self).__init__(*args, **kwargs)
        self.mongo = mongo

    @expose('/', methods=['GET', 'POST'])
    def index(self):
        if request.method == 'POST':
            series_name = request.form['series_name']
            episodes_text = request.form['episodes']
            episodes = self.parse_episodes(episodes_text)
            self.add_series(series_name, episodes)
            return redirect(url_for('.index'))
        return self.render('admin/add_series.html')

    def parse_episodes(self, episodes_text):
        episodes = {}
        for line in episodes_text.split('\n'):
            if line.strip():
                parts = line.split(': ')
                episode_number = int(parts[0].replace('Episode ', '').strip())
                m3u8_url = parts[1].strip()
                episodes[episode_number] = m3u8_url
        return episodes

    def add_series(self, series_name, episodes):
        series = self.mongo.db.series.find_one({'name': series_name.lower()})
        if not series:
            series_id = self.mongo.db.series.insert_one({'name': series_name.lower()}).inserted_id
        else:
            series_id = series['_id']
        for episode_number, m3u8_url in episodes.items():
            self.mongo.db.episodes.update_one(
                {'series_id': series_id, 'episode_number': episode_number},
                {'$set': {'m3u8_url': m3u8_url}},
                upsert=True
            )