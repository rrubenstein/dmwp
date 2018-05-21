import time
import random
from tkinter import *
import sys

a = int(input("How many rooms wide? "))
b = int(input("How many rooms tall? "))
x = a * 60 + 120
y = b * 60 + 120
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
#each room will be 60 units so that is a ten by ten grid
canvas = Canvas(tk, width=x, height=y)
canvas.pack()
tk.update()

class Room(object):
    def __init__(self, top, bottom, left, right, monster, player, treasure, x, y):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.monster = monster
        self.player = player
        self.treasure = treasure
        self.x = x
        self.y = y

    def test(self):
        if self.top == True:
            if self.bottom == True:
                if self.left == True:
                    if self.right == True:
                        result = 11
                    else:
                        result = 8
                else:
                    if self.right == True:
                        result = 7
                    else:
                        result = 1
            else:
                if self.left == True:
                    if self.right == True:
                        result = 9
                    else:
                        result = 4
                else:
                    if self.right == True:
                        result = 3
                    else:
                        result = 13
        else:
            if self.bottom == True:
                if self.left == True:
                    if self.right == True:
                        result = 10
                    else:
                        result = 6
                else:
                    if self.right == True:
                        result = 5
                    else:
                        result = 12
            else:
                if self.left == True:
                    if self.right == True:
                        result = 2
                    else:
                        result = 14
                else:
                    if self.right == True:
                        result = 15
                    else:
                        if self.monster == True:
                            result = 0
                        else:
                            result = 16
        return result

    def draw_room(self):
        rn = self.test()
        x1 = self.x * 60
        y1 = self.y * 60
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

frame_room = Room(False, False, False, False, True, False, False, 0, 0)
rooms = Room(True, True, True, True, False, False, False, 0, 0)

def make_array(max_x, max_y):
    array = []
    for x in range(max_y + 2):
        array.append([frame_room])
    for y in range(1, max_y + 1):
        for x in range(1, max_x + 1):
            array[y].append(rooms)
    for x in range(max_y + 1):
        array[x].append(frame_room)
    for x in range(max_x + 1):
        array[len(array) - 1].append(frame_room)
    for x in range(max_x):
        array[0].append(frame_room)
    return array

