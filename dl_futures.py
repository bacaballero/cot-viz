import pandas as pd
import yfinance as yf

data = yf.download(
    tickers= '''
    ZC=F 
    ZO=F 
    ZS=F 
    ZL=F 
    ZB=F 
    UB=F 
    HO=F 
    NG=F 
    ZM=F 
    ZT=F 
    ZN=F 
    ZF=F 
    ZQ=F
    HE=F
    LE=F
    CL=F
    RB=F
    PL=F
    SI=F
    HG=F
    GC=F
    VX=F
    YM=F
    GE=F
    BTC=F
    ES=F
    NQ=F
    NKD=F
    ''',
    period='max',
    interval='1wk',
    group_by='ticker'
)

df = pd.DataFrame(data)
print(df)