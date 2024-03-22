from surmount.base_class import Strategy, TargetAllocation
from surmount.logging import log
from surmount.data import Asset, OHLCV
from surmount.execution import place_order, check_order_status, set_trailing_stop_loss

class TradingStrategy(Strategy):
    def __init__(self):
        # List all tickers you are considering for scanning.
        self.tickers = ["Example1", "Example2"]  # Add your tickers here
        self.data_list = [OHLCV(i) for i in self.tickers]

    @property
    def interval(self):
        # Select an appropriate interval for scanning.
        return "1day"

    @property
    def assets(self):
        return self.tickers

    @property
    def data(self):
        return self.data_list

    def run(self, data):
        for ticker in self.tickers:
            ohlcv_data = data["ohlcv"][-1][ticker]  # Assuming the last index contains the latest data point
            
            # Calculate the percentage change from open to close.
            percentage_change = ((ohlcv_data["close"] - ohlcv_data["open"]) / ohlcv_data["open"]) * 100
            
            # Check price range.
            if ohlcv_data["close"] >= 1.50 and ohlcv_data["close"] <= 20.50:
                
                # Assume `volume_check` and `float_check` are functions you defined to check for high volume and low float.
                # These definitions depend on your data source and aren't provided in the Surmount AI package, hence pseudocode.
                if volume_check(ticker) and float_check(ticker):
                    
                    # Assume `fetch_news` is a function that returns True if there's positive news. This might involve
                    # parsing news APIs or websites, which is beyond the scope of this script.
                    if percentage_change >= 10 and fetch_news(ticker):
                        
                        # Place an order for 100 shares of the stock.
                        order_id = place_order(ticker, quantity=100)
                        order_filled = False
                        
                        # Check if the order is filled, keep checking until it is filled.
                        # `check_order_status` is a stand-in for functionality to check orders which isn't in the base examples.
                        while not order_filled:
                            order_filled = check_order_status(order_id)
                            
                        # Once order is filled, set a trailing stop loss of 10%.
                        # `set_trailing_stop_loss` is pseudocode for setting a trailing stop loss, which isn't detailed in the examples.
                        if order_filled:
                            set_trailing_stop_loss(ticker, percentage=10)

        # The allocation is kept neutral here since actual trading actions are taken inside the loop.
        # This is more of an operational script rather than one deciding on allocation weights.
        return TargetAllocation({})