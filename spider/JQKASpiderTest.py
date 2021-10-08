import datetime
import unittest
from JQKASpider import JQKASpider
from model.exception.NotTradeException import NotTradeException


class JQKASpiderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.spider = JQKASpider()

    def testResponse(self):
        res = self.spider.get_stock("600165")

    def testDailyResponse(self):
        # res=self.spider.get_day_stock()
        target_date = datetime.datetime.strptime("2021-1-5", "%Y-%m-%d")
        try:
            res = self.spider.get_day_stock("600165", date=target_date)
            print(res)
        except NotTradeException:
            print("当日未交易")
