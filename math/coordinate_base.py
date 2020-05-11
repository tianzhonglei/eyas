import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

fig = plt.figure(figsize=(5, 5))
ax = axisartist.Subplot(fig, 111)  # 使用axisartist.Subplot方法创建一个绘图区对象ax
fig.add_axes(ax)  # 将绘图区对象添加到画布中

ax.axis[:].set_visible(False)  # 隐藏原来的实线矩形

ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="bottom")  # 添加y轴

ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加箭头
ax.axis["y"].set_axisline_style("->", size=1.0)  # 给y坐标轴加箭头
ax.annotate(s='x', xy=(2 * math.pi, 0), xytext=(2 * math.pi, 0.1))  # 标注x轴
ax.annotate(s='y', xy=(0, 1.0), xytext=(-0.5, 1.0))  # 标注y轴

plt.xlim(-10.0, 10.0)  # 设置横坐标范围
plt.ylim(-10.0, 10.0)  # 设置纵坐标范围
ax.set_xticks([-10, -5, 0, 5, 10])  # 设置x轴刻度
ax.set_yticks([-10, -5, 5, 10])  # 设置y轴刻度

#y = []  # 用来存放函数值
#x = np.linspace(-2 * math.pi, 2 * math.pi, 100)  # 构造横坐标数据
#for xi in x:  # 生成函数值
#    y.append(math.sin(xi))  # 追加

x = np.arange(-10, 10, 0.1)
x1 = np.arange(-10, 5, 0.1)

y = x
y1 = 2 * x1

plt.title("Proportional Function")
plt.plot(x, y)
plt.plot(x1, y1)

plt.plot(x, y, color="blue")  # 描点连线
plt.show()  # 出图
