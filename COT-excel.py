from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import os
import requests
import tempfile
import zipfile
from datetime import date

# Download and Save Each Year's Excel Report

def get_all_cot_data():
    year = '2021'
    #url = 'https://www.cftc.gov/files/dea/history/dea_fut_xls_'+year+'.zip'
    
    for i in range(2021, 2022):
        year = str(i)
        url = ('https://www.cftc.gov/files/dea/history/dea_fut_xls_' + year + '.zip')
        print(url)

        r = requests.get(url, stream=True)
        with open(r'C:\Users\brent\Desktop\python projects\COT CFTC\COT.zip', 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

        with zipfile.ZipFile(r'C:\Users\brent\Desktop\python projects\COT CFTC\COT.zip', 'r') as zip_ref:
            zip_ref.extractall(r'C:\Users\brent\Desktop\python projects\COT CFTC\COT Reports')
            
        for file_ in os.listdir(r'COT Reports'):
            if 'annual.xls' in file_:
                old_file = os.path.join(r'COT Reports', 'annual.xls')
                new_file = os.path.join(r'COT Reports', 'COT-'+year+'.xls')
                os.rename(old_file, new_file)

get_all_cot_data()
