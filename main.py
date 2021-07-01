# Computer Science Project
# SlightlyEpic
# https://github.com/SlightlyEpic/RubiksCube

############################################################
# Imports
############################################################

import sys
import tkinter as tk
import math

from modules.matrix import Matrix, listMap
import modules.helper as helper
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
# Testing stuff out
############################################################

offset = 200

Ry45 = helper.Ry(math.pi/6)
Rx45 = helper.Rx(math.pi/6)

verts = [(0,0,0), (100,0,0), (0,0,100), (100,0,100),
         (0,100,0), (100,100,0), (0,100,100), (100,100,100)]   # (x,y,z)

for i in range(len(verts)):
    verts[i] = Matrix.static_fromArray(verts[i])               # Convert from List to Matrix
    verts[i] = Matrix.static_multiply(Ry45, verts[i])          # Rotate all vertices by 45 degrees about Y axis
    verts[i] = Matrix.static_multiply(Rx45, verts[i])          # Rotate all vertices by 45 degrees about X axis

edges = [(0,1), (0,2), (3,1), (3,2), 
         (4,5), (4,6), (7,5), (7,6),
         (0,4), (1,5), (2,6), (3,7)]

project = lambda vert: (vert.data[0][0], vert.data[1][0])

projected = []

for vert in verts:
    projected.append(project(vert))

for edge in edges:
    v1 = projected[edge[0]]
    v2 = projected[edge[1]]
    canvas.create_line(v1[0]+offset, v1[1]+offset, v2[0]+offset, v2[1]+offset, fill="#FFFFFF")

# This makes a cube

############################################################
# 
############################################################

win.mainloop()