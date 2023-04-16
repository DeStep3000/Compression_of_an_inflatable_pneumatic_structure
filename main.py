from math import *
import numpy as np
from celluloid import Camera as cum
import matplotlib.pyplot as plt
import matplotlib


def drawArc(BIG, axes):
    # Рисование дуги
    arc_x = BIG[0][1]
    arc_y = BIG[0][2]
    arc_width = BIG[3]
    arc_height = BIG[3]
    arc_theta1 = BIG[0][3]
    arc_theta2 = BIG[0][4]

    arc = matplotlib.patches.Arc((arc_x, arc_y), arc_width, arc_height, theta1=arc_theta1, theta2=arc_theta2)
    axes.add_patch(arc)
    plt.text(0.6, -0.3, "Arc", horizontalalignment="center")


def draw(BIG, ax):
    ax.hlines(0, BIG[0][0], BIG[0][1])
    ax.hlines(BIG[3], BIG[1], BIG[2])
    drawArc(BIG, ax)


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
    delta_t = 0.9

    m = 100
    g = 9.8
    p = 2000
    v = 0

    freq = int(all_time / step)
    x = np.zeros(5, dtype=np.float64)

    fig, ax = plt.subplots()

    cam = cum(fig)
    for i in range(freq):
        while True:
            count = 0
            x_next = x - F(x) * delta_t
            for j in range(5):
                if abs(x[j] - x_next[j]) < EPSILON:
                    count += 1
            if count == 5:
                break
            x = x_next
        delta_x = abs(x[0] - x[1])

        BIG = [x, Ax, Bx, Ay, C, By]

        draw(BIG, ax)
        cam.snap()
        Ay += v * step
        v += (1 / m) * (p * delta_x - m * g) * step
        By = Ay

    animation = cam.animate()
    animation.save('FEDYA.gif', writer="Pillow")
    # print(x)
    # print()
    print('x1 = {}'.format(x[0]))
    print('x2 = {}'.format(x[1]))
    print('y = {}'.format(x[2]))
    print('phi1 = {}'.format(x[3]))
    print('phi2 = {}'.format(x[4]))
