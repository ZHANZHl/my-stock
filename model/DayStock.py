# 股票价格 (每日)
import datetime

DEFAULT_DATE = datetime.datetime.now()


class DayStock:
    def __init__(self, identity, date=DEFAULT_DATE, open_price=0, prev_close=0,
                 high=0, low=0,
                 chg=0, change=0,
                 volume=0,
                 big_sell=0, big_buy=0,
                 mid_sell=0, mid_buy=0,
                 small_sell=0, small_buy=0, ):
        self.identity = identity
        self.date = date
        self.open_price = open_price
        self.prev_close = prev_close
        self.high = high
        self.low = low
        self.chg = chg
        self.change = change
        self.volume = volume
        self.big_sell = big_sell
        self.mid_sell = mid_sell
        self.small_sell = small_sell
        self.big_buy = big_buy
        self.mid_buy = mid_buy
        self.small_buy = small_buy

    def __str__(self):
        return "股票代码:" + self.identity + \
               "\n今开:" + self.open_price + \
               "\n昨收:" + self.prev_close + \
               "\n最高:" + self.high + \
               "\n最低:" + self.low + \
               "\n涨跌幅:" + self.chg + \
               "\n涨跌额:" + self.change + \
               "\n成交量:" + self.volume + \
               "\n大单流入:" + self.big_buy + "\t大单流出:" + self.big_sell + \
               "\n中单流入:" + self.mid_buy + "\t中单流出:" + self.mid_sell + \
               "\n小单流入:" + self.small_buy + "\t小单流出:" + self.small_sell

    def to_json(self):
        return {
            "identity": self.identity,
            "date": self.date,
            "open_price": self.open_price,
            "prev_close": self.prev_close,
            "high": self.high,
            "low": self.low,
            "chg": self.chg,
            "change": self.change,
            "volume": self.volume,
            "big_sell": self.big_sell,
            "mid_sell": self.mid_sell,
            "small_sell": self.small_sell,
            "big_buy": self.big_buy,
            "mid_buy": self.mid_buy,
            "small_buy": self.small_buy,
        }

    @staticmethod
    def from_json(day_stock):
        return DayStock(day_stock["identity"],
                        day_stock["date"],
                        day_stock["open_price"],
                        day_stock["prev_close"],
                        day_stock["high"],
                        day_stock["low"],
                        day_stock["chg"],
                        day_stock["change"],
                        day_stock["volume"],
                        day_stock["big_sell"],
                        day_stock["big_buy"],
                        day_stock["mid_sell"],
                        day_stock["mid_buy"],
                        day_stock["small_sell"],
                        day_stock["small_buy"], )
