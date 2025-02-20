import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb # optional to set plot theme
sb.set_theme() # optional to set plot theme
import yfinance as yf

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
     self.symbol = symbol
     self.start = start
     self.end = None
     self.data = ()


    def get_data(self):
        stock_data = yf.download(self.symbol, start=self.start, end=self.end)
        stock_data.index = pd.to_datetime(stock_data.index)  # Ensure index is DateTime object
        self.data = stock_data  # Store data in the object
        self.calc_returns()  # Call helper method to calculate returns


    
    def calc_returns(self, df):
        """Calculate daily price changes and log returns."""
        self.data['change'] = self.data['Close'].diff()  # Daily price change
        self.data['instant_return'] = np.log(self.data['Close']).diff().round(4)  # Log return


    
    def plot_return_dist(self):
        plt.figure(figsize=(8,5))
        plt.hist(self.data['instant_return'].dropna(), bins=30, alpha=0.75, color='blue')
        plt.xlabel("Instantaneous Return")
        plt.ylabel("Frequency")
        plt.title(f"Return Distribution for {self.symbol}")
        plt.grid(True)
        plt.show()



    def plot_performance(self):
        plt.figure(figsize=(10, 5))
        normalized_price = (self.data['Close'] / self.data['Close'].iloc[0]) * 100
        plt.plot(self.data.index, normalized_price, label=self.symbol, linewidth=2, color='green')
        plt.xlabel("Date")
        plt.ylabel("Price (% Gain/Loss)")
        plt.title(f"Stock Performance for {self.symbol}")
        plt.legend()
        plt.grid(True)
        plt.show()

                  


def main():
    # Define the stock symbol you want to analyze
    stock_symbol = "AAPL"

    # Create an instance of the Stock class
    test = Stock(symbol=stock_symbol)  # You can add start/end dates if needed

    # Print the first few rows of the data to verify it was fetched
    print(test.data.head())

    # Plot stock performance over time
    test.plot_performance()

    # Plot the return distribution histogram
    test.plot_return_dist()


if __name__ == '__main__':
    main() 