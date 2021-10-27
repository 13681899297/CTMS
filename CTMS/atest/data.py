# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/26 15:40
@Author  : zhx
@FileName: shuju.py
"""
from atest.encapsulation  import Webkeys

wk = Webkeys('Chrome')
wk.open("url")
wk.click('link text','登录')
wk.input('name','accounts','xuzhu666')
wk.input('name','pwd','123456')
wk.click('xpath','xpath')
wk.wait(3)
wk.quit()
