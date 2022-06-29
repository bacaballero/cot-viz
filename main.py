import os
from datetime import date, datetime
import time
from tkinter import Y
from matplotlib.pyplot import get
import pandas as pd
from COT_current_year_excel_dl import get_current_year_data
from COT_combine_COT_reports import append_COT_reports, combine_COT_reports
from COT_All_rpts_to_json import cot_all_to_json
from COT_dl_all_excels import get_all_years_data


def check_if_COT_reports_present():
    dir_name = os.path.dirname(__file__)
    folder_name = os.path.join(dir_name, 'COT Reports')
    file_list = os.listdir(folder_name)

    if (dir_name + '\COT Combined Report\COT-All.csv'):
        df = pd.read_csv(dir_name + '\COT Combined Report\COT-All.csv')

        max_date = df['Report_Date_as_MM_DD_YYYY'].max()
        min_date = df['Report_Date_as_MM_DD_YYYY'].min()
        max_datestring = datetime.strptime(max_date, '%Y-%m-%d')
        min_datestring = datetime.strptime(min_date, '%Y-%m-%d')

        if int(min_datestring.year) < 2005 and int(max_datestring.year) == date.today().year:
            return True
    else:
        return False


if check_if_COT_reports_present():
    get_current_year_data()
    append_COT_reports()
    cot_all_to_json()
else:
    get_all_years_data()
    combine_COT_reports()
    cot_all_to_json()
