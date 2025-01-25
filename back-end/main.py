import pandas as pd
import os

class BacktestingEngine():
    def __init__(self, strategy, market_data, start_date, end_date, timeframe, initial_capital, slippage, commission, asset, leverage):
        self.strategy = strategy
        self.market_data = market_data
        self.start_date = start_date
        self.end_date = end_date
        self.timeframe = timeframe
        self.initial_capital = initial_capital
        self.slippage = slippage
        self.commission = commission
        self.asset = asset
        self.leverage = leverage


class MarketData():
    def __init__(self, data_source, file_path=None, api_url=None, api_key=None):
        data = {
            "timestamp":[],
            "open":[],
            "high":[],
            "low":[],
            "close":[],
            "volume":[]
        }
        self.dataFrame = pd.DataFrame(self.data)
        if data_source == 'FILE':
            self.load_from_file(file_path)
        elif data_source == 'API':
            self.load_from_api()

    def load_from_file(self, file_path):
        if not file_path.endswith('.csv'):
            raise ValueError("File must be a CSV file")
        elif not os.path.exists(file_path):
            raise ValueError("File does not exist")
        else:
            data = pd.read_csv(file_path)
            if not set(self.dataFrame.columns).issubset(set(data.columns)):
                raise ValueError(f"CSV file must contain the following columns: {', '.join(self.dataFrame.columns)}")
            self.dataFrame = data[self.dataFrame.columns]

    # TODO Add loading from API
    def load_from_api(self):
        raise NotImplementedError


class Strategy():
    def __init__(self):
        pass

if __name__ == "__main__":
    print("Execute")
    


