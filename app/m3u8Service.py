from bson.objectid import ObjectId

class M3U8Service:
    def __init__(self, mongo):
        self.mongo = mongo

    def get_m3u8_url(self, series_name, episode_number):
        series = self.mongo.db.series.find_one({'name': series_name.lower()})
        if series:
            episode = self.mongo.db.episodes.find_one({'series_id': series['_id'], 'episode_number': episode_number})
            if episode:
                return episode['m3u8_url']
        return None

    def get_series(self):
        return [series['name'] for series in self.mongo.db.series.find()]

    def get_episodes(self, series_name):
        series = self.mongo.db.series.find_one({'name': series_name.lower()})
        if series:
            episodes = self.mongo.db.episodes.find({'series_id': series['_id']})
            return {episode['episode_number']: episode['m3u8_url'] for episode in episodes}
        return {}