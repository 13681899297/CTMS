
import os
import time
from unittestreport import TestRunner
import unittest
import HTMLTestRunner

# 1，初始化测试用例
from config.setting import Config

testloader = unittest.defaultTestLoader
# 2， 查找测试用例，加载
# 获取路径后拼接，出入路径名
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)
# 后拼接，出入路径名
# case_path = os.path.join(dir_path,'test_cases')
# # 提供路径后默认匹配
# suite = testloader.discover(config.case_path)
# 后拼接，出入路径名
case_path = os.path.join(dir_path, 'test_cases')
print(case_path)
# 提供路径后默认匹配
# suite = testloader.discover(config.cases_path)
suite = testloader.discover(case_path)

# 获取report路径
report_path = os.path.join(dir_path,'report')
# 判断文件是否存在，不存在就创建   os.path.exists(path)	路径存在则返回True,路径损坏返回False
if not os.path.exists(report_path):
    # os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
    # 如果目录有多级，则创建最后一级，如果最后一级目录的上级目录有不存在的，则会抛出一个 OSError。
    os.mkdir(report_path)

ts = str(int(time.time()))

file_name = 'test_result_{}.html'.format(ts)
file_path = os.path.join(report_path,file_name)

# with open(file_path,"wb") as f:
runner = TestRunner(suite,
                         filename=file_name,
                         report_dir=r'./report',
                         title='伦理系统',
                         tester='张',
                         desc="测试报告",
                         templates=2)
runner.run()


