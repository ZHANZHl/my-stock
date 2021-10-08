"""
这个类是所有storage的基类
这个层面负责处理数据的提供 比如当天价格 股票数据等
如果不能从本地获得 则通过爬虫获取 即至少要有两个构造参数
怎么从本地获取数据 爬虫是哪个?
因为这个层面只是在爬虫的层面加上本地存储而已,所以应当保持接口一致
"""


class BaseStorage(object):
    def __init__(self):
        pass

    def get_stock(self, identity):
        """

        :param identity: 股票id
        :return: 股票基本面
        """
        pass

    def get_day_stock(self, identity, date):
        """

        :param identity: 股票id
        :param date: 日期
        :return:
        """
        pass
