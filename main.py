from math import *
import numpy as np
from celluloid import Camera
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def drawArc(parametrs, axes):
    # Рисование дуги
    arc_x = parametrs[0][1]
    arc_y = parametrs[0][2]
    arc_width = parametrs[3]
    arc_height = parametrs[3]
    arc_theta1 = parametrs[0][3]
    arc_theta2 = parametrs[0][4]

    arc = patches.Arc((arc_x, arc_y), arc_width, arc_height, theta1=arc_theta1, theta2=arc_theta2)
    axes.add_patch(arc)
    plt.text(0.6, -0.3, "Arc", horizontalalignment="center")


def draw(parametres, ax):
    ax.hlines(0, parametres[0][0], parametres[0][1])
    ax.hlines(parametres[3], parametres[1], parametres[2])
    drawArc(parametres, ax)


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
    delta_t = 0.005

    m = 100
    g = 9.8
    p = 2000
    v = 0

    freq = int(all_time / step)
    x = np.zeros(5, dtype=np.float64)

    fig, ax = plt.subplots()

    camera = Camera(fig)
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

        all_parametrs = [x, Ax, Bx, Ay, C, By]

        draw(all_parametrs, ax)
        camera.snap()
        Ay += v * step
        v += (1 / m) * (p * delta_x - m * g) * step
        By = Ay

    animation = camera.animate()
    animation.save('camera.gif')
    # print(x)
    # print()
    print('x1 = {}'.format(x[0]))
    print('x2 = {}'.format(x[1]))
    print('y = {}'.format(x[2]))
    print('phi1 = {}'.format(x[3]))
    print('phi2 = {}'.format(x[4]))
