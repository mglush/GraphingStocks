import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go
import plotly.subplots as subp
from datetime import datetime, timedelta
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import numpy as np

pd.options.mode.chained_assignment = None

# Pull a json file from Alpha Vantage, store it into an excel file locally.

ALPHA_VANTAGE_API_KEY = 'K8PO7UJB8247TE1N' 
ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas') 
ticker = input("Enter ticker symbol of the stock you'd like to view: ")
ticker = ticker.upper();
userInterval = input("Enter the number of minutes to be included per bar: ")
userInterval = str(userInterval) + 'min'
intraday_data, data_info = ts.get_intraday( 
    ticker, outputsize='full', interval=userInterval) 
intraday_data.to_excel('stockData.xlsx')
cbh = pd.offsets.CustomBusinessHour(start='04:00', 
                                    end='21:00', 
                                    weekmask='Mon Tue Wed Thu Fri')

# Read the stock excel file into a pandas data frame.
df = pd.read_excel('stockData.xlsx', index_col=0)
bhours = pd.date_range(start=datetime.today() - timedelta(days=14), end=datetime.today(), freq=cbh)
bhoursSeries = bhours.to_series()
bhoursSeries = bhoursSeries.resample('T').pad()
df = df.reindex(bhoursSeries.index, fill_value=np.nan)
df.columns = ['open', 'low', 'high', 'close', 'volume']

# Find the corresponding colors for the volume bar graph.
df['color'] = ''
df['color'][0:] = (np.where(df['close'][0:] 
                              > df['open'][0:], 'green', df['color']))
df['color'][0:] = (np.where(df['close'][0:] 
                              == df['open'][0:], 'gray', df['color']))
df['color'][0:] = (np.where(df['close'][0:] 
                              < df['open'][0:], 'red', df['color']))
df['color'][0:] = (np.where(df['color'][0:] 
                              == '', 'black', df['color']))
# Create the traces to be charted.
trace1 = {
    'x': df.index,
    'open': df.open,
    'close': df.close,
    'high': df.high,
    'low': df.low,
    'type': 'candlestick',
    'name': ticker,
    'showlegend': True,
    'visible': True
}

trace5 = {
    'x': df.index,
    'y': df.close,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'black'
            },
    'name': ticker,
    'showlegend': True,
    'connectgaps':True,
    'visible': False
}

# Calculate and define moving average of 20, 50, 250 periods.
df['sma_20'] = df.close.rolling(window=20, min_periods=1).mean()
df['sma_50'] = df.close.rolling(window=50, min_periods=1).mean()
df['sma_250'] = df.close.rolling(window=250, min_periods=1).mean()

# Calculate bollinger bands.
bol_size = 2
mov_avg_size = 20
df['low_boll'] = df['sma_20'] + df['close'].rolling(window = mov_avg_size, min_periods=1).std() * bol_size
df['high_boll'] = df['sma_20'] - df['close'].rolling(window = mov_avg_size, min_periods=1).std() * bol_size

# Calculate RSI.
def computeRSI (data, window):
    diff = data.diff(1).dropna()    
    up = 0 * diff
    down = 0 * diff
    up[diff>0] = diff[ diff>0 ]
    down[diff<0] = diff[diff<0]
    avgUp   = up.ewm(com=window-1 , min_periods=window).mean()
    avgDown = down.ewm(com=window-1 , min_periods=window).mean()
    rs = abs(avgUp/avgDown)
    rsi = 100 - 100/(1+rs)
    return rsi

# Add RSI to dataframe and create a trace.
rsiTimePeriod = 14
df['RSI'] = computeRSI(df['close'], rsiTimePeriod)
trace11 = {
    'x': df.index,
    'y': df['RSI'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'lightblue'
    },
    'name': 'RSI ' + str(rsiTimePeriod),
    'connectgaps':True,
    'visible': True
}
trace2 = {
    'x': df.index,
    'y': df['sma_20'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
            },
    'name': 'SMA 20',
    'connectgaps':True,
    'visible': True
}
trace3 = {
    'x': df.index,
    'y': df['sma_50'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'gold'
    },
    'name': 'SMA 50',
    'connectgaps':True,
    'visible': True
}
trace4 = {
    'x': df.index,
    'y': df['sma_250'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'purple'
    },
    'name': 'SMA 250',
    'connectgaps':True,
    'visible': True
}
trace6 = {
    'x': df.index,
    'y': df['low_boll'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'black'
    },
    'name': 'Low Boll Band',
    'connectgaps':True,
    'visible': False
}
trace7 = {
    'x': df.index,
    'y': df['high_boll'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'black'
    },
    'name': 'High Boll Band',
    'connectgaps':True,
    'visible': False
}
trace8 = {
    'x': df.index,
    'y': df['volume'],
    'type': 'bar',
    'marker': {'color': df['color']},
    'orientation':"v",
    'name': 'Volume',
    'showlegend':True,
    'opacity':1,
    'visible':True
}

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]