z = 0.65
def make_map(max_x, max_y):
    map_frame = make_array(max_x, max_y)
    for y in range(len(map_frame)):
        for x in range(len(map_frame[y])):
            if map_frame[y][x] != frame_room:
                if map_frame[y - 1][x].bottom == False:
                    if map_frame[y][x - 1].right == False:
                        if map_frame[y][x + 1].left == False:
                            if map_frame[y + 1][x].top == False:
                                map_frame[y][x] = Room(False, False, False, False, False, False, False, x, y)
                            else:
                                ynb = 0.01 * float(random.randint(1, 100))
                                if ynb <= z:
                                    map_frame[y][x] = Room(False, True, False, False, False, False, False, x, y)
                                else:
                                    map_frame[y][x] = Room(False, False, False, False, False, False, False, x, y)
                        else:
                            ynr = 0.01 * float(random.randint(1, 100))
                            if map_frame[y + 1][x].top == False:
                                if ynr <= z:
                                    map_frame[y][x] = Room(False, False, False, True, False, False, False, x, y)
                                else:
                                    map_frame[y][x] = Room(False, False, False, False, False, False, False, x, y)
                            else:
                                ynd = 0.01 * float(random.randint(1, 100))
                                if ynr <= z:
                                    if ynd <= z:
                                        map_frame[y][x] = Room(False, True, False, True, False, False, False, x, y)
                                    else:
                                        map_frame[y][x] = Room(False, False, False, True, False, False, False, x, y)
                                else:
                                    if ynd <= z:
                                        map_frame[y][x] = Room(False, True, False, False, False, False, False, x, y)
                                    else:
                                        map_frame[y][x] = Room(False, False, False, False, False, False, False, x, y)
                    else:
                        if map_frame[y][x + 1].left == False:
                            if map_frame[y + 1][x].top == False:
                                map_frame[y][x] = Room(False, False, True, False, False, False, False, x, y)
                            else:
                                ynb = 0.01 * float(random.randint(1, 100))
                                if ynb <= z:
                                    map_frame[y][x] = Room(False, True, True, False, False, False, False, x, y)
                                else:
                                     map_frame[y][x] = Room(False, False, True, False, False, False, False, x, y)
                        else:
                            ynr = 0.01 * float(random.randint(1, 100))
                            if map_frame[y + 1][x].top == False:
                                if ynr <= z:
                                    map_frame[y][x] = Room(False, False, True, True, False, False, False, x, y)
                                else:
                                    map_frame[y][x] = Room(False, False, True, False, False, False, False, x, y)
                            else:
                                ynd = 0.01 * float(random.randint(1, 100))
                                if ynr <= z:
                                    if ynd <= z:
                                        map_frame[y][x] = Room(False, True, True, True, False, False, False, x, y)
                                    else:
                                        map_frame[y][x] = Room(False, False, True, True, False, False, False, x, y)
                                else:
                                    if ynd <= z:
                                        map_frame[y][x] = Room(False, True, True, False, False, False, False, x, y)
                                    else:
                                        map_frame[y][x] = Room(False, False, True, False, False, False, False, x, y)
                else:
                    if map_frame[y][x - 1].right == False:
                        if map_frame[y][x + 1].left == False:
                            if map_frame[y + 1][x].top == False:
                                map_frame[y][x] = Room(True, False, False, False, False, False, False, x, y)
                            else:
                                ynb = 0.01 * float(random.randint(1, 100))
                                if ynb <= z:
                                    map_frame[y][x] = Room(True, True, False, False, False, False, False, x, y)
                                else:
                                    map_frame[y][x] = Room(True, False, False, False, False, False, False, x, y)
                        else:
                            ynr = 0.01 * float(random.randint(1, 100))
                            if map_frame[y + 1][x].top == False:
                                if ynr <= z:
                                    map_frame[y][x] = Room(True, False, False, True, False, False, False, x, y)
                                else:
                                    map_frame[y][x] = Room(True, False, False, False, False, False, False, x, y)
                            else:
                                ynd = 0.01 * float(random.randint(1, 100))
                                if ynr <= z:
                                    if ynd <= z:
                                        map_frame[y][x] = Room(True, True, False, True, False, False, False, x, y)
                                    else:
                                        map_frame[y][x] = Room(True, False, False, True, False, False, False, x, y)
                                else:
                                    if ynd <= z:
                                        map_frame[y][x] = Room(True, True, False, False, False, False, False, x, y)
                                    else:
                                        map_frame[y][x] = Room(True, False, False, False, False, False, False, x, y)
                    else:
                        if map_frame[y][x + 1].left == False:
                            if map_frame[y + 1][x].top == False:
                                map_frame[y][x] = Room(True, False, True, False, False, False, False, x, y)
                            else:
                                ynb = 0.01 * float(random.randint(1, 100))
                                if ynb <= z:
                                    map_frame[y][x] = Room(True, True, True, False, False, False, False, x, y)
                                else:
                                    map_frame[y][x] = Room(True, False, True, False, False, False, False, x, y)
                        else:
                            ynr = 0.01 * float(random.randint(1, 100))
                            if map_frame[y + 1][x] == 1 or map_frame[y + 1][x].top == False:
                                if ynr <= z:
                                    map_frame[y][x] = Room(True, False, True, True, False, False, False, x, y)
                                else:
                                    map_frame[y][x] = Room(True, False, True, False, False, False, False, x, y)
                            else:
                                ynd = 0.01 * float(random.randint(1, 100))
                                if ynr <= z:
                                    if ynd <= z:
                                        map_frame[y][x] = Room(True, True, True, True, False, False, False, x, y)
                                    else:
                                        map_frame[y][x] = Room(True, False, True, True, False, False, False, x, y)
                                else:
                                    if ynd <= z:
                                        map_frame[y][x] = Room(True, True, True, False, False, False, False, x, y)
                                    else:
                                        map_frame[y][x] = Room(True, False, True, False, False, False, False, x, y)
    return map_frame
def draw_map(map_frame):
    for y in range(len(map_frame)):
        for x in range(len(map_frame[y])):
            map_frame[y][x].draw_room()
            tk.update()
            time.sleep(0.1)

c = make_map(a, b)
draw_map(c)
time.sleep(7)
