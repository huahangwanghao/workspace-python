# coding:utf-8
import pandas as pd
# 对于csv文件 不能使用重命名的格式来, 应该是用  另存为的方式 这样才可以打开
brics=pd.read_csv("D:\\workspace-python\\1.csv",index_col=0,encoding='gbk')
#添加新的列
brics["on_earth"]=[True,True,True,True]
#通过现有的列,构造新的列
brics["ab"]=brics["area"] / brics["num"]
brics["cd"]=brics.area / brics.num


print("打印全部\n",brics)
print("打印列名称\n",brics.coutry)

#获取到行
print("获取到一行\n",brics.loc["RS"])
print("获取到俄罗斯首都\n",brics.loc["RS"]["capition"])