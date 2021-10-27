# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/26 16:24
@Author  : zhx
@FileName: 11.py
"""

class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat函数-实例化后需要被调用----")

    def ini(self):
        print("name",(self.name))
tom = cat("1猫",12)
tom.eat()
tom.ini()


class cat2:

    def test(self,name):
        print("下面是test方法的返回结果")
        return 1

    def test2(self,name1,age):
        print("test2有两个参数，下面是test2的返回结果")
        """方法内代码逻辑，然后各种运算，调用方法时返回最终结果进行使用"""
        """类的使用：1、先实例化类
                   2、然后根据-类名.方法名-对（方法）进行传参；
                   3、传参成功后得到方法的返回结果  return 2
        """
        return 2

a = cat2()
print(a.test("姓名"))
print("----22")
"""打印的是：test2有两个参数，下面是test2的返回结果  和  2
  a.test2('函数2',2)--调用函数，print输出函数的返回值
"""
print(a.test2('函数2',2))
print("----")
"""打印的是：test2有两个参数，下面是test2的返回结果
因为：只是调用函数，打印出的是函数内的内容，不打印函数的返回值；因为没有打印
"""
a.test2('函数2',2)

