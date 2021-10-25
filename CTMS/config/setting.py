#  ******
# author:zhx
# @Time:2020/12/4

import os

class Config:

    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path,'data/cases.xlsx')

    # 测试用例路径
    case_path = os.path.join(root_path,'test_cases')

    # 测试报告路径
    report_path = os.path.join(root_path,'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)

class DevConfig(Config):

    # 项目的域名
    # host = 'http://120.78.128.25:8766/futureloan'
    host = 'http://gcpmsapi.ashermed.cn/'
    #  http://gcpmsapi.ashermed.cn/api/v1/Login/SingleSignOnByLoginId


config = DevConfig()

