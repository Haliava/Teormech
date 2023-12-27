import math
import numpy as np
import sympy as sp
from matplotlib.transforms import Affine2D
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from utils import *
from constants import *

fig = plt.figure(figsize=(9, 8))

graph = fig.add_subplot(1, 1, 1)
graph.axis('equal')
graph.set_title("Model of the system movement")
graph.set_xlabel("Ox")
graph.set_ylabel("Oy")
graph.set(xlim=[-3, 5], ylim=[-3, 5])

prismVertices = [
    [-1, slopeFunction(-1)],
    [2, slopeFunction(-1)],
    [2, slopeFunction(2)],
    [-1, slopeFunction(-1)],
]
newPrismVertices = prismVertices
cylinderCenterCoords = calculatePrismMidPoint(prismVertices)
rodCornerCoords = calculatePrismMidPoint(prismVertices)


prism = graph.plot(
    list([x[0] for x in prismVertices]), list([x[1] for x in prismVertices]), color=[0, 0, 1]
)[0]


def drawPrism(vertices, transormXY=[0, 0], theta=0):
    prism = patches.Polygon(vertices, color="blue", alpha=0.5)
    rotation = Affine2D().rotate_deg(theta)
    translation = Affine2D().translate(transormXY[0], transormXY[1])
    prism.set_transform(rotation + translation + graph.transData)
    return prism


def drawCylinder(centerCoords, r=CYLINDER_RADIUS):
    cylinder = plt.Circle(centerCoords, r)
    return cylinder


def drawRod(
        cornerCoords, width=ROD_WIDTH, height=ROD_HEIGHT,
        transormXY=[-CYLINDER_RADIUS / 2, CYLINDER_RADIUS / 2], theta=0
):
    rectangle = patches.Rectangle(cornerCoords, width, height, color='green')
    rotation = Affine2D().rotate_deg(theta)
    translation = Affine2D().translate(transormXY[0], transormXY[1])
    rectangle.set_transform(rotation + translation + graph.transData)
    return rectangle


# initial slope
graph.plot([-3, 4], [1.5, -2])

#prism = drawPrism(prismVertices)
cylinder = drawCylinder(cylinderCenterCoords)
rod = drawRod(rodCornerCoords)

def init():
    global rodCornerCoords, prismVertices, cylinderCenterCoords
    graph.add_patch(prism)
    graph.add_patch(cylinder)
    graph.add_patch(rod)
    return cylinder, rod, prism

def animation(frame):
    global rodCornerCoords, prismVertices, cylinderCenterCoords
    prismVertices = [[x[0] + 0.0005*frame, x[1] - 0.00025 * frame] for x in prismVertices]
    prism.set_xy(prismVertices)

    newCylinderCenterCoords = calculatePrismMidPoint(prismVertices)
    cylinder.set_transform(Affine2D().translate(*newCylinderCenterCoords) + graph.transData)
    cylinderCenterCoords = newCylinderCenterCoords

    rodCornerCoords = calculatePrismMidPoint(prismVertices)
    rodCornerCoords = [rodCornerCoords[0] + PHI_T[frame], rodCornerCoords[1] + S[frame]]
    rod.set_xy(rodCornerCoords)
    return cylinder, rod, prism


#show_movement = FuncAnimation(fig, animation, init_func=init, frames=len(t), interval=10, repeat=True)

if __name__ == "__main__":
    plt.show()
