__author__ = 'Corey Petty'
import pandas as pd
import os.path
import datetime

# dailyFile = input("Please input the daily downloads filename: ")
# daily_metrics = pd.DataFrame.from_csv(dailyFile, index_col=None, parse_dates=[0])


def update_daily_csv(daily_database_filename, daily_additions_filename):
    if not os.path.isfile(daily_database_filename):
        print("{} does not exist, try again".format(daily_database_filename))
        raise FileExistsError
    if not os.path.isfile(daily_additions_filename):
        print("{} does not exist, try again".format(daily_additions_filename))
        raise FileExistsError

    path = os.path.dirname(daily_database_filename)
    filename, extention = os.path.basename(daily_database_filename).split('.')

    print("Files exist")

    database = pd.read_csv(daily_database_filename, parse_dates=[0])
    addition = pd.read_csv(daily_additions_filename, parse_dates=[0])

    print("pandas DataFrames created")

    database = database[['date', 'total_downloads']].set_index('date')
    addition = addition.set_index('date')

    print("DataFrames structured correctly")

    database.update(addition)

    print("Old entries updated with newest data")

    df = pd.merge(database, addition, how='right', left_index=True, right_index=True)
    addition = df[df.total_downloads_x.isnull()].total_downloads_y
    addition = pd.DataFrame(addition)
    addition.columns = ['total_downloads']

    database = database.append(addition)
    database = database.sort_index()

    print("Adding the following days to the database:")
    print(addition)

    new_database_filename = path + '/' + "daily-totals_" + str(datetime.date.today()) + '.' + extention

    database.to_csv(new_database_filename)

