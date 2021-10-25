# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/20 17:50
@Author  : zhx
@FileName: test_register.py
"""
from common.requests_handler import RequestsHandler

"""注册相关测试用例"""
import json
import unittest
import ddt

from common.excel_handler import ExcelHandler
from config.setting import config




@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    def setUp(self):
        self.req = RequestsHandler()

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_register(self,test_data):
        """用例描述"""
        print(test_data)
        # 访问接口，得到实际结果, 字符串？其实是字典
        res = self.req.visit(config.host + test_data['url'],
                             test_data['method'],
                             json = json.loads(test_data['json']),
                             headers = json.loads(test_data['headers'])
                             )

        print('res----',res)
        print(config.host + test_data['url'])
        print(test_data['method'])
        self.assertEqual(test_data['expected'],res['gatewayMessage'])


if __name__ == '__main__':
    unittest.main()




