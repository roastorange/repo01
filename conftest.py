"""
============================
Author:柠檬班-木森
Time:2020/5/23   11:38
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium import webdriver
from selenium.webdriver import Chrome

import pytest

from common.handle_config import conf
from common.handle_logging import log
from page.page_index import IndexPage
from page.page_invest import InvestPage
from page.page_login import LoginPage
from page.page_user import UserPage


@pytest.fixture(scope='class')
def invest_fixture():
    """添加小区功能的前置后置"""


@pytest.fixture(scope='class')
def login_fixture():
    """登录功能的前置后置"""
    # 前置条件
    log.info("开始执行登录的用例")
    driver = Chrome(options=get_option())
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page
    # 后置条件
    driver.quit()
    log.info("登录的用例执行完毕")


def get_option():
    if conf.getboolean('env', "headless"):
        """设置浏览启动的选项：无头模式"""
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        return opt
    else:
        return None
