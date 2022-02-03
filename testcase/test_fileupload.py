import jsonpath
import pytest
import requests

from common.handle_config import conf
from data.case_data import FileUpload
from common.handle_logging import log


class TestFileUpload:
    @pytest.mark.parametrize("case_data", FileUpload.case_data)
    def test_file_upload(self, case_data):
        method = "POST"
        url = conf.get("url", "public_url") + "/file/upload"
        headers = {"X-Lemonban-Media-Type": "lemonban.v1"}
        data = case_data["case_data"]
        expected = case_data["expected"]
        response = requests.request(method=method, url=url, headers=headers, files=data)
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
