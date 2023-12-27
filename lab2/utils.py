import numpy as np
from constants import ROD_LENGTH, ROD_WIDTH, CYLINDER_PRISM_OFFSET_X, CYLINDER_PRISM_OFFSET_Y


def slopeFunction(x, k=-0.5, b=0):
    return k * x + b


def calculatePrismVerticesCoords(currentPrismVertices, dx, dy):
    return list([[x + dx, y + dy] for [x, y] in currentPrismVertices])

def calculatePrismMidPoint(vertices):
    return sum([x[0] + CYLINDER_PRISM_OFFSET_X for x in vertices]) / len(vertices), \
        sum([x[1] + CYLINDER_PRISM_OFFSET_Y for x in vertices]) / len(vertices)


def calculateRodMidPoint(x, y):
    return x + ROD_WIDTH / 2, y + ROD_LENGTH / 2
