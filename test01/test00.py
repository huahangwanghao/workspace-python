import  requests
import pymysql
import json
from bs4 import  BeautifulSoup

print("hello world")

# -----------------------------------------------
class Person():
    # 定义构造方法
    def __init__(self,name):
        self.name=name
    # 定义一个自定义的函数
    def show(self):
        print(self.name)
    # 定义一个equal方法
    def __eq__(self, other):
        return self.name == other.name
    # toString()方法的实现  还用了一个占位符的方式去实现这个功能
    def __str__(self):
        return  "我的名字是%s"%self.name

p=Person("我是王浩11")
p.show()
p1=Person("我是王浩")
print(p==p1)
print(p)




