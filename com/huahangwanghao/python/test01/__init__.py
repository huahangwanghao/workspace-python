import numpy as np
#里面包含了等差数列和reshape变为2维数组
lst=np.arange(1,9,2).reshape(2,2)
print("对于等差数列进行变为二维数组",lst)

print("对于等差数列进行变为二维数组",np.exp(lst))
print("对于等差数列进行变为二维数组",np.exp2(lst))
print("对于等差数列进行变为二维数组",np.sin(lst))
print("对于等差数列进行变为二维数组",np.sqrt(lst))

a=[[[1,2,3,4],[4,5,6,7]],
   [[5.6,7,8],[9,10,11,12]],
   [[13,14,15,16],[17,18,19,20]]
  ]

list=np.array(a)

print(list.sum(axis=0))