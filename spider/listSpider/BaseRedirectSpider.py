from spider.listSpider.BaseListSpider import BaseListSpider


class BaseRedirectSpider(BaseListSpider):
    """
    用于处理需要跳转的情况

    比如从一个用户收益排行榜上,需要先找到对应的用户,才能找到他操作的股票
    """

    def redirect(self, index):
        """
        进行一次跳转

        :param index: 将要跳转到第几个
        :return: 返回下一层BaseRedirectSpider的实例
        """
        pass
