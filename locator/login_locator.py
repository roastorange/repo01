"""
============================
Author:柠檬班-木森
Time:2020/5/19   20:24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium.webdriver.common.by import By


class LoginLocator:
    """登录页面的元素定位"""
    # 账号输入框
    mobile_loc = (By.XPATH, '//input[@placeholder="手机号"]')
    # 密码输入框
    pwd_loc = (By.XPATH, '//input[@placeholder="密码"]')
    # 点击按钮
    login_loc = (By.XPATH, "//button[text()='登录']")
    # 失败的提示内容
    error_info = (By.XPATH, "//div[@class='form-error-info']")
    # 失败的弹框
    alert_error_info = (By.XPATH, '//div[@class="layui-layer-content"]')
    # 记住手机号选框
    re_mobile = (By.XPATH, '//input[@name="remember_me"]')
