from common.handle_config import conf
import requests
import jsonpath

# 文件上传,获取图片地址
headers0 = {"X-Lemonban-Media-Type": "lemonban.v1"}
file0 = {"file": ("1.jpg", open(r"C:\Users\cy001\Desktop\1.jpg", "rb"), "image/jpg")}
response0 = requests.request(method="POST", url=conf.get("url", "public_url") + "/file/upload",
                             headers=headers0, files=file0)
res0 = response0.json()
image_url = jsonpath.jsonpath(res0, "$..data")[0]

# 登录获取用户id和token
headers1 = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
data1 = {"pwd": "sunday666", "userName": "sunday"}
response1 = requests.request(method="POST", url=conf.get("url", "public_url") + "/user/login",
                             headers=headers1, json=data1)
res1 = response1.json()
u_id = jsonpath.jsonpath(res1, "$..id")[0]
u_token = jsonpath.jsonpath(res1, "$.data..token")[0]


# 完善商户信息，成为代理商
headers2 = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json",
            "Authorization": "Bearer" + " " + u_token}
data2 = {"address": "上海市阳光街道",
         "establishDate": "2021-05-02",
         "legalPerson": "阳阳",
         "licenseCode": "xh430646asas46fa",
         "licenseUrl": "http://127.0.0.1/smarthome/aaa.jpg",
         "merchantName": "青海文梅科技有限公司",
         "merchantType": 2,
         "registerAuthority": "城中区派出所",
         "tel": "18888888888",
         "userId": 1,
         "validityDate": "2033-05-02"
         }

"""
{'code': '0', 'msg': '操作成功', 'data':
    {'token_info':
         {'token_type': 'Bearer',
          'expires_in': '2022-02-02 23:01:17',
          'token': 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiMTcwNjg0IiwiZXhwIjoxNjQzODE0MDc3fQ.ykkdcRrQrfirWK-RxSl3osVdXxaCy9UUf0oMhpthN5UHnr1z_-946WiUl8KfyxpArdlp_msOxXHXfin4LOwkNg'
          },
     'phone': '15180000000',
     'user_name': 'sunday',
     'id': 170684,
     'type': False}
 }
"""
