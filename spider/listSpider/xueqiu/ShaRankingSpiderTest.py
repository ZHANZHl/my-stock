import unittest
import logging

from spider.listSpider.xueqiu.ShaRankingSpider import ShaRankingSpider

logger = logging.getLogger("ShaRankingSpiderTest")
logger.setLevel(level=logging.INFO)


class ShaRankingSpiderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.spider = ShaRankingSpider()

    def testIterator(self):
        length = 0
        for i in range(len(self.spider)):
            logger.debug(self.spider[i])
            length = length + 1
        self.assertEqual(length, len(self.spider))

    def testGenerator(self):
        length = 0
        for item in self.spider:
            logger.debug(item)
            length = length + 1
        self.assertEqual(length, len(self.spider))


if __name__ == '__main__':
    unittest.main()
