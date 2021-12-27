class BaseListSpider:
    """
    获取一个列表(比如排行榜)上的信息
    """
    def __getitem__(self, item):
        """
        获取对应位置的特征 比如股票id 或者用户id
        :param item: 位置
        :return: 特征
        """
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __len__(self):
        pass
