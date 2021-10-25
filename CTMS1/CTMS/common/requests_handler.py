# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/20 13:57
@Author  : zhx
@FileName: requests_handler.py
"""
import requests

class RequestsHandler:
    #
    # def __int__(self):
    #     self.session = requests.Session()
    #
    #
    # def visit(self, url, method, params=None, data=None,json=None,**kwargs):
    #     """   访问一个接口，使用get， post，put
    #           传data：data是python字典格式；传参data=json.dumps(data)是字符串类型传参
    #     :param url: 请求地址
    #     :param method: 请求方法   POST ， get
    #     :param params: params在get请求中使用，。
    #     :param data: data在post请求中使用
    #     :param json:  data、json在post请求中使用
    #     :param kwargs:
    #     :return:
    #     """
    #     res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
    #     try:
    #         return res.json()
    #     except ValueError:
    #         print("not json")

    def visit_2(self,method,url,param=None,data=None,json=None,header=None):
        data_method = (str(method)).upper()
        if data_method == 'GET':
            if json == None:
                res = requests.get(url=url,params=param,headers=header)
                return res.json()
            else:
                res = requests.get(url=url,json=json,headers=header)
                return res.json()
        elif data_method == 'POST':
            if json == None:
                res = requests.post(url=url,data=data,headers=header)
                return res.json()
            else:
                res = requests.post(url=url,json=json,headers=header)
                return res.json()
        else:
            print('输入有误')


#     def close_session(self):
#         self.session.close()
# # #
# # if __name__ == '__main__':
# #     print(RequestsHandler)
