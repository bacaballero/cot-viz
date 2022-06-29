import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv(r'C:\Users\brent\Desktop\python projects\COT CFTC\COT Combined Report\COT-All.csv')

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Candlestick(x=df['Report_Date_as_MM_DD_YYYY'],
                    open=df['Open'],
				    high=df['High'],
				    low=df['Low'],
				    close=df['Close'],
                            name="Price"),
              secondary_y=False,)

fig.add_trace(go.Scatter(x=df['Report_Date_as_MM_DD_YYYY'], y=df['Comm_Net_All'], name="Commercial Hedgers"),
              secondary_y=True,)

fig.add_trace(go.Scatter(x=df['Report_Date_as_MM_DD_YYYY'], y=df['NonComm_Net_All'], name="Large Traders"),
              secondary_y=True,)

fig.add_trace(go.Scatter(x=df['Report_Date_as_MM_DD_YYYY'], y=df['NonRept_Net_All'], name="Small Traders"),
              secondary_y=True,)

fig.update_layout(
    title_text="Corn Futures vs COT Data"
    )

fig.update_xaxes(title_text="Time")

fig.update_yaxes(title_text="<b>Price of Corn</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Number of Contracts</b>", secondary_y=True)

fig.show()
