import os
import unittest
import time

# 1,初始化 testloader
from config.setting import config
from libs.HTMLTestRunner import HTMLTestRunner

testloader = unittest.TestLoader()

# 加载所有测试用例
suite = testloader.discover(config.case_path)

ts = str(int(time.time()))
file_name = 'test_result_{}.html'.format(ts)
file_path = os.path.join(config.report_path,file_name)

# TODO：一定要以二进制的方式打开
with open(file_path,"wb") as f:
    runner = HTMLTestRunner(f, title="zhx",
                            description="haha",
                            )
    runner.run(suite)


