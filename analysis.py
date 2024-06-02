import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# List of companies
companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'BRK.B', 'V', 'JNJ', 'WMT']

# Function to analyze data for a given symbol
def analyze_stock(symbol):
    try:
        df = pd.read_csv(f'stock_data_{symbol}.csv', index_col=0, parse_dates=True)
        
        # Calculate Moving Averages
        df['SMA50'] = df['close'].rolling(window=50).mean()
        df['SMA200'] = df['close'].rolling(window=200).mean()
        
        # Calculate Daily Returns
        df['returns'] = df['close'].pct_change()
        
        # Calculate Average Returns
        avg_return = df['returns'].mean()
        
        # Calculate Volatility
        volatility = df['returns'].std()
        
        # Calculate Cumulative Returns
        df['cumulative_returns'] = (1 + df['returns']).cumprod()
        
        # Data Visualization
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 18), sharex=True)
        
        # Plot Close Price and SMAs on the first subplot
        ax1.plot(df['close'], label='Close Price', color='blue')
        ax1.plot(df['SMA50'], label='50-day SMA', linestyle='--', color='orange')
        ax1.plot(df['SMA200'], label='200-day SMA', linestyle='--', color='green')
        ax1.set_title(f'{symbol} Stock Price and Moving Averages')
        ax1.set_ylabel('Price')
        ax1.legend()
        ax1.grid(True)
        
        # Plot Daily Returns on the second subplot
        ax2.plot(df['returns'], label='Daily Returns', color='purple')
        ax2.axhline(y=avg_return, color='red', linestyle='-', label='Average Return')
        ax2.set_title(f'{symbol} Daily Returns')
        ax2.set_ylabel('Returns')
        ax2.legend()
        ax2.grid(True)
        
        # Plot Cumulative Returns on the third subplot
        ax3.plot(df['cumulative_returns'], label='Cumulative Returns', color='brown')
        ax3.set_title(f'{symbol} Cumulative Returns')
        ax3.set_xlabel('Date')
        ax3.set_ylabel('Cumulative Returns')
        ax3.legend()
        ax3.grid(True)
        
        # Show additional analysis in the console
        print(f"Analysis for {symbol}:")
        print(f"Average Daily Return: {avg_return:.4f}")
        print(f"Volatility (Standard Deviation of Returns): {volatility:.4f}")
        
        # Adjust layout and show plot
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Data for {symbol} not found. Please ensure the data is downloaded correctly.")

# Select a company to analyze
for i, company in enumerate(companies, 1):
    print(f"{i}. {company}")

choice = int(input("Enter the number of the company you want to analyze: ")) - 1
analyze_stock(companies[choice])
