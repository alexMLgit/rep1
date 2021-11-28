import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    x = np.arange(-10, 10, 0.01)

    def function(x):
        return np.sin(x)

    plots=[]

    for xi in x:
        temp = np.array([xi, (function(xi)-function(xi-0.01))/0.01])
        plots.append(temp)

    plt.plot(x, function(x))    

    plt.title("График функции")
    plt.grid(True)
    plt.show()

    for pt in plots:
            plt.plot(pt[0], pt[1], 'r.')

    plt.title("Производная функции")
    plt.grid(True)
    plt.show()