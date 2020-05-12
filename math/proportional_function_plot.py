import numpy as np

import coordinate_plot

class ProportionalFunctionPlot(coordinate_plot.CoordinatePlot):
    pass

if __name__ == "__main__":
    proportional_function_plot = ProportionalFunctionPlot()
    x = np.arange(-10, 10, 0.1)
    x1 = np.arange(-10, 5, 0.1)
    y = x
    y1 = 2 * x1
    data = [(x, y), (x1, y1)]
    proportional_function_plot.set_title("Proportional Function")
    proportional_function_plot.set_values(data)
    proportional_function_plot.drawCorrdinatePlot()