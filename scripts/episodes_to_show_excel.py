import pandas as pd
import datetime as dt
import os, sys

# Get Dataframe of release dates
def make_episodes_df(inputFile: str) -> pd.DataFrame:
    episodes = pd.DataFrame.from_csv(inputFile, index_col=None, parse_dates=['release_date'])
    episodes = episodes[['release_date','item_title','downloads__total']]
    episodes.columns = ['release_date','title', 'downloads']
    episodes = episodes.sort_values(by='release_date')
    return episodes

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
    exportFileName = "TBPN_Downloads_" + str(dt.datetime.today())[:10] + ".xlsx"
    # shows = list(show_df.show)
    with pd.ExcelWriter(exportFileName) as writer:
        show_df.to_excel(writer, 'Weekly Downloads', index=False)

pathcorrect = True
while pathcorrect:
    if sys.argv[1]:
        print(sys.argv[1])
        inputFileName = sys.argv[1]
    else:
        inputFileName = input("Input a filename: ")
    if os.path.isfile(inputFileName):
        show_data_to_excel(inputFile=inputFileName)
        pathcorrect = False
    else:
        print("Fuck off, {} is not a filename".format(inputFileName))
        print("Try again \n")
