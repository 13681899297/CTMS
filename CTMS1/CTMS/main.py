# from ddt import ddt, unpack, data
# import unittest
# import json
#
# a = [1, 2]
# b = [[4, 5], [6, 7]]
# c = "now_value"
# d = [{"name": "小明", "age": 28}, {"name": "大红", "age": 18}]
# e = [{"code": 1, "data": {"token": "123456", "name": "大白"}, "mes": ""}]
#
#
# @ddt
# class Test(unittest.TestCase):
#     def setUp(self):
#          print("执行开始--------")
#
#     def tearDown(self):
#         print("--------执行结束")
#
#     #  以逗号为分割点，分别打印1和2
#     @data(*a)
#     def Test01(self, se):
#         print(se)
# import unittest,os
# from ddt import ddt,data,unpack,file_data
# '''※字典的读取比较特殊，因为在拆分的时候，形参和实参的key值要一致，否则就报错※'''
# '''NO.1单组数据'''
# @ddt
# class Testwork(unittest.TestCase):
#
#     @data({'name':'lili','age':'16'},{'sex':'female','job':'nurser'})
#     # @unpack
#     def test_01(self,a):
#         print(a)
#
# if __name__ == '__main__':
#     unittest.main()
import random

import requests
from requests import request

def re(**kwargs):
    with request(**kwargs) as rs:
        print(rs.text)
        return rs.json()

ClientId = "123456"

def login():
    log = {
        "method": "POST",
        "url": "http://edcpmapi.ashermed.cn/Login/UserLogin",
        "data": {"loginName": "18917407729","password":"407729",
                 "usepwd":"1","clientId": ClientId,
                 "clientType":"1"}
    }
    return re(**log)["Data"]["token"]
    # return request(**log).json()["Data"]["token"]


# token = login()
# print(token)

