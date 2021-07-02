from tkinter import Canvas
from tkinter.constants import ALL
from .matrix import Matrix, listMap
from typing import List, Tuple
import math

def renderEdges(canvas: Canvas, verts: List[Matrix], edges: List[Tuple], camera_pos=(0,0), fill="#FFFFFF"):
    canvas.delete(ALL)
    projected = projectVertices(verts)

    for edge in edges:
        v1 = projected[edge[0]]
        v2 = projected[edge[1]]
        canvas.create_line(v1[0]+camera_pos[0], v1[1]+camera_pos[1], v2[0]+camera_pos[0], v2[1]+camera_pos[1], fill=fill)
    
    canvas.update()

def renderFaces(canvas: Canvas, verts: List[Matrix], faces: List[Tuple], camera_pos): # the occlusion culling is all wrong
    canvas.delete(ALL)
    projected = projectVertices(verts)
    #depth_map = listMap(verts, lambda e, i: math.sqrt(e.data[0][0]**2 + e.data[1][0]**2 + e.data[2][0]**2))

    #faces.sort(key=lambda face: (depth_map[face[0]] + depth_map[face[1]] + depth_map[face[2]])/3)

    for face in faces:
        canvas.create_polygon(
            projected[face[0]][0]+camera_pos[0], projected[face[0]][1]+camera_pos[1],
            projected[face[1]][0]+camera_pos[0], projected[face[1]][1]+camera_pos[1],
            projected[face[2]][0]+camera_pos[0], projected[face[2]][1]+camera_pos[1],
            fill=face[3]
        )
    
    canvas.update()
    

def projectVertices(verts: List[Matrix]):
    return listMap(verts, lambda vert, i: (vert.data[0][0], vert.data[1][0]))