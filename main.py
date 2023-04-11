from math import *
import numpy as np

def F(x):
    fx = np.zeros(5, dtype=np.float64)
    fx[0] = x[0] + x[2] * np.cos(3 * pi / 2 - x[3]) - Ax
    fx[1] = x[1] + x[2] * np.cos(3 * pi / 2 + x[4]) - Bx
    fx[2] = x[2] + x[2] * np.sin(3 * pi / 2 - x[3]) - Ay
    fx[3] = (x[3] + x[4]) * x[2] + (x[1] - x[0]) - C
    fx[4] = x[2] + x[2] * np.sin(3 * pi / 2 + x[4]) - By
    return fx


if __name__ == "__main__":
    Ax = -0.353
    Bx = 0.353
    Ay = By = 0.3
    C = 3 * pi / 8
    EPSILON = 1e-6

    all_time = 2.5
    step = 0.01

    freq = int(all_time / step)
    x = np.zeros(5, dtype=np.float64)

    # values = [[x1, x2, y, phi1, phi2]] * freq
    for i in range(freq):
        while True:
            count = 0
            x_next = x - F(x) * step
            for j in range(5):
                if abs(x[j] - x_next[j]) < EPSILON:
                    count += 1
            if count == 5:
                break
            x = x_next
    print('x1 = {}'.format(x[0]))
    print('x2 = {}'.format(x[1]))
    print('y = {}'.format(x[2]))
    print('phi1 = {}'.format(x[3]))
    print('phi2 = {}'.format(x[4]))

