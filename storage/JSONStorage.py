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
        self.path = path
        with open(path, "r") as f:
            self.cache = json.load(f)
        self.spider = spider_class()

    def get_stock(self, identity):
        if identity in self.cache:
            cache_stock = self.cache[identity]
            return Stock.from_json(cache_stock)
        stock = self.spider.get_stock(identity)
        self.cache[identity] = stock.to_json()
        return stock

    def get_day_stock(self, identity, date: datetime.datetime):
        date_key = date.strftime("%Y-%m-%d")
        if identity not in self.cache:
            self.cache[identity] = {}
        if date_key in self.cache[identity]:
            cache_day_stock = self.cache[identity][date_key]
            return DayStock.from_json(cache_day_stock)
        day_stock = self.spider.get_day_stock(identity, date)
        self.cache[date_key] = day_stock.to_json()
        return day_stock

    def save(self):
        """

        保存json文件为最新的数据
        为什么cache不存对象
        因为这里怎么从对象转为json我没想好怎么写
        所以保存的是json数据,需要的话返回对象
        :return:
        """
        with open(self.path, "w") as f:
            json.dump(self.cache, f)

    def __del__(self):
        self.save()
