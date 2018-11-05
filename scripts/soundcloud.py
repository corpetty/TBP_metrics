import pandas as pd
import requests
import scripts.utils as utils


def get_track_downloads(show_name: str, client_id: str) -> pd.DataFrame:
    url = 'http://api.soundcloud.com/resolve?url=http://soundcloud.com/' + show_name + '/tracks&client_id=' + client_id
    tracks = requests.get(url=url)
    tracks = tracks.json()

    stats = []
    for track in tracks:
        url2 = "https://api-v2.soundcloud.com/tracks/" + str(track['id']) + "?client_id=" + client_id
        res = requests.get(url=url2).json()
        stats.append([res['title'], res['playback_count']])

    stats = pd.DataFrame(stats, columns=['title', 'playback_count'])
    stats['title'] = [utils.dequote(title) for title in stats.title]
    stats = stats.set_index('title')
    return stats
