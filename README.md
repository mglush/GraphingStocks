## Stock Charting and Technical Analysis

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
First stock worked on: '$WKHS'

* Charted the closing price of the ticker:
![closing price](/Chart.jpg)

* Able to look at the Candlestick chart:
![candle](/Candle.jpg)

* Use of Moving Averages and Bollinger Bands:

Moving Averages             |  Bollinger Bands
:-------------------------:|:-------------------------:
![](/MA.jpg)              |  ![](/BollBands.jpg)

* Buy/Sell Strategy 1: MA crossover

![strat](/MAstrat.jpg)

## Features
* View individual tickers' intraday data for the last two weeks.
* Chart the chosen ticker and strategy of choice.
* Chart multiple tickers to compare relation between price fluctuations in the two.


## Installation
* Open the terminal, and type in **git clone https://github.com/mglush/graphingStocks.git**.
* **cd graphingStocks** to enter the folder.
* Convert the Jupyter notebook file to a python file by using **jupyter nbconvert --to python 'Graphing Stocks'.ipynb**.
* You will now be able to run the python file with **python 'Graphing Stocks'.py**.

## How to use
Once new strategies are implemented, you will be able to:
* Run the program.
* Choose the ticker(s) and the strategy.
* View the ticker and strategy charts in the *'[Ticker Symbol] Stock Chart'.html* file.
* View the data for the ticker in the *'[Ticker Symbol] Stock Chart'.xlsx* file.

## Next Steps
* View the success of your strategy in a series of matplotlib charts, including percent change of the portfolio, highest and lowest portfolio values over the timeperiod, the statistical analysis of strategy effectiveness, regression charts relating the price change of multiple tickers (if more than one is entered).
* Make an option to allow the user to enter multiple tickers.
* Implement and refine new strategies for buy and sell signals.
* Implement the running of multiple simulations competing against each other on the stock market, with each simulation employing a different trading strategy.
* Find the best set of 2-3 statistical analysis indicators which a simulation can use to profit the most in today's market.
* Train and compare statistical and machine learning models and results, compare to financial approaches to the stock market within intraday trading.
* Potentially allow users to enter a filename with their own trading strategy, that this program will then use.

## Credits
2020 © Michael Glushchenko.
