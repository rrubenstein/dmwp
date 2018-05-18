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

class Room(object):
    def __init__(self, top, bottom, left, right, monster, player, treasure x, y):
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
        result = {"top":0, "bottom":0, "left":0, "right":0}

        if self.top == True:
            result["top"] = True
        else:
            result["top"] = False

        if self.bottom == True:
            result["bottom"] = True
        else:
            result["bottom"] = False

        if self.left == True:
            result["left"] = True
        else:
            result["left"] = False

        if self.right == True:
            result["right"] = True
        else:
            result["right"] = False

        return result

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

frame_room = Room(False, False, False, False, False, False, False, 0, 0)
rooms = Room(True, True, True, True, False, False, False, 0, 0)
def make_map():
    map_frame = [
    [[frame_room], [frame_room], [frame_room], [frame_room], [frame_room], [frame_room], [frame_room], [frame_room]],
    [[frame_room], [rooms], [rooms], [rooms], [rooms], [rooms], [rooms], [frame_room]],
    [[frame_room], [rooms], [rooms], [rooms], [rooms], [rooms], [rooms], [frame_room]],
    [[frame_room], [rooms], [rooms], [rooms], [rooms], [rooms], [rooms], [frame_room]],
    [[frame_room], [rooms], [rooms], [rooms], [rooms], [rooms], [rooms], [frame_room]],
    [[frame_room], [rooms], [rooms], [rooms], [rooms], [rooms], [rooms], [frame_room]],
    [[frame_room], [rooms], [rooms], [rooms], [rooms], [rooms], [rooms], [frame_room]],
    [[frame_room], [frame_room], [frame_room], [frame_room], [frame_room], [frame_room], [frame_room], [frame_room]]
    ]

    for y in range(len(map_frame)):
        for x in range(len(map_frame[y])):
            if map_frame[y - 1][x].bottom == False:
                if map_frame[y][x - 1].right == False:
                    if map_frame[y][x + 1].left == False:
                        if map_frame[y + 1][x].top == False:
                            print("no connections")
                            map_frame[y][x] = Room(False, False, False, False, False, False, False, x, y)
                        else:
                            ynb = 0.01 * float(random.randint(1, 100))
                            if ynb <= 0.85:
                                map_frame[y][x] = Room(False, True, False, False, False, False, False, x, y)
                                print("one connection: down")
                            else:
                                map_frame[y][x] = Room(False, False, False, False, False, False, False, x, y)
                                print("no connections (tried down)")
                    else:
                        ynr = 0.01 * float(random.randint(1, 100))
                        if map_frame[y + 1][x].top == False:
                            if ynr <= 0.85:
                                map_frame[y][x] = Room(False, False, False, True, False, False, False, x, y)
                                print("one connection: right")
                            else:
                                map_frame[y][x] = Room(False, False, False, False, False, False, False, x, y)
                                print("No connections (tried right)")
                        else:
                            ynd = 0.01 * float(random.randint(1, 100))
                            if ynr <= 0.85:
                                if ynd <= 0.85:
                                    map_frame[y][x] = Room(False, True, False, True, False, False, False, a, b)
                                    print("two connections: bottom, right")
                                else:
                                    map_frame[y][x] = Room(False, False, False, True, False, False, False, x, y)
                                    print("one connection: right (tried bottom)")
                            else:
                                if ynd <= 0.85:
                                    map_frame[y][x] = Room(False, True, False, False, False, False, False, x, y)
                                    print("one connection: bottom (tried right)")
                                else:
                                    map_frame[y][x] = Room(False, False, False, False, False, False, False, x, y)
                                    print("no connections (tried bottom, right)")
                else:
                    if map_frame[y][x + 1].left == False:
                        if map_frame[y + 1][x].top == False:
                            map_frame[y][x] = Room(False, False, True, False, False, False, False, x, y)
                            print("one connection: left")
                        else:
                            ynb = 0.01 * float(random.randint(1, 100))
                            if ynb <= 0.85:
                                map_frame[y][x] = Room(False, True, True, False, False, False, False, x, y)
                                print("two connection: down, left")
                            else:
                                map_frame[y][x] = Room(False, False, True, False, False, False, False, x, y)
                                print("one connection: left (tried down)")
                    else:
                        ynr = 0.01 * float(random.randint(1, 100))
                        if map_frame[y + 1][x].top == False:
                            if ynr <= 0.85:
                                map_frame[y][x] = Room(False, False, True, True, False, False, False, x, y)
                                print("two connection: left, right")
                            else:
                                map_frame[y][x] = Room(False, False, True, False, False, False, False, x, y)
                                print("one connection: left (tried right)")
                        else:
                            ynd = 0.01 * float(random.randint(1, 100))
                            if ynr <= 0.85:
                                if ynd <= 0.85:
                                    map_frame[y][x] = Room(False, True, True, True, False, False, False, x, y)
                                    print("three connections: bottom, left, right")
                                else:
                                    map_frame[y][x] = Room(False, False, True, True, False, False, False, x, y)
                                    print("two connection: left, right (tried bottom)")
                            else:
                                if ynd <= 0.85:
                                    map_frame[y][x] = Room(False, True, True, False, False, False, False, x, y)
                                    print("two connection: left, bottom (tried right)")
                                else:
                                    map_frame[y][x] = Room(False, False, True, False, False, False, False, x, y)
                                    print("one connection: left (tried bottom, right)")
            else:
                if map_frame[y][x - 1].right == False:
                    if map_frame[y][x + 1].left == False:
                        if map_frame[y + 1][x].top == False:
                            print("one connection: top")
                            map_frame[y][x] = Room(True, False, False, False, False, False, False, x, y)
                        else:
                            ynb = 0.01 * float(random.randint(1, 100))
                            if ynb <= 0.85:
                                map_frame[y][x] = Room(True, True, False, False, False, False, False, x, y)
                                print("two connection: top, bottom")
                            else:
                                map_frame[y][x] = Room(True, False, False, False, False, False, False, x, y)
                                print("one connection: top (tried down)")
                    else:
                        ynr = 0.01 * float(random.randint(1, 100))
                        if map_frame[y + 1][x].top == False:
                            if ynr <= 0.85:
                                map_frame[y][x] = Room(True, False, False, True, False, False, False, x, y)
                                print("two connections: top, right")
                            else:
                                map_frame[y][x] = Room(True, False, False, False, False, False, False, x, y)
                                print("one connection: top (tried right)")
                        else:
                            ynd = 0.01 * float(random.randint(1, 100))
                            if ynr <= 0.85:
                                if ynd <= 0.85:
                                    map_frame[y][x] = Room(True, True, False, True, False, False, False, x, y)
                                    print("three connections: top, bottom, right")
                                else:
                                    map_frame[y][x] = Room(True, False, False, True, False, False, False, x, y)
                                    print("two connections: top, right (tried bottom)")
                            else:
                                if ynd <= 0.85:
                                    map_frame[y][x] = Room(True, True, False, False, False, False, False, x, y)
                                    print("two connections: top, bottom (tried right)")
                                else:
                                    map_frame[y][x] = Room(True, False, False, False, False, False, False, x, y)
                                    print("one connection: top (tried bottom, right)")
                else:
                    if map_frame[y][x + 1].left == False:
                        if map_frame[y + 1][x].top == False:
                            map_frame[y][x] = Room(True, False, True, False, False, False, False, x, y)
                            print("two connections: top, left")
                        else:
                            ynb = 0.01 * float(random.randint(1, 100))
                            if ynb <= 0.85:
                                map_frame[y][x] = Room(True, True, True, False, False, False, False, x, y)
                                print("three connections: top, down, left")
                            else:
                                map_frame[y][x] = Room(True, False, True, False, False, False, False, x, y)
                                print("two connections: top, left (tried down)")
                    else:
                        ynr = 0.01 * float(random.randint(1, 100))
                        if map_frame[y + 1][x] == 1 or map_frame[y + 1][x].top == False:
                            if ynr <= 0.85:
                                map_frame[y][x] = Room(True, False, True, True, False, False, False, x, y)
                                print("three connections: top, left, right")
                            else:
                                map_frame[y][x] = Room(True, False, True, False, False, False, False, x, y)
                                print("two connections: top, left (tried right)")
                        else:
                            ynd = 0.01 * float(random.randint(1, 100))
                            if ynr <= 0.85:
                                if ynd <= 0.85:
                                    map_frame[y][x] = Room(True, True, True, True, False, False, False, x, y)
                                    print("four connections: top, bottom, left, right")
                                else:
                                    map_frame[y][x] = Room(True, False, True, True, False, False, False, x, y)
                                    print("three connection: top, left, right (tried bottom)")
                            else:
                                if ynd <= 0.85:
                                    map_frame[y][x] = Room(True, True, True, False, False, False, False, x, y)
                                    print("three connection: top, left, bottom (tried right)")
                                else:
                                    map_frame[y][x] = Room(True, False, True, False, False, False, False, x, y)
                                    print("two connections: top, left (tried bottom, right)")
