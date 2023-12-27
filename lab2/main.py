import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from utils import *
from constants import *

fig = plt.figure(figsize=(9, 8))

graph = fig.add_subplot(1, 1, 1)
graph.axis('equal')
graph.set_title("Teormech #2")
graph.set_xlabel("Ox")
graph.set_ylabel("Oy")
graph.set(xlim=[-3, 5], ylim=[-3, 5])

prismVertices = [
    [-1, slopeFunction(-1)],
    [2, slopeFunction(-1)],
    [2, slopeFunction(2)],
    [-1, slopeFunction(-1)],
]
prismVertices = calculatePrismVerticesCoords(prismVertices, PRISM_DX[0], PRISM_DY[0])
midX, midY = calculatePrismMidPoint(prismVertices)

# rod end coordinates
Ax = midX - ROD_LENGTH * np.sin(PHI_T)
Ay = midY + ROD_LENGTH * np.cos(PHI_T)

rod = graph.plot(
    [Ax[0], midX], [Ay[0], midY], color=[0, 0, 1], linewidth=7.0
)[0]

prism = graph.plot(
    list([x[0] for x in prismVertices]), list([x[1] for x in prismVertices]), color=[0, 0, 1]
)[0]

cylinderAngles = np.linspace(0, 2 * math.pi, 100)
cylinder = graph.plot(
    midX + CYLINDER_RADIUS * np.cos(cylinderAngles),
    midY + CYLINDER_RADIUS * np.sin(cylinderAngles)
)[0]

spiralX = - (R_INNER + THETA * (R_OUTER - R_INNER) / THETA_MAX) * np.sin(THETA)
spiralY = (R_INNER + THETA * (R_OUTER - R_INNER) / THETA_MAX) * np.cos(THETA)
spiral = graph.plot(spiralX + midX, spiralY + midY)[0]

# Oxy axis
Ox = graph.plot(
    [midX, midX + 2], [midY, midY], color='red', linewidth=3, linestyle='dashed', alpha=0.5, marker='>'
)[0]
Oy = graph.plot(
    [midX, midX], [midY, midY + 2], color='red', linewidth=3, linestyle='dashed', alpha=0.5, marker='^'
)[0]

# initial slope
graph.plot([-3, 6], [1.5, -3])

def animation(frame):
    global prismVertices
    prismVertices = calculatePrismVerticesCoords(prismVertices, PRISM_DX[frame], PRISM_DY[frame])
    midX, midY = calculatePrismMidPoint(prismVertices)
    Ax = midX - ROD_LENGTH * np.sin(PHI_T)
    Ay = midY + ROD_LENGTH * np.cos(PHI_T)
    THETA = np.linspace(0, N_SPIRAL_TURNS * 2 * math.pi + PHI_T[frame], 100)
    spiralX = - (R_INNER + THETA * (R_OUTER - R_INNER) / THETA_MAX) * np.sin(THETA)
    spiralY = (R_INNER + THETA * (R_OUTER - R_INNER) / THETA_MAX) * np.cos(THETA)

    Ox.set_data([midX, midX + 2], [midY, midY])
    Oy.set_data([midX, midX], [midY, midY + 2])

    prism.set_data(list([x[0] for x in prismVertices]), list([x[1] for x in prismVertices]))
    cylinder.set_data(
        midX + CYLINDER_RADIUS * np.cos(cylinderAngles),
        midY + CYLINDER_RADIUS * np.sin(cylinderAngles)
    )
    spiral.set_data(spiralX + midX, spiralY + midY)
    rod.set_data([Ax[frame], midX], [Ay[frame], midY])


show_movement = FuncAnimation(fig, animation, frames=len(t), interval=12.6, repeat=True)
animation_running = True


def animation_pause(e):
    global animation_running

    if animation_running:
        show_movement.event_source.stop()
    else:
        show_movement.event_source.start()
    animation_running = not animation_running


if __name__ == "__main__":
    fig.canvas.mpl_connect('button_press_event', animation_pause)
    plt.show()