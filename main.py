from math import *
import numpy as np
from celluloid import Camera
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def drawArc(parametrs, axes):
    # Рисование дуг
    arc_x1 = parametrs[0][0]
    arc_x2 = parametrs[0][1]
    arc_y = parametrs[0][2]
    arc_theta1 = parametrs[0][3]
    arc_theta2 = parametrs[0][4]

    arc_Ax = parametrs[1]
    arc_Bx = parametrs[2]
    arc_Ay = parametrs[3]

    ang = 180 / pi
    c = 3 * pi / 2

    radius1 = ((arc_x1 - arc_Ax) ** 2 + (arc_y - arc_Ay) ** 2) ** 0.5
    radius2 = ((arc_x2 - arc_Bx) ** 2 + (arc_y - arc_Ay) ** 2) ** 0.5

    # Дуга слева
    arc1 = patches.Arc((arc_x1, arc_y), 2 * radius1, 2 * radius1, 0,
                       (c - arc_theta1) * ang, c * ang, color="purple", linewidth=2)
    # Дуга справа
    arc2 = patches.Arc((arc_x2, arc_y), 2 * radius2, 2 * radius2, 270,
                       0, arc_theta2 * ang, color="purple", linewidth=2)

    axes.add_patch(arc1)
    axes.add_patch(arc2)

def drawLines(parametrs, ax):
    # Рисование линий
    arc_x1 = parametrs[0][0]
    arc_x2 = parametrs[0][1]

    arc_Ax = parametrs[1]
    arc_Bx = parametrs[2]
    arc_Ay = parametrs[3]
    ax.hlines(0, arc_x1, arc_x2, color="purple", linewidth=2)
    ax.hlines(arc_Ay, arc_Ax, arc_Bx, color="purple", linewidth=2)


def F(x):
    # Система уравнений F(от вектора x)
    fx = np.zeros(5, dtype=np.float64)
    fx[0] = x[0] + x[2] * np.cos(3 * pi / 2 - x[3]) - Ax
    fx[1] = x[1] + x[2] * np.cos(3 * pi / 2 + x[4]) - Bx
    fx[2] = x[2] + x[2] * np.sin(3 * pi / 2 - x[3]) - Ay
    fx[3] = (x[3] + x[4]) * x[2] + (x[1] - x[0]) - C
    fx[4] = x[2] + x[2] * np.sin(3 * pi / 2 + x[4]) - By
    return fx


if __name__ == "__main__":
    # Ваши ЗНАЧЕНИЯ
    Ax = -0.353
    Bx = 0.353
    Ay = By = 0.3
    C = 3 * pi / 8
    EPSILON = 1e-6

    # Значения, связанные со временем
    all_time = 2.5
    step = 0.01
    delta_t = 0.05
    freq = int(all_time / step)

    # Физические значения
    m = 100
    g = 9.8
    p = 2000
    v = 0

    x = np.zeros(5, dtype=np.float64)# Значения: x1, x2, y, phi1, phi2

    # Для графика
    fig, ax = plt.subplots()
    plt.ylim([-0.1, 0.4])
    plt.xlim([-0.5, 0.5])
    camera = Camera(fig)

    for i in range(freq):
        # Метод подгонки
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

        all_parametrs = [x, Ax, Bx, Ay, C, By] # Список параметров

        # Значения для следующего шага
        Ay += v * step
        v += (1 / m) * (p * delta_x - m * g) * step
        By = Ay

        drawLines(all_parametrs, ax)
        drawArc(all_parametrs, ax)
        camera.snap()

    animation = camera.animate()
    animation.save('FEDYA.gif')
    # print(x)
    # print()
    print('x1 = {}'.format(x[0]))
    print('x2 = {}'.format(x[1]))
    print('y = {}'.format(x[2]))
    print('phi1 = {}'.format(x[3]))
    print('phi2 = {}'.format(x[4]))
