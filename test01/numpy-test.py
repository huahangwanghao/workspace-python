
import numpy as np
#一维数组
print("*************一维数组*****************")
a=[1,2,3,4,5]
b=np.array(a)
# 矩阵的长度
print("几行几列",b.shape)
#参数最大索引
print("参数最大索引",b.argmax())
#最大值
print("最大值",b.max())
#数据的平均值
print("数据的平均值",b.mean())

#二维数组
print("*************二维数组*****************")
c=[[1,2,3],[4,5,6]]
d=np.array(c)
print("几行几列",d.shape)
print("共多少元素",d.size)
print("竖着的y轴的最大值",d.max(axis=0))
print("横着的x轴的最大值",d.max(axis=1))
print("转化为一维数组",d.flatten())


