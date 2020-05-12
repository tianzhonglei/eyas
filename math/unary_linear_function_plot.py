import numpy as np


import coordinate_plot

class UnaryLinearFunctionPlot(coordinate_plot.CoordinatePlot):

    pass

if __name__ == "__main__":
    unary_linear_function_plot = UnaryLinearFunctionPlot()
    x = np.arange(-10, 10, 0.1)
    x1 = np.arange(-10, 5, 0.1)
    y = x + 1
    y1 = 2 * x1 + 1
    data = [(x, y), (x1, y1)]
    unary_linear_function_plot.set_title("Unary linear function")
    unary_linear_function_plot.set_values(data)
    unary_linear_function_plot.drawCorrdinatePlot()
