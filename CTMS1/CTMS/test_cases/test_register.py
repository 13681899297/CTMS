# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/20 17:50
@Author  : zhx
@FileName: test_register.py
"""
"""注册相关测试用例"""
import json
import unittest
import ddt

from common.excel_handler import ExcelHandler
from config.setting import Config,DevConfig
from common.requests_handler import RequestsHandler


@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(Config.data_path)
    # data = excel_handler.read('register')
    data = excel_handler.read('Sheet1')
    def setUp(self):
        self.req = RequestsHandler()
    #
    # def tearDown(self) -> None:
    #     self.req.close_session()

    @ddt.data(*data)
    def test_register(self,test_data):
        """用例描述"""
        # 访问接口，得到实际结果, 字符串？其实是字典
        print('用例执行的数据',test_data['url'],test_data['method'],test_data['js_data'],test_data['header'])
        res = self.req.visit_2(url=DevConfig.host + test_data['url'],
                             method = test_data['method'],
                             json = json.loads(test_data['js_data']),
                             header = json.loads(test_data['header'])
                             )

        print('res----',res)
        self.assertEqual(test_data['expected'],res['gatewayMessage'])


# if __name__ == '__main__':
#     unittest.main()




