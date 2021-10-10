import datetime
import random
import re
import string
import sys

from selenium import webdriver
from selenium.webdriver import ActionChains

from spider.BaseSpider import BaseSpider
from model.Stock import Stock
from model.DayStock import DayStock
from model.exception.NotTradeException import NotTradeException
from utils.SeleniumUtils import wheel_element

driver = webdriver.Chrome()

url = "http://stockpage.10jqka.com.cn/"


def auto_adjust_position(convert_to_datetime, target_date_time=datetime.datetime.now()):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_css_selector("#hqzs > div > iframe"))
    canvas_element = driver.find_element_by_xpath('//*[@id="hxc3_cross_testcanvas"]')
    # 使显示日期的元素存在,使视图缩放到最小并获取element
    ActionChains(driver).move_to_element_with_offset(canvas_element, 85, 73).perform()
    wheel_element(canvas_element, 680)
    date_or_time_element = driver.find_element_by_xpath('//*[@id="testcanvas"]/div[8]')

    # 1. 首先确保目标日期在这个canvas表示的范围之内,因为首先出现的就是最新的,所以只考虑目标日期在左边的情况
    ActionChains(driver).move_to_element_with_offset(canvas_element, 2, 37).perform()
    start_date_time = convert_to_datetime(date_or_time_element.text)
    drag_actions = ActionChains(driver) \
        .move_to_element_with_offset(canvas_element, 2, 36) \
        .click_and_hold() \
        .move_to_element_with_offset(canvas_element, 560, 48) \
        .release() \
        .move_to_element_with_offset(canvas_element, 2, 38)
    while target_date_time < start_date_time:
        drag_actions.perform()
        start_date_time = convert_to_datetime(date_or_time_element.text)
    # 2. 二分查找目标日期
    left_position, right_position = 0, 564
    while left_position < right_position:
        mid_position = (left_position + right_position) // 2
        ActionChains(driver).move_to_element_with_offset(canvas_element, mid_position,
                                                         random.randint(10, 50)).perform()
        current_date = convert_to_datetime(date_or_time_element.text)
        if current_date < target_date_time:
            left_position = mid_position + 1
        else:
            right_position = mid_position
    ActionChains(driver).move_to_element_with_offset(canvas_element, left_position,
                                                     random.randint(10, 50)).perform()
    current_date = convert_to_datetime(date_or_time_element.text)
    if current_date != target_date_time:
        raise NotTradeException
    return


class JQKASpider(BaseSpider):
    def __init__(self):
        super().__init__()

    def get_stock(self, identity: string):
        stock = Stock(identity=identity)
        driver.implicitly_wait(3)
        driver.get(url + identity)
        # main frame
        element_name = driver.find_element_by_css_selector("#stockNamePlace")
        stock.name = element_name.get_attribute("stockname")
        # header frame
        driver.switch_to.frame(driver.find_element_by_css_selector("#in_squote > div > div > iframe"))
        element_price = driver.find_element_by_css_selector("#hexm_curPrice")
        stock.current_price = element_price.text

        element_open = driver.find_element_by_css_selector("#topenprice")
        stock.open_price = element_open.text

        element_prev_close = driver.find_element_by_css_selector("#pprice")
        stock.prev_close = element_prev_close.text

        element_last_day_high_price = driver.find_element_by_css_selector("#thighprice")
        stock.highest_price_last_day = element_last_day_high_price.text

        element_last_day_low_price = driver.find_element_by_css_selector("#tlowprice")
        stock.lowest_price_last_day = element_last_day_low_price.text

        element_volume = driver.find_element_by_css_selector("#tamount")
        volume = element_volume.text
        if volume[-1] == "万":
            volume = float(volume[:-1]) // 10000
        stock.volume = volume
        driver.close()
        return stock

    def get_day_stock(self, identity, date):
        stock = DayStock(identity, date)
        driver.implicitly_wait(3)
        driver.get(url + identity)
        driver.switch_to.frame(driver.find_element_by_css_selector("#hqzs > div > iframe"))
        day_element = driver.find_element_by_css_selector("body > ul > li:nth-child(2) > a")
        day_element.click()
        try:
            auto_adjust_position(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"), date)

            stock.open_price = driver.find_element_by_xpath('//*[@id="testcanvas"]/div[4]/span[1]').text
            stock.prev_close = driver.find_element_by_xpath('//*[@id="testcanvas"]/div[4]/span[4]').text
            stock.high = driver.find_element_by_xpath('//*[@id="testcanvas"]/div[4]/span[2]').text
            stock.low = driver.find_element_by_xpath('//*[@id="testcanvas"]/div[4]/span[3]').text
            stock.change = driver.find_element_by_xpath('//*[@id="testcanvas"]/div[4]/span[5]').text
            stock.chg = driver.find_element_by_xpath('//*[@id="testcanvas"]/div[4]/span[6]').text

            stock.volume = driver.find_element_by_xpath('//*[@id="testcanvas"]/div[6]').text
            volume_re = re.compile("成交量 量(.*)万")
            stock.volume = volume_re.findall(stock.volume)[0]

            driver.switch_to.default_content()
            stock.big_buy = driver.find_element_by_xpath('//*[@id="gegugp_zjjp"]/table/tbody/tr[1]/td[2]').text
            stock.big_sell = driver.find_element_by_xpath('//*[@id="gegugp_zjjp"]/table/tbody/tr[1]/td[3]').text
            stock.mid_buy = driver.find_element_by_xpath('//*[@id="gegugp_zjjp"]/table/tbody/tr[2]/td[2]').text
            stock.mid_sell = driver.find_element_by_xpath('//*[@id="gegugp_zjjp"]/table/tbody/tr[2]/td[3]').text
            stock.small_buy = driver.find_element_by_xpath('//*[@id="gegugp_zjjp"]/table/tbody/tr[3]/td[2]').text
            stock.small_sell = driver.find_element_by_xpath('//*[@id="gegugp_zjjp"]/table/tbody/tr[3]/td[3]').text
        finally:
            driver.close()
        return stock
