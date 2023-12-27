import math
import numpy as np
from scipy.integrate import odeint

# general
K = 0.005
K1 = 0.03
G = 9.8
t = np.linspace(0, 120, 1000)

# slope
SLOPE_K = 2
SLOPE_ANGLE = 0.01

# prism
PRISM_M = 5  # m1

# cylinder
CYLINDER_PRISM_OFFSET_X = 1
CYLINDER_PRISM_OFFSET_Y = -0.2
CYLINDER_RADIUS = 0.15

# rod
ROD_WIDTH = 0.15
ROD_LENGTH = 0.2
ROD_M = 2  # m2

# spiral
SPIRAL_C = 0.1
N_SPIRAL_TURNS = 2
THETA = np.linspace(0, N_SPIRAL_TURNS * 2 * math.pi, 100)
THETA_MAX = THETA[-1]
R_INNER = 0.08
R_OUTER = 0.25


# differential equation
def odesys(y, t):
    dy = np.zeros(4)
    dphi = y[2]
    phi = y[0]

    a11 = - ROD_M * ROD_LENGTH * np.cos(phi + SLOPE_ANGLE)
    a12 = 2 * ROD_M + 2 * PRISM_M
    a21 = 1 / 3 * ROD_M * ROD_LENGTH ** 2
    a22 = -1 / 2 * ROD_M * ROD_LENGTH * np.cos(phi + SLOPE_ANGLE)

    b1 = 2 * PRISM_M * G * np.sin(SLOPE_ANGLE) + 2 * ROD_M * G * np.sin(SLOPE_ANGLE) \
        - ROD_M * ROD_LENGTH * dphi ** 2 * np.sin(phi + SLOPE_ANGLE)
    b2 = 1 / 2 * ROD_M * ROD_LENGTH * G * np.sin(phi) - K * dphi - SPIRAL_C * phi

    dy = [y[2], y[3], (b1 * a22 - b2 * a12) / (a11 * a22 - a12 * a21),
          (b2 * a11 - b1 * a21) / (a11 * a22 - a12 * a21)]

    return dy


PHI_0 = -0.5236
S_0 = 0
DPHI_0 = 4
DS_0 = 0
Y = odeint(odesys, [PHI_0, S_0, DPHI_0, DS_0], t)

# functions
PHI_T = Y[:, 0]
S_T = Y[:, 1]
PRISM_DX = 0.005 * S_T
PRISM_DY = -0.0025 * S_T
