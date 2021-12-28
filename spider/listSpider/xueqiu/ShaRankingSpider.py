import requests
import json
from spider.listSpider.BaseListSpider import BaseListSpider

max_length = 5
url = "https://xueqiu.com/service/v5/stock/screener/quote/list?order=desc&order_by=percent&exchange=CN&market=CN" \
      "&type=sha&size=" + str(max_length)


class ShaRankingSpider(BaseListSpider):
    def __init__(self):
        self.rank = []
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        })
        if response.status_code == 200:
            content = json.loads(response.text)
            try:
                self.rank = content["data"]["list"]
            except:
                pass

    def __getitem__(self, index):
        return self.rank[index]

    def __len__(self):
        return len(self.rank)

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i = self.i + 1
        if self.i < len(self):
            return self[self.i]
        else:
            raise StopIteration()
