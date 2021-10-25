
# author:zhx   今天第4张   37节
#  ******
import requests

class RequestsHandler:

    def __init__(self):
        self.session = requests.Session()



    def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        """访问一个接口，你可以使用get请求，也可以使用post 请求，put ，delete
        请求方法： method：
        请求地址： url
        请求参数： params ，data ，json
        """
        # if method.lower()== 'get':
        #     res = self.session.get(url, params=params,  **kwargs)
        # elif method.lower == 'post':
        #     res = self.session.post(url, params=params,data =data, json=json, **kwargs)
        # else:
        #  可以处理请求方法
        res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json")

    def close_session(self):
        self.session.close()

# 保持测试用例的独立性
# req = RequestsHandler()
