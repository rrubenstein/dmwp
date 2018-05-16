import time
import random
from tkinter import *
import sys


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
#each room will be 60 units so that is a ten by ten grid
canvas = Canvas(tk, width=610, height=610)
canvas.pack()
tk.update()

def draw_room(rn, x1, y1):
    if rn == 1:
        x1 += 10
        x2 = x1 + 40
        y2 = y1 + 60
        canvas.create_line(x1, y1, x1, y2)
        canvas.create_line(x2, y1, x2, y2)
    elif rn == 2:
        x2 = x1 + 60
        y1 += 10
        y2 = y1 + 40
        canvas.create_line(x1, y1, x2, y1)
        canvas.create_line(x1, y2, x2, y2)
    elif rn == 3:
        x1 += 10
        x2 = x1 + 40
        y2 = y1 + 10
        x3 = x2 + 10
        y3 = y2 + 40
        canvas.create_line(x1, y1, x1, y3)
        canvas.create_line(x1, y3, x3, y3)
        canvas.create_line(x2, y1, x2, y2)
        canvas.create_line(x2, y2, x3, y2)
    elif rn == 4:
        x2 = x1 + 10
        x3 = x2 + 40
        y2 = y1 + 10
        y3 = y2 + 40
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x2, y1, x2, y2)
        canvas.create_line(x1, y3, x3, y3)
        canvas.create_line(x3, y3, x3, y1)
    elif rn == 5:
        x1 += 10
        x2 = x1 + 40
        x3 = x2 + 10
        y1 += 10
        y2 = y1 + 40
        y3 = y2 + 10
        canvas.create_line(x1, y1, x1, y3)
        canvas.create_line(x1, y1, x3, y1)
        canvas.create_line(x2, y2, x3, y2)
        canvas.create_line(x2, y2, x2, y3)
    elif rn == 6:
        x2 = x1 + 10
        x3 = x2 + 40
        y1 += 10
        y2 = y1 + 40
        y3 = y2 + 10
        canvas.create_line(x1, y1, x3, y1)
        canvas.create_line(x3, y1, x3, y3)
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x2, y2, x2, y3)
    elif rn == 7:
        x1 += 10
        x2 = x1 + 40
        x3 = x2 + 10
        y2 = y1 + 10
        y3 = y2 + 40
        y4 = y3 + 10
        canvas.create_line(x1, y1, x1, y4)
        canvas.create_line(x2, y1, x2, y2)
        canvas.create_line(x2, y2, x3, y2)
        canvas.create_line(x2, y3, x3, y3)
        canvas.create_line(x2, y3, x2, y4)
    elif rn == 8:
        x2 = x1 + 10
        x3 = x2 + 40
        y2 = y1 + 10
        y3 = y2 + 40
        y4 = y3 + 10
        canvas.create_line(x3, y1, x3, y4)
        canvas.create_line(x2, y1, x2, y2)
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x1, y3, x2, y3)
        canvas.create_line(x2, y3, x2, y4)
    elif rn == 9:
        x2 = x1 + 10
        x3 = x2 + 40
        x4 = x3 + 10
        y2 = y1 + 10
        y3 = y2 + 40
        canvas.create_line(x1, y3, x4, y3)
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x2, y1, x2, y2)
        canvas.create_line(x3, y1, x3, y2)
        canvas.create_line(x3, y2, x4, y2)
    elif rn == 10:
        x2 = x1 + 10
        x3 = x2 + 40
        x4 = x3 + 10
        y1 += 10
        y2 = y1 + 40
        y3 = y2 + 10
        canvas.create_line(x1, y1, x4, y1)
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x2, y2, x2, y3)
        canvas.create_line(x3, y2, x3, y3)
        canvas.create_line(x3, y2, x4, y2)
    elif rn == 11:
        x2 = x1 + 10
        x3 = x2 + 40
        x4 = x3 + 10
        y2 = y1 + 10
        y3 = y2 + 40
        y4 = y3 + 10
        canvas.create_line(x2, y1, x2, y2)
        canvas.create_line(x3, y1, x3, y2)
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x3, y2, x4, y2)
        canvas.create_line(x1, y3, x2, y3)
        canvas.create_line(x3, y3, x4, y3)
        canvas.create_line(x2, y3, x2, y4)
        canvas.create_line(x3, y3, x3, y4)
    elif rn == 12:
        x1 += 5
        x2 = x1 + 5
        x3 = x2 + 40
        x4 = x3 + 5
        y1 += 5
        y2 = y1 + 45
        y3 = y2 + 10
        canvas.create_line(x1, y1, x4, y1)
        canvas.create_line(x1, y1, x1, y2)
        canvas.create_line(x4, y1, x4, y2)
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x2, y2, x2, y3)
        canvas.create_line(x3, y2, x4, y2)
        canvas.create_line(x3, y2, x3, y3)
    elif rn == 13:
        x1 += 5
        x2 = x1 + 5
        x3 = x2 + 40
        x4 = x3 + 5
        y2 = y1 + 10
        y3 = y2 + 45
        canvas.create_line(x1, y3, x4, y3)
        canvas.create_line(x1, y2, x1, y3)
        canvas.create_line(x4, y2, x4, y3)
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x2, y1, x2, y2)
        canvas.create_line(x3, y1, x3, y2)
        canvas.create_line(x3, y2, x4, y2)
    elif rn == 14:
        x2 = x1 + 10
        x3 = x2 + 45
        y1 += 5
        y2 = y1 + 5
        y3 = y2 + 40
        y4 = y3 + 5
        canvas.create_line(x1, y2, x2, y2)
        canvas.create_line(x2, y2, x2, y1)
        canvas.create_line(x2, y1, x3, y1)
        canvas.create_line(x3, y1, x3, y4)
        canvas.create_line(x3, y4, x2, y4)
        canvas.create_line(x2, y4, x2, y3)
        canvas.create_line(x2, y3, x1, y3)
    elif rn == 15:
        x1 += 5
        x2 = x1 + 45
        x3 = x2 + 10
        y1 += 5
        y2 = y1 + 5
        y3 = y2 + 40
        y4 = y3 + 5
        canvas.create_line(x3, y2, x2, y2)
        canvas.create_line(x2, y2, x2, y1)
        canvas.create_line(x2, y1, x1, y1)
        canvas.create_line(x1, y1, x1, y4)
        canvas.create_line(x1, y4, x2, y4)
        canvas.create_line(x2, y4, x2, y3)
        canvas.create_line(x2, y3, x3, y3)
    else:
        print("oops")
count = 1
while count < 15:
    for y in range(10, 600, 60):
        for x in range(10, 600, 60):
            draw_room(count, x, y)
            count += 1
            canvas.pack()
            tk.update()
            time.sleep(2)
