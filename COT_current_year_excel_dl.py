from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import os
import pandas as pd
import requests
import tempfile
import zipfile
from datetime import date
from COT_remove_xls_files import remove_xls_files

# Download and Save Each Year's Excel Report


def get_current_year_data():
    year = str(date.today().year)
    #url = 'https://www.cftc.gov/files/dea/history/dea_fut_xls_'+year+'.zip'

    url = ('https://www.cftc.gov/files/dea/history/dea_fut_xls_' + year + '.zip')
    print(url)

    r = requests.get(url, stream=True)
    with open(os.getcwd() + '\COT.zip', 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

    with zipfile.ZipFile(os.getcwd() + '\COT.zip', 'r') as zip_ref:
        zip_ref.extractall(
            r'COT Reports')

    for file_ in os.listdir(r'COT Reports'):
        if 'annual' in file_:
            old_file = os.path.join(r'COT Reports', file_)
            new_file = os.path.join(r'COT Reports', 'COT-'+year+'.xls')
            try:
                os.remove(new_file)
            except OSError:
                pass
            os.rename(old_file, new_file)
    df = pd.read_excel(r'COT Reports\COT-'+year+'.xls')
    df.to_csv(r'COT Reports\COT-'+year+'.csv')
    remove_xls_files()
