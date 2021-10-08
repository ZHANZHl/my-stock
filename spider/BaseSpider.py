"""
这是所有爬虫的基类,
应当只抽象接口而不具备任何实现
"""
import string


class BaseSpider:
    def __init__(self):
        pass

    def get_stock(self, identity: string):
        """
        应该根据给定的股票代码返回对应的stock实例 即对应股票的基本信息

        :param identity: 股票代码
        :return:
        """
        pass

    def get_day_stock(self, date, identity):
        """
        返回指定日期对应股票的数据

        :param date: 日期
        :param identity: 股票代码
        :return:
        """
        pass
