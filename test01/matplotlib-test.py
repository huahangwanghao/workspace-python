import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24
#设置随机的种子
np.random.seed(5)

# x轴的采样点, 等差数列  0~5 之间 取出来100个值
x = np.linspace(0, 5, 9)

# 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……   下面相当于俩个矩阵的相加
y = 2*np.sin(x) + 0.3*x**2
#什么 高斯的方程... 没有看懂
y_data = y + np.random.normal(scale=0.3, size=9)

# figure()指定图表名称
plt.figure('数据')

# '.'标明画散点图，每个散点的形状是个圆
plt.plot(x, y_data, '.')

# 画模型的图，plot函数默认画连线图
plt.figure('模型')
plt.plot(x, y)

# 两个图画一起
plt.figure('数据 & 模型')

# 通过'k'指定线的颜色，lw指定线的宽度
# 第三个参数除了颜色也可以指定线形，比如'r--'表示红色虚线
# 更多属性可以参考官网：http://matplotlib.org/api/pyplot_api.html
plt.plot(x, y, 'k', lw=3)

# scatter可以更容易地生成散点图
plt.scatter(x, y_data)

# 将当前figure的图保存到文件result.png
plt.savefig('result.png')

# 一定要加上这句才能让画好的图显示在屏幕上
plt.show()