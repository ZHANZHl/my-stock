from model.Industry import Industry, EnergySecondaryIndustry


class Stock:
    def __init__(self, identity, current_price=0,
                 name="",
                 open_price=0, prev_close=0,
                 quote_change=0,
                 highest_price_year=0, lowest_price_year=0,
                 highest_price_last_day=0, lowest_price_last_day=0,
                 market_earnings_ttm=0, market_earnings_dynamic=0, market_earnings_static=0,
                 pbr=0,
                 sell=0, buy=0,
                 volume=0, turnover=0,
                 market_capitalization=0, total_equity=0,
                 circulation_market_value=0, trade_equity=0,
                 dividend_yield=0,
                 industry=Industry.Energy, second_industry=EnergySecondaryIndustry.EnergyEquipment
                 ):
        self.identity = identity
        self.current_price = current_price
        self.name = name
        self.open_price = open_price
        self.prev_close = prev_close
        self.quote_change = quote_change
        self.highest_price_year = highest_price_year
        self.lowest_price_year = lowest_price_year
        self.highest_price_last_day = highest_price_last_day
        self.lowest_price_last_day = lowest_price_last_day
        self.market_earnings_ttm = market_earnings_ttm
        self.market_earnings_dynamic = market_earnings_dynamic
        self.market_earnings_static = market_earnings_static
        self.pbr = pbr
        self.sell = sell
        self.buy = buy
        self.volume = volume
        self.turnover = turnover
        self.market_capitalization = market_capitalization
        self.total_equity = total_equity
        self.circulation_market_value = circulation_market_value
        self.trade_equity = trade_equity
        self.dividend_yield = dividend_yield
        self.industry = industry
        self.second_industry = second_industry

    def __str__(self):
        return "股票代码:" + self.identity + \
               "\n股票名称:" + self.name + \
               "\n当日价格:" + self.current_price + \
               "\n今开:" + self.open_price + \
               "\n昨收:" + self.prev_close + \
               "\n最高:" + self.highest_price_last_day + \
               "\n最低:" + self.lowest_price_last_day

    def to_json(self):
        """
        目前没找到序列化枚举值的好办法,所以忽略掉行业相关的序列化
        :return:
        """
        return {
            "identity": self.identity,
            "current_price": self.current_price,
            "name": self.name,
            "open_price": self.open_price,
            "prev_close": self.prev_close,
            "quote_change": self.quote_change,
            "highest_price_year": self.highest_price_year,
            "lowest_price_year": self.lowest_price_year,
            "highest_price_last_day": self.highest_price_last_day,
            "lowest_price_last_day": self.lowest_price_last_day,
            "market_earnings_ttm": self.market_earnings_ttm,
            "market_earnings_dynamic": self.market_earnings_dynamic,
            "market_earnings_static": self.market_earnings_static,
            "pbr": self.pbr,
            "sell": self.sell,
            "buy": self.buy,
            "volume": self.volume,
            "turnover": self.turnover,
            "market_capitalization": self.market_capitalization,
            "total_equity": self.total_equity,
            "circulation_market_value": self.circulation_market_value,
            "trade_equity": self.trade_equity,
            "dividend_yield": self.dividend_yield,
            # "industry": self.industry,
            # "second_industry": self.second_industry,
        }

    @staticmethod
    def from_json(stock):
        return Stock(stock["identity"],
                     stock["current_price"],
                     stock["name"],
                     stock["open_price"],
                     stock["prev_close"],
                     stock["quote_change"],
                     stock["highest_price_year"],
                     stock["lowest_price_year"],
                     stock["highest_price_last_day"],
                     stock["lowest_price_last_day"],
                     stock["market_earnings_ttm"],
                     stock["market_earnings_dynamic"],
                     stock["market_earnings_static"],
                     stock["pbr"],
                     stock["sell"],
                     stock["buy"],
                     stock["volume"],
                     stock["turnover"],
                     stock["market_capitalization"],
                     stock["total_equity"],
                     stock["circulation_market_value"],
                     stock["trade_equity"],
                     stock["dividend_yield"],
                     # stock["industry"],
                     # stock["second_industry"]
                     )
