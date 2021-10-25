# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/20 13:32
@Author  : zhx
@FileName: setting.py
"""
import os

class Config:
    # 项目路径 os.path.dirname(path)	返回文件路径   os.path.abspath(path)	返回绝对路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path,"data\cases.xlsx")
    print(data_path)
    # print(data_path)

    # 测试用例路径   把目录和文件名合成一个路径
    cases_path = os.path.join(root_path,"test_cases")
    print(cases_path)

    # 测试报告路径
    report_path = os.path.join(root_path,"report")
    if not os.path.exists(report_path):
        os.mkdir(report_path)


class DevConfig(Config):

    # 项目的域名
    # host = "http://edcpmapi.ashermed.cn/"
    host = 'http://gcpmsapi.ashermed.cn/'



# config = DevConfig()

if __name__ == '__main__':
    Config()
