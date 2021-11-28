import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    r = 10
    circle1 = plt.Circle((0, 0), r, color='r')
    ax=plt.gca()
    ax.add_patch(circle1)
    plt.axis('scaled')
    plt.show()
