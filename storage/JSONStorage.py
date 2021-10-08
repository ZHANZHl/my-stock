import datetime
import json

from model.Stock import Stock
from model.DayStock import DayStock
from storage.BaseStorage import BaseStorage
from spider.JQKASpider import JQKASpider


class JSONStorage(BaseStorage):
    def __init__(self, path, spider_class=JQKASpider):
        super().__init__()
        # cache={
        #       identity:{
        #           something in stock
        #           date?:{
        #               something in day stock
        #               time?:{}
        #           }
        #       }
        # }
        self.cache = {}
        with open(path, "r") as f:
            self.cache = json.load(f)
        self.spider = spider_class()

    def get_stock(self, identity):
        if self.cache[identity]:
            cache_stock = self.cache[identity]
            return Stock.from_json(cache_stock)
        return self.spider.get_stock(identity)

    def get_day_stock(self, identity, date:datetime.datetime):
        date_key=date.strftime("%Y-%m-%d")
        if self.cache[identity] and self.cache[identity][date]:
            cache_day_stock=self.cache[identity][date]
            return DayStock.from_json(cache_day_stock)
