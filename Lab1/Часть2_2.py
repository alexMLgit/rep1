import numpy as np
import matplotlib.pyplot as plt

def Calculate_the_function_f(x):
    return x - (x**3)/6 + (x**5)/120 - (x**7)/5040

def Calculate_the_function_g(x):
    return np.sin(x)

if __name__ == '__main__':
    xmin = -5.0
    xmax = 5.0
    xlist = np.linspace(xmin, xmax, 1000)
    ylist_f = [Calculate_the_function_f(x) for x in xlist]
    ylist_g = [Calculate_the_function_g(x) for x in xlist]
    plt.plot(xlist, ylist_f)
    plt.plot(xlist, ylist_g)
    plt.show()
