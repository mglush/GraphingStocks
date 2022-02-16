## Stock Charting and Technical Analysis with Python

Graphing stock market tickers and the statistical analysis indicators that come with them. Implementing a multitude of trading strategies based on these indicators. Backtesting the trading strategies, finding the best ones.

## Table of Contents
* [Motivation](https://github.com/mglush/graphingStocks/blob/main/README.md#motivation)
* [Work So Far](https://github.com/mglush/graphingStocks/blob/main/README.md#work-so-far)
* [Features](https://github.com/mglush/graphingStocks/blob/main/README.md#features)
* [Installation](https://github.com/mglush/graphingStocks/blob/main/README.md#installation)
* [How to Use](https://github.com/mglush/graphingStocks/blob/main/README.md#how-to-use)
* [Next Steps](https://github.com/mglush/graphingStocks/blob/main/README.md#next-steps)
* [Credits](https://github.com/mglush/graphingStocks/blob/main/README.md#credits)

## Motivation

An attempt to create successful trading strategies for the stock market, and using statistics to analyze the data and results. Eventually expandable to include machine learning models that would employ these trading strategies.

## Work So Far
Stock ticker in the example: WKHS

* Charted the closing price of the ticker:
![closing price](/images/Chart.jpg)

* Able to look at the Candlestick chart:
![candle](/images/Candle.jpg)

* Use of Moving Averages and Bollinger Bands:

Moving Averages             |  Bollinger Bands
:-------------------------:|:-------------------------:
![](/images/MA.jpg)              |  ![](/images/BollBands.jpg)

* Buy/Sell Strategy 1: MA crossover

![strat](/images/MAstrat.jpg)

## Features
* View individual tickers' intraday data for the last two weeks.
* Chart the chosen ticker and strategy of choice.
* Chart multiple tickers to compare relation between price fluctuations in the two.


## Installation
* **git clone https://github.com/mglush/graphingStocks.git** to get the repository.
* **cd graphingStocks** to enter the folder.
* **python graphing.py** to run the file.
* **open stockChart.html** to inspect the chart.

## How to use
Once new strategies are implemented, you will be able to:
* Run the program.
* Choose the ticker(s) and the strategy.
* View the ticker and strategy charts in the *stockChart.html* file.
* View the data for the ticker in the *stockData.xlsx* file.

## Next Steps
1. Implement and refine new strategies for buy/sell signals.
2. View the success of your strategy in a series of matplotlib charts, including percent change of the portfolio, highest and lowest portfolio values over the timeperiod, the statistical analysis of strategy effectiveness, regression charts relating the price change of multiple tickers (if more than one is entered).
3. Implement the running of multiple simulations competing against each other on the stock market, with each simulation employing a different trading strategy.
4. Connect the strategy of choice to a backtesting software, and deploy the strategy to trade in a real market.
5. Make an option to allow the user to enter multiple tickers.
6. Make an option to allow the user to choose the timeframe they want to inspect/trade.
7. Make an option to allow the user to combine trading strategies.
8. Allow the user to enter a filename with their own trading strategy, that this program will then use.
9. Find the best set of statistical analysis indicators which a simulation can use to profit the most in comparison to other available strategies.
10. Train and compare statistical and machine learning models and results, compare to financial approaches to the stock market within intraday trading.

## Credits
2021 © Michael Glushchenko.
