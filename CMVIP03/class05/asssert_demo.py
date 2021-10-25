'''
    断言机制：
        断言的使用不仅仅只是driver.title,断言一定是选择有指定意义的内容来进行断言。
        断言的对象可以是元素，可以是属性，可以是文本，可以是任何东西。只要是特定的即可。
        一般常用的断言就是通过text来进行，除此之外，如果需要流程继续执行，可以考虑用显式等待。
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://39.98.138.157/shopxo/')
# driver.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
# driver.find_element_by_name('accounts').send_keys('666666')
# driver.find_element_by_name('pwd').send_keys('111111')
# driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()

# text = driver.find_element_by_xpath(
#     '/html/body/div[6]/div/div[1]/div[1]/em/span/em[2]').text
#
# print(text)
# # 预期结果
# assert_text = '6666661'
# # 断言机制：预期结果与实际结果对比
# assert assert_text == driver.find_element_by_xpath(
#     '/html/body/div[6]/div/div[1]/div[1]/em/span/em[2]').text, '断言失败'

'''
断言的核心原理：
    if assert_text == driver.find_element_by_xpath(
    '/html/body/div[6]/div/div[1]/div[1]/em/span/em[2]').text:
        pass
    else:
        return AssertionError
'''

'''
    JS执行器：
        Document对象的应用：Document对象是JS中的一个模块
            1. 用于获取元素信息或者修改元素属性，以便于在实际自动化时可以更为便捷地执行操作
            2. 因为selenium本身是基于js来实现的。但是在实际web中，有一些特定的情况是通过selenium很难实现，就需要通过js去注入脚本
            3. JS执行器配合document对象，一般是用于自动化中的疑难杂症来进行处理的。
            4. 如果你需要通过js执行器来操作获取元素或者获取信息，进行赋值，就需要添加return
'''
# 通过Selenium获取元素属性
# el = driver.find_element_by_xpath('//*[@id="ai-topsearch"]')
# value = el.get_attribute('class')
# print(value)
# 通过Document对象来修改元素属性
js = "document.getElementById('ai-topsearch').setAttribute('value','asd')"
# 执行js语句函数：js执行器
driver.execute_script(js)
# 如何有效地运行js语句
el = driver.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/a[1]')
# 占位符的应用
js = "arguments[0].innerHTML"
# 灵活版js执行器操作：通过传递元素参数，来快速实现元素的识别与操作
driver.execute_script(js, el)
# 滚动条操作，一般都是在特定需要操作滚动条时应用即可。
# document.scrollingElement.scrollTop表示上下滚动，0-2000区间
# window.scrollTo(x,y) 左右滚动
# el = driver.find_element_by_xpath('/html/body/footer/div[1]/ul[1]/li[4]/div/p[5]/a')
# js = "arguments[0].scrollIntoView()"
# driver.execute_script(js, el)
