import jsonpath
import pytest
import requests

from data.case_data import Login
from common.handle_config import conf
from common.handle_logging import log


class TestLogin:

    @pytest.mark.parametrize("case_data", Login.case_data)
    def test_login(self, case_data):
        method = "POST"
        url = conf.get("url", "public_url") + "/user/login"
        headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
        data = case_data["case_data"]
        expected = case_data["expected"]
        response = requests.request(method=method, url=url, headers=headers, json=data)
        res = response.json()
        try:
            assert jsonpath.jsonpath(res, "$..code")[0] == expected["code"]
            assert jsonpath.jsonpath(res, "$..msg")[0] == expected["msg"]
        except AssertionError as e:
            log.error("用例--{}--执行未通过".format(case_data["case_title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行通过".format(case_data["case_title"]))