# Config graph layout.
layout = go.Layout({
    'title': {
        'text': ticker + ' Stock Graph',
        'font': {
            'size': 15
        }
    },
    'plot_bgcolor':'rgba(255, 255, 255, 0)'
})

# Moving Averages Crossover Strategy.
df['signal'] = 0.0
df['signal'][50:] = (np.where(df['sma_50'][50:] 
                              >= df['sma_250'][50:], 1.0, 0.0))
# Here, 1 means buy, -1 means sell.
df['positions'] = df['signal'].diff()

trace9 = { 
    'name': 'BUY',
    'mode':"markers",
    'x':df.loc[df.positions == 1.0].index,
    'y':df.sma_50[df.positions == 1.0],
    'marker_symbol': 'triangle-up',
    'marker_line_color': "black",
    'marker_color': "green", 
    'marker_line_width': 2,
    'marker_size': 15,
    'visible': False
}
trace10 = { 
    'name': 'SELL',
    'mode':"markers",
    'x':df.loc[df.positions == -1.0].index,
    'y':df.sma_50[df.positions == -1.0],
    'marker_symbol': 'triangle-down',
    'marker_line_color': "black",
    'marker_color': "red", 
    'marker_line_width': 2,
    'marker_size': 15,
    'visible': False
}

fig = go.Figure(data=data, layout=layout)
fig = subp.make_subplots(rows = 5, cols = 1, specs=[[{"secondary_y": True, "rowspan":3}],
                                                    [None],
                                                    [None],
                                                    [None],
                                                    [{"secondary_y": False, "rowspan":1}]])
# Add the first 7 traces to our chart.
for i in range(7):
 fig.add_trace(data[i], row = 1, col = 1)


# Add the volume over the graphs.
fig.add_trace(trace8, row = 1, col = 1, secondary_y=True)

# Add buy and sell signals to the graph.
fig.add_trace(trace9, row = 1, col = 1)
fig.add_trace(trace10, row = 1, col = 1)
fig.add_trace(trace11, row = 5, col = 1)
fig['layout'].update(layout)
fig.update_yaxes(range=[0,df['volume'].max()*4], secondary_y=True)

# Indicator and chart buttons.
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=1,
            x=0.7,
            y=1.2,
            buttons=list([
                dict(label="Chart",
                     method="update",
                     args=[{"visible": [False, False, False, False, True, False, False, True, False, False, True]},
                           {"title": ticker + " Line Chart",
                            "annotations": []}]),
                dict(label="Candlesticks",
                     method="update",
                     args=[{"visible": [True, False, False, False, False, False, False, True, False, False, True]},
                           {"title": ticker + " Candlestick Chart",
                            "annotations": []}]),
                dict(label="Moving Averages",
                     method="update",
                     args=[{"visible": [False, True, True, True, True, False, False, True, False, False, True]},
                           {"title": ticker + " Moving Averages",
                            "annotations": []}]),
                dict(label="Bollinger Bands",
                     method="update",
                     args=[{"visible": [True, True, False, False, False, True, True, True, False, False, True]},
                           {"title": ticker + " Boll Bands",
                            "annotations": []}]),
                dict(label="MA Strategy",
                     method="update",
                     args=[{"visible": [False, True, True, True, True, False, False, True, True, True, True]},
                           {"title": ticker + " Strategy 1",
                            "annotations": []}])
            ])
        )
    ]
)

fig.update_yaxes(title_text="RSI", row = 5, col = 1)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0, 0, 0, 0.25)', row = 1, col = 1)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0, 0, 0, 0.25)', row = 1, col = 1)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0, 0, 0, 0.25)', row = 5, col = 1)

# Update the axis to hide weekends and hours on weekdays when the market is closed.
fig.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "mon"]),
        dict(bounds=[20, 4], pattern="hour")
    ]
)

# Create the html file.
fig.write_html("stockChart.html")

print("Type 'open stockChart.html' to view the chart!\n")
print("Type 'open stockChart.xlsx' to view the chart data!\n")