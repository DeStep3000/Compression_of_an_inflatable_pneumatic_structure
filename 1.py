def drawArc(axes):
    arc_x = 0
    arc_y = 0
    arc_width = 1
    arc_height = 1
    arc_theta1 = 270
    arc_theta2 = 360


    arc = matplotlib.patches.Arc((arc_x, arc_y),
    arc_width,
    arc_height,
    theta1=arc_theta1,
    theta2=arc_theta2)
    axes.add_patch(arc)
    plt.text(0.6, -0.3, "Arc", horizontalalignment="center")

