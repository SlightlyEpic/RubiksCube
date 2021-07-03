# Computer Science Project
# SlightlyEpic
# https://github.com/SlightlyEpic/RubiksCube

############################################################
# Imports
############################################################

import sys
import tkinter as tk
import math
from tkinter.constants import ALL
from typing import List
import copy

from modules.matrix import Matrix, listMap
import modules.helper as Helper
import modules.renderer as Renderer
from modules.cube import RubiksCube as Cube
import config

############################################################
# Main
############################################################

win = tk.Tk()
win.title("Rubik's Cube")
win.geometry("512x512")
win.resizable(0,0)

canvas = tk.Canvas(win, height=config.canvas_height, width=config.canvas_width, bg="#000000")
canvas.pack()

############################################################
# Debug mode stuff
############################################################

_DEBUG = False
if("-d" in sys.argv): _DEBUG = True

def showVars():
    pass

if _DEBUG:
    def showVarsMain():
        # Code here
        pass
    showVars = showVarsMain

############################################################
# Testing stuff out
############################################################

offset = {
    "x": 0,
    "y": 0,
    "z": 0
}

camera_pos = (216,216)

Ry45 = Helper.Ry(math.pi/6)
Rx45 = Helper.Rx(math.pi/6)

deltaRx = Helper.Rx(0.005)
deltaRy = Helper.Ry(0.005)

"""
verts = [(0,0,0), (100,0,0), (0,0,100), (100,0,100),
         (0,100,0), (100,100,0), (0,100,100), (100,100,100)]   # (x,y,z)

for i in range(len(verts)):
    verts[i] = Matrix.static_fromArray(verts[i])               # Convert from List to Matrix
    verts[i] = Matrix.static_multiply(Ry45, verts[i])          # Rotate all vertices by 45 degrees about Y axis
    verts[i] = Matrix.static_multiply(Rx45, verts[i])          # Rotate all vertices by 45 degrees about X axis

edges = [(0,1), (0,2), (3,1), (3,2), 
         (4,5), (4,6), (7,5), (7,6),
         (0,4), (1,5), (2,6), (3,7)]

while True:
    for i in range(len(verts)):
        verts[i] = Matrix.static_multiply(deltaRx, verts[i])
        #verts[i] = Matrix.static_multiply(deltaRy, verts[i])
    Renderer.renderEdges(canvas, verts, edges)
"""

verts = copy.deepcopy(Cube.origin_cubelet["verts"])
edges = copy.deepcopy(Cube.origin_cubelet["edges"])
faces = copy.deepcopy(Cube.origin_cubelet["faces"])

for i in range(len(verts)):
    verts[i] = (verts[i][0]+offset["x"], verts[i][1]+offset["y"], verts[i][2]+offset["z"])
    verts[i] = Matrix.static_fromArray(verts[i])               # Convert from List to Matrix
    verts[i] = Matrix.static_multiply(Ry45, verts[i])          # Rotate all vertices by 45 degrees about Y axis
    verts[i] = Matrix.static_multiply(Rx45, verts[i])          # Rotate all vertices by 45 degrees about X axis

while True:
    for i in range(len(verts)):
        pass
        verts[i] = Matrix.static_multiply(deltaRx, verts[i])
        #verts[i] = Matrix.static_multiply(deltaRy, verts[i])
    Renderer.renderFaces(canvas, verts, faces, camera_pos)

    showVars()      # Debug method

# This makes a cube

############################################################
# 
############################################################

win.mainloop()