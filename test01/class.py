import  requests
import pymysql
import json
from bs4 import  BeautifulSoup

class Person():

    name="wanghao"
    age=123
    # 私有化的一个属性
    __id=19900103
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id
    #初始化
    def __init__(self):
        self.name="初始化"
        self.age=23
    # toString 方法
    def __str__(self):
        return ("我的名字是%s,我的年龄是%d" %(self.name,self.age))


class Student(Person):
    def show(self):
        print("我要展示我的名字年龄")
    def add(self,a,b):
        return a+b

p=Person()
p.setId(34)
#print(p.getId())
s=Student()
s.name="学生"
s.age=90
print(s.add(1,2))