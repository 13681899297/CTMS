from asyncio import sleep

from selenium import webdriver


# 生成一个浏览器（webdriver对象）：反射机制
def brower(type_):
    # if type_ == 'Chrome':
    #     driver = webdriver.Chrome()
    try:
       driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Webkeys:
    # 为了补全
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self,type_):
        self.driver = brower(type_)
        self.driver.implicitly_wait(10)


    # 访问url
    def open(self,url):
        self.driver.get(url)

   # 退出
    def quit(self):
        self.driver.quit()



    # 元素定位
    def locator(self,name,value):
        return self.driver.find_element(name,value)

    # 输入
    def input(self,name,value,txt):
        self.locator(name,value).send_keys(txt)

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()

    # wenben 断言校验
    def assert_text(self,name,value,fact_text):
        assert self.locator(name,value).text == fact_text

    def wait(self,time_):
        sleep(time_)




