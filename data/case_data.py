from common.handle_path import DATA_DIR
import os


class FileUpload:
    """文件上传用例数据"""
    case_data = [{"case_id": 1, "case_title": "100KB以下jpg格式", "case_data":
                    {"file": ("1.jpg", open(os.path.join(DATA_DIR, "1.jpg"), "rb"), "image/jpg")},
                  "expected": {"code": "0", "msg": "操作成功"}},
                 {"case_id": 2, "case_title": "100KB以下png格式", "case_data":
                     {"file": ("2.png", open(os.path.join(DATA_DIR, "2.PNG"), "rb"), "image/png")},
                  "expected": {"code": "0", "msg": "操作成功"}},
                 {"case_id": 3, "case_title": "100KB以上jpg格式", "case_data":
                     {"file": ("3.jpg", open(os.path.join(DATA_DIR, "3.jpg"), "rb"), "image/jpg")},
                  "expected": {"code": "1005", "msg": "文件超过限制大小100KB"}}
                 ]


class Login:
    """登录用例数据"""
    case_data = [{"case_id": 1, "case_title": "正常登录", "case_data": {"userName": "sunday", "pwd": "sunday666"},
                  "expected": {"code": "0", "msg": "操作成功"}},
                 {"case_id": 2, "case_title": "登陆失败-用户名错误", "case_data": {"userName": "sunDay", "pwd": "sunday666"},
                  "expected": {"code": "1001", "msg": "用户名或密码错误！"}},
                 {"case_id": 3, "case_title": "登陆失败-密码错误", "case_data": {"userName": "sunday", "pwd": "sunDay666"},
                  "expected": {"code": "1001", "msg": "用户名或密码错误！"}},
                 {"case_id": 4, "case_title": "登陆失败-用户名为空", "case_data": {"userName": "", "pwd": "sunday666"},
                  "expected": {"code": "1001", "msg": "用户名或密码错误！"}},
                 {"case_id": 5, "case_title": "登陆失败-密码为空", "case_data": {"userName": "sunday", "pwd": ""},
                  "expected": {"code": "1001", "msg": "用户名或密码错误！"}},
                 {"case_id": 6, "case_title": "登陆失败-用户名、密码为空", "case_data": {"userName": "", "pwd": ""},
                  "expected": {"code": "1001", "msg": "用户名或密码错误！"}}
                 ]
