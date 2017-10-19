import  requests
import pymysql
import time
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

# ---请求www.baidu.com
res=requests.get("http://www.baidu.com")
res.encoding="utf-8"
print(res.text)
soup=BeautifulSoup(res.text,"html.parser")
print(soup.select("a"))


try:
    # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn = pymysql.connect(host='59.110.215.202', user='root', passwd='wanghao', db='app_cms', port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    cur.execute('select * from t_a')
    data = cur.fetchall()
    for d in data:
        # 注意int类型需要使用str函数转义
        #print("ID: " + d[0] + '  用户名： ' + d[1] + "  注册时间： " + d[2])
        # 字符串的拼接
        print("id is %s name is %s  age is %s"   % (d[0],d[1],d[2]))
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
except Exception as e :
    print(e.args)



list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
all=zip(list1,list2,list3)
for a,b,c in all:
    print(a,b,c)



urls=["{}".format(str(i)) for i in range(10,100,10)]
for url in urls:
    time.sleep(2)
    print(url)