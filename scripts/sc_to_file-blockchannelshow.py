import scripts.soundcloud as sc
from datetime import timedelta, datetime

client_id = 'DjQCXgNUkh7MZaqgtwPYHqeyOwdKFdPd'
show_name = "blockchannelshow"

tracks = sc.get_track_downloads(show_name=show_name, client_id=client_id)

date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

tracks.to_csv("/Users/coreypetty/PycharmProjects/TBP_metrics/raw_data/soundcloud/" + show_name + "/daily-" + date)

