"""
============================
Author:柠檬班-木森
Time:2020/5/12   21:36
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os
import pytest

pytest.main(['--alluredir=allure_report'])
os.system('allure serve allure_report')
