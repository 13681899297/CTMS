'''
    网页弹窗：
        传统的弹窗交互形式：
            1. 确定弹窗 alert
            2. 确定、取消弹窗 confirm
            3. 输入文本，确定、取消弹窗 prompt文本窗
        这种弹窗的形式基本已经没有了。因为交互太老旧
        移动端叫做toast
        特殊弹窗（通知，不属于弹窗）：这一类型的内容，需要通过修改chrome属性来实现操作
            1. 记住密码和更新密码
            2. 禁用启用权限设置
            3. 弹窗允许与否
'''
from selenium import webdriver

driver = webdriver.Chrome()
# 切换到弹窗本体
web_alert = driver.switch_to.alert
# 确认弹窗
web_alert.accept()
# 取消弹窗
web_alert.dismiss()
# 输入文本
web_alert.send_keys('')
# 获取文本
text = web_alert.text
