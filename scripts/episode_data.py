import pandas as pd
import datetime as dt

# Get Dataframe of release dates
def make_episodes_df(inputFile: str) -> pd.DataFrame:
    episodes = pd.DataFrame.from_csv(inputFile, index_col=None, parse_dates=['release_date'])
    episodes = episodes[['release_date','item_title','downloads__total']]
    episodes.columns = ['release_date','title', 'downloads']
    episodes = episodes.sort_values(by='release_date')
    return episodes

# Creates a DataFrame that has which day of week a show aired on.
def make_day_of_week_df(daily_df: pd.DataFrame) -> pd.DataFrame:
    days_of_week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    df_wkdays = daily_df
    df_wkdays['weekday'] = df_wkdays.reset_index().date.dt.dayofweek.values
    df_wkdays = df_wkdays.reset_index().pivot(index='date', columns='weekday', values='total_downloads')
    df_wkdays.columns = days_of_week.values()
    return df_wkdays

# Get show name from Title
def get_show(title):
    if "BlockChannel" in title:
        return 'BlockChannel'
    elif 'On-Ramping' in title:
        return 'On-Ramping with Dee'
    elif 'Announcements' in title:
        return 'Announcements with Dr. Petty'
    elif 'NABP' in title:
        return 'Not Another Bitcoin Podcast'
    elif 'Ether Review' in title:
        return "The Ether Review"
    else:
        return 'The Bitcoin Podcast'

def show_data_to_excel(inputFile: str):
    show_df = make_episodes_df(inputFile)
    show_df['show'] = show_df.title.apply(get_show)
    exportFileName = "TBPN_show_data_" + str(dt.datetime.today())[:10] + ".xlsx"
    # shows = list(show_df.show)
    with pd.ExcelWriter(exportFileName) as writer:
        for show, group in show_df.groupby('show'):
            group.to_excel(writer, show, index=False)

