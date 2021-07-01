import math
from typing import List
from .matrix import Matrix

############################################################

def Rx(theta: float) -> Matrix:
    """Returns a Rotation Matrix for the X axis"""
    s = math.sin(theta)
    c = math.cos(theta)

    rotMatrix = Matrix(3,3)
    rotMatrix.data[0] = [1, 0, 0]
    rotMatrix.data[1] = [0, c, -s]
    rotMatrix.data[2] = [0, s, c]

    return rotMatrix

def Ry(theta: float) -> Matrix:
    """Returns a Rotation Matrix for the Y axis"""
    s = math.sin(theta)
    c = math.cos(theta)

    rotMatrix = Matrix(3,3)
    rotMatrix.data[0] = [c, 0, s]
    rotMatrix.data[1] = [0, 1, 0]
    rotMatrix.data[2] = [-s, 0, c]

    return rotMatrix

def Rz(theta: float) -> Matrix:
    """Returns a Rotation Matrix for the Z axis"""
    s = math.sin(theta)
    c = math.cos(theta)

    rotMatrix = Matrix(3,3)
    rotMatrix.data[0] = [c, -s, 0]
    rotMatrix.data[1] = [s, c, 0]
    rotMatrix.data[2] = [0, 0, 1]

    return rotMatrix

############################################################