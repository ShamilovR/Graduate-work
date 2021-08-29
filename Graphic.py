import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class CreateGraph:
    def __init__(self, func_result, X1, X2, name):
        self.func_result = func_result
        self.X1 = X1
        self.X2 = X2
        self.name = name

    def create_graph(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        fig.canvas.manager.set_window_title(self.name)
        fig.set_facecolor('gray')
        ax.set_facecolor('gray')

        z_line = self.func_result
        x_line = self.X1
        y_line = self.X2

        ax.plot3D(x_line, y_line, z_line, 'red')

        plt.show()


