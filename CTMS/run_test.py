#  ******
# author:zhx
# @Time:2020/12/4
# 收集测试用例
import os
import time
from unittestreport import TestRunner
import unittest

# 1，初始化测试用例
from config.setting import config

testloader = unittest.TestLoader()
# 2， 查找测试用例，加载
# 获取路径后拼接，出入路径名
dir_path = os.path.dirname(os.path.abspath(__file__))
# 后拼接，出入路径名
case_path = os.path.join(dir_path,'test_cases')
# 提供路径后默认匹配
suite = testloader.discover(config.case_path)
# print(suite)

# 获取report路径
report_path = os.path.join(dir_path,'report')
# 判断文件是否存在，不存在就创建
if not os.path.exists(report_path):
    os.mkdir(report_path)

ts = str(int(time.time()))

file_name = 'test_result_{}.html'.format(ts)
file_path = os.path.join(report_path,file_name)

with open(file_path,"wb") as f:
    runner = TestRunner(suite,
                             filename=file_name,
                             report_dir=r'D:/a_python/CTMS/report',
                             title='伦理系统',
                             tester='张',
                             desc="测试报告",
                             templates=2)
    runner.run()


