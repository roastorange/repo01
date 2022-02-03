"""
============================
Author:柠檬班-木森
Time:2020/5/21   21:25
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
from common.base_page import BasePage
from locator.user_locator import UserLocator as loc


class UserPage(BasePage):

    def get_user_amount(self):
        """获取用户的余额"""
        ele = self.wait_element_visibility(loc.user_amount_ele,"用户页面_等待用户余额元素可见")
        amount = ele.text
        # amount = self.get_element_text(loc.user_amount_ele,'用户页面_获取余额')
        amount = amount.replace('元', '')
        return amount
