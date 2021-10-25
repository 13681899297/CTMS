# 拿出工具箱
from class07.key_word_web.keyword_web import WebKeys

# 实例化类对象
wk = WebKeys('Chrome')
wk.open('http://39.98.138.157/shopxo/')
wk.click('link text', '登录')
wk.input('name', 'accounts', 'xuzhu666')
wk.input('name', 'pwd', '123456')
wk.click('xpath', '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
wk.wait(3)
wk.quit()
