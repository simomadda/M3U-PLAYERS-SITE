from flask import render_template, redirect, url_for
from . import app, m3u8_service

@app.route('/')
def index():
    series_list = m3u8_service.get_series()
    return render_template('index.html', series_list=series_list)

@app.route('/series/<series_name>')
def series(series_name):
    episodes = m3u8_service.get_episodes(series_name)
    return render_template('series.html', series_name=series_name, episodes=episodes)

@app.route('/play/<series_name>/<int:episode_number>')
def play(series_name, episode_number):
    m3u8_url = m3u8_service.get_m3u8_url(series_name, episode_number)
    if not m3u8_url:
        return "Episode not found", 404
    return render_template('player.html', m3u8_url=m3u8_url)