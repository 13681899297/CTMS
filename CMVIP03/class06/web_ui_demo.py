'''
    1. 从注册到用户信息的修改
    2. 从登陆到商品添加购物车
    PS: 在定位元素过程中，如果出现一闪即逝的元素需要定位，可以先启动chrome开发者工具——Source
        然后运行浏览器流程，需要抓取元素时，通过F8让页面暂停
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from class06.chrome_options import Options

driver = webdriver.Chrome(options=Options().options_conf())
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/')
# 实现注册操作
# driver.find_element_by_link_text('注册').click()
# driver.find_element_by_name('accounts').send_keys('xuzhu666')
# driver.find_element_by_name('pwd').send_keys('123456')
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/label').click()
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[4]/button').click()
# WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element_by_link_text('退出'), message='登陆失败')

# 实现登录操作
driver.find_element_by_link_text('登录').click()
driver.find_element_by_name('accounts').send_keys('xuzhu666')
driver.find_element_by_name('pwd').send_keys('123456')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element_by_link_text('退出'), message='登陆失败')

# 个人信息修改：文件上传时，需要有一个小的上传时间，通过强制等待，让元素可以正常被操作
driver.find_element_by_link_text('个人中心').click()
driver.find_element_by_link_text('修改头像').click()
driver.find_element_by_name('file').send_keys(r'D:\头像\1.jpg')
sleep(2)
driver.find_element_by_xpath('//*[@id="user-avatar-popup"]/div/div[2]/form/button').click()
# 截图：需要先创建路径，再进行截图
WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element_by_xpath('//*[@id="common-prompt"]/p'),
                                    message='登陆失败')
driver.save_screenshot('./img/test02.png')
sleep(3)
driver.quit()
