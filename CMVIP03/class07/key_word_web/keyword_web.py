'''
    web端的关键字驱动类：
        结构中属于逻辑代码层，主要的目的是作为一个工具类的角色，在需要用到这些工具时，通过这个类来实现
        大型超市——自家工具箱——动用工具
        Selenium——关键字——web自动化
        工具箱一般包含有需要的常规操作行为：
            输入、点击、启动、、、、、、
        单独的工具类的存在是没有意义的，一定需要关联到实际应用，才能够产生价值
'''

# 开始去超市购物
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

'''
    getattr(class,name)()函数，从class对象中获取名称为name的成员属性
    如果要获取class对象的函数，则需要在末尾添加一个()
    getattr(webdriver,'Chrome') = webdriver.Chrome
    getattr(webdriver,'Chrome')() = webdriver.Chrome()
    如果传入的type_不是被允许的或错误的格式，那么browser函数会报错
'''


# 生成一个浏览器（webdriver对象）:反射机制
def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


# 定义工具类
class WebKeys:
    # 定义driver
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, type_):
        self.driver = browser(type_)
        self.driver.implicitly_wait(10)

    # 访问URL:wk.open(**args)
    def open(self, **kwargs):
        self.driver.get(kwargs['txt'])

    # 退出
    def quit(self, **kwargs):
        self.driver.quit()

    # 元素定位
    def locator(self, **kwargs):
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    # 输入
    def input(self, **kwargs):
        el = self.locator(**kwargs)
        el.clear()
        el.send_keys(kwargs['txt'])

    # 点击
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 文本断言校验
    def assert_text(self, **kwargs):
        try:
            assert self.locator(**kwargs).text == kwargs['expect']
            return True
        except:
            return False

    # 强制等待
    def wait(self, **kwargs):
        sleep(kwargs['txt'])

    # 显示等待：等待到了就返回元素，等待失败就返回一个超时的异常
    def assert_wait(self, **kwargs):
        try:
            # log
            el = WebDriverWait(self.driver, kwargs['txt'], 0.5).until(
                lambda el: self.locator(**kwargs))
            # print(el)
            return el
        except:
            # log
            # print(el)
            return False

    # 切换句柄：关闭标签页，再切换
    def switch_with_close(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 切换句柄：不关闭标签页，直接切换模式
    def switch_no_close(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 切换旧窗体
    def switch_to_old(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    # 获取元素属性,进行断言
    def assert_att(self, **kwargs):
        att = self.locator(**kwargs).get_attribute(kwargs['txt'])
        try:
            # log
            # print(type(att))
            # print(type(str(kwargs['expect'])))
            assert att == str(kwargs['expect'])
            # print(att)
            return True
        except:
            # print(att)
            # log
            return False
