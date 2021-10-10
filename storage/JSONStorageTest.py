import datetime
import unittest

from JSONStorage import JSONStorage


class JSONStorageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.storage = JSONStorage("../data.json")

    def test_get_stock(self):
        print(self.storage.get_stock("600165"))

    def test_get_day_stock(self):
        print(self.storage.get_day_stock("600165", datetime.datetime.now()))
