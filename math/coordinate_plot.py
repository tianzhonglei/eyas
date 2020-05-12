import math
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


class CoordinatePlot(object):
    def __init__(self, fig_x_size=5, fig_y_size=5, x_scale=[-10, -5, 0, 5, 10], y_scale=[-10, -5, 5, 10]):
        fig = plt.figure(figsize=(fig_x_size, fig_x_size))
        ax = axisartist.Subplot(fig, 111)  # 使用axisartist.Subplot方法创建一个绘图区对象ax
        fig.add_axes(ax)  # 将绘图区对象添加到画布中

        ax.axis[:].set_visible(False)  # 隐藏原来的实线矩形

        ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
        ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="bottom")  # 添加y轴

        ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加箭头
        ax.axis["y"].set_axisline_style("->", size=1.0)  # 给y坐标轴加箭头
        ax.annotate(s='x', xy=(2 * math.pi, 0), xytext=(2 * math.pi, 0.1))  # 标注x轴
        ax.annotate(s='y', xy=(0, 1.0), xytext=(-0.5, 1.0))  # 标注y轴

        ax.set_xticks(x_scale)  # 设置x轴刻度
        ax.set_yticks(y_scale)  # 设置y轴刻度

        plt.xlim(x_scale[0], x_scale[len(x_scale) - 1])  # 设置横坐标范围
        plt.ylim(y_scale[0], y_scale[len(y_scale) - 1])  # 设置纵坐标范围

    def set_title(self, title):
        plt.title(title)

    def set_values(self, data):
        for x, y in data:
            plt.plot(x, y)

    def drawCorrdinatePlot(self):
        plt.show()
