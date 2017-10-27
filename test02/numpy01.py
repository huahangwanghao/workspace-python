import  numpy as np

h=[1,2,3]
w=[4,5,6]

np_h=np.array(h)
np_w=np.array(w)
print(np_h+np_w)
print("平方是**2",np_h**2)


np_test=np.array([1,2,3,4,5,6])
print("判断里面值大于3的内容:",np_test>3)
print("里面的类型,必须全部是一种类型,否则有字符串就变成字符串啦",np_test)
print("判断里面值大于3的内容",np_test[np_test>3])


'''
[ [170 169 188 190]
  [ 60  80  78 98]
]
'''

np_2d=np.array([[170,169,188,190,34,23],[60,80,78,98,23,1]])
print("二维数组:",np_2d)
print("几行几列",np_2d.shape)
print("第一行",np_2d[0])
print("第一行,第一列",np_2d[0][0])
print("另一种方式:第一行,第一列",np_2d[0,0])
# [a,b] 表示 a行b列  x:y 表示 [x,y) 如果前后不写, 表示所有
print("另一种方式:第一行,第一列",np_2d[:,1:3])
print("查询所有的体重:",np_2d[1,:])
print("平均体重:",np.mean(np_2d[1,:]))
print("中位数:",np.median(np_2d[1,:]))


print("身高体重的相关性",np.corrcoef(np_2d[0,:],np_2d[1,:]))


#随机数
print("随机的问题",np.round(np.random.normal(100,1,100)))
print("随机的问题123",np.random.normal(100,1,100))
'''
h=[1,2,3]
w=[4,5,6]

列连接 [[1 4]
 [2 5]
 [3 6]]

'''
print("列连接",np.column_stack((np_h,np_w)))
print("行连接",np.row_stack((np_h,np_w)))


'''
行连接 [[1 2 3]
 [4 5 6]]
'''