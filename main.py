#Computer Science Project
#SlightlyEpic

############################################################
# Imports
############################################################

import sys
import tkinter as tk

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

win.mainloop()