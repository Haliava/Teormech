import math
import numpy as np

# general
G = 9.8
t = np.linspace(0, 120, 1000)

# slope
SLOPE_K = 2
SLOPE_ANGLE = math.degrees(np.arctan(SLOPE_K))

# prism
PRISM_M = 5

# cylinder
CYLINDER_PRISM_OFFSET_X = 1
CYLINDER_PRISM_OFFSET_Y = -0.2
CYLINDER_RADIUS = 0.15
K = 0

# rod
ROD_WIDTH = 0.15
ROD_LENGTH = 3
ROD_M = 2

# functions
PHI_T = 1.2 * np.sin(t)
PRISM_DX = 0.0005 * t
PRISM_DY = -0.00025 * t
S = np.cos(t)

# spiral
N_SPIRAL_TURNS = 3
THETA = np.linspace(0, N_SPIRAL_TURNS * 2 * math.pi - PHI_T[0], 100)
THETA_MAX = THETA[-1]
R_INNER = 0.08
R_OUTER = 0.4
