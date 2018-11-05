"""
created from the sc_to_influx jupyter notebook in TBP_metrics/scripts project folder
date created: April 24, 2017
author: Corey Petty
"""

import pandas as pd
import requests
import influxdb

def dequote(s: str):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

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
    stats['title'] = [dequote(title) for title in stats.title]
    stats = stats.set_index('title')
    return stats

client_id = 'DjQCXgNUkh7MZaqgtwPYHqeyOwdKFdPd'
show_name = "blockchannelshow"

tracks = get_track_downloads(show_name=show_name, client_id=client_id)
tracks = tracks.reset_index()

def create_json(title, count) -> dict:
    return {
        "measurement": "blockchannel",
        "tags": {
            "episode": title,
        },
        "fields": {
            "value": count
        }
    }

tracks['json'] = [create_json(title, count) for title,count in zip(tracks.title.values, tracks.playback_count.values)]
client = influxdb.InfluxDBClient(host="192.168.1.199", database='sc_downloads')
array = []
for json_object in tracks.json.values:
    array.append(json_object)
client.write_points(array)
