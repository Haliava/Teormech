import numpy as np
import sympy as sp

t = sp.Symbol('t')


def rotate(x, y, angle):
    return (x * np.cos(angle) - y * np.sin(angle),
            x * np.sin(angle) + y * np.cos(angle))


def calculateVxVy(x, y):
    return sp.diff(x, t), sp.diff(y, t)


def calculateAxAy(x, y):
    return (sp.diff(calculateVxVy(x, y)[0], t),
            sp.diff(calculateVxVy(x, y)[1], t))


def calculateAtanAnorm(v, w):
    wTan = sp.diff(v, t)
    wNorm = sp.sqrt(w ** 2 - wTan ** 2)
    return wTan, wNorm
