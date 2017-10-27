# coding:utf-8
import  matplotlib.pyplot as plt
import matplotlib
year=[1975]+[1980,1985,1990,2000,2005,2010,2015]
num=[4]+[5.12,8.12,9.00,10.23,11.56,12.44,17.34]
# 直线图 x,y 的值
plt.plot(year,num)
# 散点图
#plt.scatter(year,num)
#进行数据填充
plt.fill_between(year,num,0,color='green')
plt.xlabel(u"year")
plt.ylabel("num")
plt.title("this is population img")
plt.yticks([0,2,4,6,8,10,12,14,16,18,20],['0B','2B','4B','6B','8B','10B','12B','14B','16B','18B'])
#显示出来
plt.show()
plt.close(0)
#-----------------直方图
# list1=[0,0.6,1.2,2.4,3.4,4.4,4.5,6]
# plt.hist(list1,3)
# plt.show()