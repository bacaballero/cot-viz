import pandas as pd
import matplotlib.pyplot as plt
#import plotly.graph_objects as go

'''
df = pd.read_excel(r'C:\Users\brent\Desktop\annual.xls')

df.set_index('Market_and_Exchange_Names')

df['Comm_Net_All'] = df['Comm_Positions_Long_All'] - df['Comm_Positions_Short_All']
df['NonComm_Net_All'] = df['NonComm_Positions_Long_All'] - df['NonComm_Positions_Short_All']
df['NonRept_Net_All'] = df['NonRept_Positions_Long_All'] - df['NonRept_Positions_Short_All']
'''

futures_list = ['CORN - CHICAGO BOARD OF TRADE',
           'OATS - CHICAGO BOARD OF TRADE',
           'SOYBEANS - CHICAGO BOARD OF TRADE',
           'SOYBEAN OIL - CHICAGO BOARD OF TRADE',
           'U.S. TREASURY BONDS - CHICAGO BOARD OF TRADE',
           'ULTRA U.S. TREASURY BONDS - CHICAGO BOARD OF TRADE',
           '#2 HEATING OIL- NY HARBOR-ULSD - NEW YORK MERCANTILE EXCHANGE',
           'NATURAL GAS - NEW YORK MERCANTILE EXCHANGE',
           'SOYBEAN MEAL - CHICAGO BOARD OF TRADE',
           '2-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE',
           '10-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE',
           '5-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE',
           '30-DAY FEDERAL FUNDS - CHICAGO BOARD OF TRADE',
           'LEAN HOGS - CHICAGO MERCANTILE EXCHANGE',
           'LIVE CATTLE - CHICAGO MERCANTILE EXCHANGE',
           'RANDOM LENGTH LUMBER - CHICAGO MERCANTILE EXCHANGE',
           'FEEDER CATTLE - CHICAGO MERCANTILE EXCHANGE',
           'CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE',
           'GASOLINE BLENDSTOCK (RBOB) - NEW YORK MERCANTILE EXCHANGE',
           'PLATINUM - NEW YORK MERCANTILE EXCHANGE',
           'SILVER - COMMODITY EXCHANGE INC.',
           'COPPER-GRADE #1 - COMMODITY EXCHANGE INC.',
           'GOLD - COMMODITY EXCHANGE INC.' 'MICRO GOLD - COMMODITY EXCHANGE INC.',
           'VIX FUTURES - CBOE FUTURES EXCHANGE',
           'DOW JONES INDUSTRIAL AVG- x $5 - CHICAGO BOARD OF TRADE',
           '3-MONTH EURODOLLARS - CHICAGO MERCANTILE EXCHANGE',
           'BITCOIN - CHICAGO MERCANTILE EXCHANGE',
           'S&P 500 STOCK INDEX - CHICAGO MERCANTILE EXCHANGE',
           'E-MINI S&P 500 STOCK INDEX - CHICAGO MERCANTILE EXCHANGE',
           'NASDAQ-100 STOCK INDEX (MINI) - CHICAGO MERCANTILE EXCHANGE',
           'E-MINI RUSSELL 2000 INDEX - CHICAGO MERCANTILE EXCHANGE',
           'NIKKEI STOCK AVERAGE - CHICAGO MERCANTILE EXCHANGE'
           ]
'''
is_corn = df['Market_and_Exchange_Names']=='CORN - CHICAGO BOARD OF TRADE'
corn_df = df[is_corn]
corn_df = corn_df[['Report_Date_as_MM_DD_YYYY','Comm_Net_All','NonComm_Net_All','NonRept_Net_All']]
corn_df.set_index('Report_Date_as_MM_DD_YYYY', inplace=True)
print(corn_df.plot.line(xlabel='Report Date', ylabel='Number of Contracts'))


is_soybeans = df['Market_and_Exchange_Names']=='SOYBEANS - CHICAGO BOARD OF TRADE'
soybean_df = df[is_soybeans]
soybean_df = soybean_df[['Report_Date_as_MM_DD_YYYY','Comm_Net_All','NonComm_Net_All','NonRept_Net_All']]
soybean_df.set_index('Report_Date_as_MM_DD_YYYY', inplace=True)
print(soybean_df.plot.line(xlabel='Report Date', ylabel='Number of Contracts'))
plt.show()
'''

'''
for future in futures_list:
    is_future_df = df['Market_and_Exchange_Names']==future
    future_df = df[is_future_df]
    future_df = future_df[['Report_Date_as_MM_DD_YYYY','Comm_Net_All','NonComm_Net_All','NonRept_Net_All']]
    future_df.set_index('Report_Date_as_MM_DD_YYYY', inplace=True)
    future_df.plot.line(xlabel='Report Date', ylabel='Number of Contracts')
    plt.title(future)
    #plt.show()
'''