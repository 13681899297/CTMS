'''
    UnitTest测试框架应用：
        1. 类名继承unittest.TestCase
        2. 测试用例:所有的测试用例，都是以函数的形式存在，函数的名称必须以test开头
        3. 用例加载顺序：UnitTest中有默认的用例加载顺序：0-9，A-Z，a-z
        4. 所有的前置后置都有等级存在：class级别，method级别；潜质与后置函数有且只有一个
            method级别前置后置：
                与用例关联，每一条用例运行前会执行前置，运行后会执行后置
            class级别前置后置：
                1. 必须定义装饰器@classmethod
                2. 前置是在所有内容运行前运行一次，后置是所有内容运行结束后运行一次
        5. cls对象只在class级别前后置中进行定义，而调用则还是通过self进行调用
        6. 修改cls对象的值，在全局生效，需要通过类名.对象进行赋值操作才可以生效，而通过self.对象进行赋值只能够在当下函数中生效
'''
# 导入UnitTest模块
import unittest
from time import sleep

from selenium import webdriver


# 如何真正意义上应用UnitTest框架:必须在类名继承unittest.TestCase
class UnitDemo(unittest.TestCase):
    # class级别前置：比如说，所有的配置
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get('http://www.baidu.com')
    #     cls.title = None
    #     cls.DD = '虚竹是吴彦竹'
    #
    # # class级别后置
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     # 用例2的值
    #     print(cls.title)
    #     cls.driver.quit()

    # 前置条件：method级别
    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://www.baidu.com')

    # 后置条件:method级别
    # def tearDown(self) -> None:
    #     self.driver.quit()

    # 测试用例:所有的测试用例，都是以函数的形式存在，函数的名称必须以test开头
    # def test_search01(self):
    # input_ = self.driver.find_element_by_name('wd')
    # input_.clear()
    # input_.send_keys(self.DD)
    # button = self.driver.find_element_by_id('su')
    # button.click()
    # sleep(3)
    # # None
    # print(self.title)
    # # 修改cls.title的值，在全局生效。
    # UnitDemo.title = self.driver.title
    # print(self.title)
    # self.assertEqual('123','123',msg='断言失败')

    # def test_search02(self):
    #     input_ = self.driver.find_element_by_name('wd')
    #     input_.clear()
    #     input_.send_keys('迪丽热嫣')
    #     button = self.driver.find_element_by_id('su')
    #     button.click()
    #     sleep(3)
    #     # 用例1的值
    #     print(self.title)
    #     UnitDemo.title = self.driver.title
    #     print(self.title)

    # 普通函数:封装逻辑代码，以便于在测试用例中进行调用
    def test_login(self):
        print('这是login函数')
        # assert '123' == '1231','断言失败'
        self.assertEqual('123', '123', msg='断言失败')
        # 3.11111111111111111与3.11111111111111112
        # self.assertAlmostEqual(3.11, 3.12, msg='失败')
        # 当一个变量为空或者None或者False的时候，从布尔值的角度考虑都属于False
        # self.assertTrue(a, msg='失败')



# 要运行测试用例
if __name__ == '__main__':
    # UnitTest执行测试用例的行为
    unittest.main()
