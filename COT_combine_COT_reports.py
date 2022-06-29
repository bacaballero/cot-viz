from datetime import date
import os
import pandas as pd
from futures_list import futures_list

renamed_commodities = {
    'U.S. TREASURY BONDS - CHICAGO BOARD OF TRADE': 'UST BOND - CHICAGO BOARD OF TRADE',
    'ULTRA U.S. TREASURY BONDS - CHICAGO BOARD OF TRADE': 'ULTRA UST BOND - CHICAGO BOARD OF TRADE',
    '#2 HEATING OIL- NY HARBOR-ULSD - NEW YORK MERCANTILE EXCHANGE': 'NY HARBOR ULSD - NEW YORK MERCANTILE EXCHANGE',
    '#2 HEATING OIL- NY HARBOR-ULSD - NEW YORK MERCANTILE EXCHANGE': 'NY HARBOR ULSD - NEW YORK MERCANTILE EXCHANGE',
    'NY HARBOR USLD - NEW YORK MERCANTILE EXCHANGE': 'NY HARBOR ULSD - NEW YORK MERCANTILE EXCHANGE',
    '3-MONTH EURODOLLARS - CHICAGO MERCANTILE EXCHANGE': 'EURODOLLARS-3M - CHICAGO MERCANTILE EXCHANGE',
    '30-DAY FEDERAL FUNDS - CHICAGO BOARD OF TRADE': 'FED FUNDS - CHICAGO BOARD OF TRADE',
    'NATURAL GAS - NEW YORK MERCANTILE EXCHANGE': 'NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE',
    '2-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE': 'UST 2Y NOTE - CHICAGO BOARD OF TRADE',
    '10-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE': 'UST 10Y NOTE - CHICAGO BOARD OF TRADE',
    '5-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE': 'UST 5Y NOTE - CHICAGO BOARD OF TRADE',
    'CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE': 'WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE',
    'COPPER-GRADE #1 - COMMODITY EXCHANGE INC.': 'COPPER- #1 - COMMODITY EXCHANGE INC.',
    'GASOLINE BLENDSTOCK (RBOB) - NEW YORK MERCANTILE EXCHANGE': 'GASOLINE RBOB - NEW YORK MERCANTILE EXCHANGE',
    'DOW JONES INDUSTRIAL AVG- x $5 - CHICAGO BOARD OF TRADE': 'DJIA x $5 - CHICAGO BOARD OF TRADE',
    'E-MINI S&P 500 STOCK INDEX - CHICAGO MERCANTILE EXCHANGE': 'E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE',
    'NASDAQ-100 STOCK INDEX (MINI) - CHICAGO MERCANTILE EXCHANGE': 'NASDAQ MINI - CHICAGO MERCANTILE EXCHANGE',
    'E-MINI RUSSELL 2000 INDEX - CHICAGO MERCANTILE EXCHANGE': 'RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE',
}


def append_COT_reports():
    '''
    Append the current year's csv file to the existing 'COT-All' csv file
    '''
    dir_name = os.path.dirname(__file__)
    folder_name = os.path.join(dir_name, 'COT Reports')
    file_list = os.listdir(folder_name)

    year = date.today().year
    full_df = pd.read_csv(os.path.join(
        dir_name, 'COT Combined Report\COT-All.csv'))

    year = str(date.today().year)
    path = folder_name + '\COT-'+year+'.csv'

    df = pd.read_csv(path)

    df.set_index('Market_and_Exchange_Names')

    df['Comm_Net_All'] = df['Comm_Positions_Long_All'] - \
        df['Comm_Positions_Short_All']
    df['NonComm_Net_All'] = df['NonComm_Positions_Long_All'] - \
        df['NonComm_Positions_Short_All']
    df['NonRept_Net_All'] = df['NonRept_Positions_Long_All'] - \
        df['NonRept_Positions_Short_All']

    for future in futures_list:
        print(f"Year: {year} - Future: {future}")
        is_future_df = df['Market_and_Exchange_Names'] == future
        future_df = df[is_future_df]
        future_df = future_df[['Market_and_Exchange_Names', 'Report_Date_as_MM_DD_YYYY',
                               'Comm_Net_All', 'NonComm_Net_All', 'NonRept_Net_All']]
        full_df = full_df.append(future_df)

    full_df['Market_and_Exchange_Names'] = full_df['Market_and_Exchange_Names'].replace(
        renamed_commodities)
    full_df.dropna()
    full_df.drop_duplicates(subset=['Market_and_Exchange_Names',
                            'Comm_Net_All', 'NonComm_Net_All', 'NonRept_Net_All'], inplace=True)
    full_df.set_index('Market_and_Exchange_Names', inplace=True)
    full_df['Report_Date_as_MM_DD_YYYY'] = pd.to_datetime(
        full_df['Report_Date_as_MM_DD_YYYY'])
    full_df.sort_values(by=['Market_and_Exchange_Names',
                        'Report_Date_as_MM_DD_YYYY'], inplace=True)

    full_df.to_csv(os.path.join(dir_name, 'COT Combined Report\COT-All.csv'))


def combine_COT_reports():
    '''
    Combine all COT reports into a csv file 'COT-All.csv'
    '''
    dir_name = os.path.dirname(__file__)
    folder_name = os.path.join(dir_name, 'COT Reports')
    file_list = os.listdir(folder_name)

    full_df = pd.DataFrame()

    for file in file_list:
        path = os.path.join(folder_name, file)

        print(path)
        df = pd.read_csv(path)

        df.set_index('Market_and_Exchange_Names')

        df['Comm_Net_All'] = df['Comm_Positions_Long_All'] - \
            df['Comm_Positions_Short_All']
        df['NonComm_Net_All'] = df['NonComm_Positions_Long_All'] - \
            df['NonComm_Positions_Short_All']
        df['NonRept_Net_All'] = df['NonRept_Positions_Long_All'] - \
            df['NonRept_Positions_Short_All']

        for future in futures_list:
            print(f"File: {file} - Future: {future}")
            is_future_df = df['Market_and_Exchange_Names'] == future
            future_df = df[is_future_df]
            future_df = future_df[['Market_and_Exchange_Names', 'Report_Date_as_MM_DD_YYYY',
                                   'Comm_Net_All', 'NonComm_Net_All', 'NonRept_Net_All']]
            full_df = full_df.append(future_df)

        full_df['Market_and_Exchange_Names'] = full_df['Market_and_Exchange_Names'].replace(
            renamed_commodities)
        full_df.drop_duplicates(subset=[
                                'Market_and_Exchange_Names', 'Comm_Net_All', 'NonComm_Net_All', 'NonRept_Net_All'], inplace=True)
        full_df['Report_Date_as_MM_DD_YYYY'] = pd.to_datetime(
            full_df['Report_Date_as_MM_DD_YYYY'])
        full_df.sort_values(
            by=['Market_and_Exchange_Names', 'Report_Date_as_MM_DD_YYYY'], inplace=True)

    full_df.set_index('Market_and_Exchange_Names', inplace=True)
    full_df.to_csv(os.path.join(dir_name, 'COT Combined Report\COT-All.csv'))


append_COT_reports()
