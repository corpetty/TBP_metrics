import pymysql
from scripts.utils import get_time_from_filename, get_show_name
import pandas as pd
from scripts.daily_data import u

def episodic(filename):
    date_string = get_time_from_filename(filename)
    df = pd.read_csv(filename, parse_dates=['release_date'])
    df = df[['item_title', 'release_date', 'downloads__total']]
    df.columns = ['title', 'release_date', 'downloads']
    df['update_date'] = [date_string for _ in df.title.values]
    df['show'] = df.title.apply(get_show_name)

    # Make connection

    # Check for Document

    # Ingest based on answr

    print(df.head())

