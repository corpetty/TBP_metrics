import scripts.soundcloud as sc
from datetime import timedelta, datetime

client_id = 'DjQCXgNUkh7MZaqgtwPYHqeyOwdKFdPd'

tracks = sc.get_track_downloads(show_name="cointelegraph", client_id=client_id)

date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

tracks.to_csv("/Users/coreypetty/PycharmProjects/TBP_metrics/raw_data/soundcloud/cointelegraph/daily-" + date)


