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
    def test_direction(self):
        result = {}
        if self.top == True:
            result['top'] = True
        else:
            result['top'] = False
        if self.bottom == True:
            result['bottom'] = True
        else:
            result['bottom'] = False
        if self.left == True:
            result['left'] = True
        else:
            result['left'] = False
        if self.right == True:
            result['right'] = True
        else:
            result['right'] = False
        return result

    def draw_room(self):
        rn = self.test()
        x1 = self.x * 60
        y1 = self.y * 60
        if rn == 1:
            x1 += 10
            x2 = x1 + 40
            y2 = y1 + 60
            a = canvas.create_line(x1, y1, x1, y2)
            b = canvas.create_line(x2, y1, x2, y2)
            shape = [a, b]
        elif rn == 2:
            x2 = x1 + 60
            y1 += 10
            y2 = y1 + 40
            a = canvas.create_line(x1, y1, x2, y1)
            b = canvas.create_line(x1, y2, x2, y2)
            shape = [a, b]
        elif rn == 3:
            x1 += 10
            x2 = x1 + 40
            y2 = y1 + 10
            x3 = x2 + 10
            y3 = y2 + 40
            a = canvas.create_line(x1, y1, x1, y3)
            b = canvas.create_line(x1, y3, x3, y3)
            c = canvas.create_line(x2, y1, x2, y2)
            d = canvas.create_line(x2, y2, x3, y2)
            shape = [a, b, c, d]
        elif rn == 4:
            x2 = x1 + 10
            x3 = x2 + 40
            y2 = y1 + 10
            y3 = y2 + 40
            a = canvas.create_line(x1, y2, x2, y2)
            b = canvas.create_line(x2, y1, x2, y2)
            c = canvas.create_line(x1, y3, x3, y3)
            d = canvas.create_line(x3, y3, x3, y1)
            shape = [a, b, c, d]
        elif rn == 5:
            x1 += 10
            x2 = x1 + 40
            x3 = x2 + 10
            y1 += 10
            y2 = y1 + 40
            y3 = y2 + 10
            a = canvas.create_line(x1, y1, x1, y3)
            b = canvas.create_line(x1, y1, x3, y1)
            c = canvas.create_line(x2, y2, x3, y2)
            d = canvas.create_line(x2, y2, x2, y3)
            shape = [a, b, c, d]
        elif rn == 6:
            x2 = x1 + 10
            x3 = x2 + 40
            y1 += 10
            y2 = y1 + 40
            y3 = y2 + 10
            a = canvas.create_line(x1, y1, x3, y1)
            b = canvas.create_line(x3, y1, x3, y3)
            c = canvas.create_line(x1, y2, x2, y2)
            d = canvas.create_line(x2, y2, x2, y3)
            shape = [a, b, c, d]
        elif rn == 7:
            x1 += 10
            x2 = x1 + 40
            x3 = x2 + 10
            y2 = y1 + 10
            y3 = y2 + 40
            y4 = y3 + 10
            a = canvas.create_line(x1, y1, x1, y4)
            b = canvas.create_line(x2, y1, x2, y2)
            c = canvas.create_line(x2, y2, x3, y2)
            d = canvas.create_line(x2, y3, x3, y3)
            e = canvas.create_line(x2, y3, x2, y4)
            shape = [a, b, c, d, e]
        elif rn == 8:
            x2 = x1 + 10
            x3 = x2 + 40
            y2 = y1 + 10
            y3 = y2 + 40
            y4 = y3 + 10
            a = canvas.create_line(x3, y1, x3, y4)
            b = canvas.create_line(x2, y1, x2, y2)
            c = canvas.create_line(x1, y2, x2, y2)
            d = canvas.create_line(x1, y3, x2, y3)
            e = canvas.create_line(x2, y3, x2, y4)
            shape = [a, b, c, d, e]
        elif rn == 9:
            x2 = x1 + 10
            x3 = x2 + 40
            x4 = x3 + 10
            y2 = y1 + 10
            y3 = y2 + 40
            a = canvas.create_line(x1, y3, x4, y3)
            b = canvas.create_line(x1, y2, x2, y2)
            c = canvas.create_line(x2, y1, x2, y2)
            d = canvas.create_line(x3, y1, x3, y2)
            e = canvas.create_line(x3, y2, x4, y2)
            shape = [a, b, c, d, e]
        elif rn == 10:
            x2 = x1 + 10
            x3 = x2 + 40
            x4 = x3 + 10
            y1 += 10
            y2 = y1 + 40
            y3 = y2 + 10
            a = canvas.create_line(x1, y1, x4, y1)
            b = canvas.create_line(x1, y2, x2, y2)
            c = canvas.create_line(x2, y2, x2, y3)
            d = canvas.create_line(x3, y2, x3, y3)
            e = canvas.create_line(x3, y2, x4, y2)
            shape = [a, b, c, d, e]
        elif rn == 11:
            x2 = x1 + 10
            x3 = x2 + 40
            x4 = x3 + 10
            y2 = y1 + 10
            y3 = y2 + 40
            y4 = y3 + 10
            a = canvas.create_line(x2, y1, x2, y2)
            b = canvas.create_line(x3, y1, x3, y2)
            c = canvas.create_line(x1, y2, x2, y2)
            d = canvas.create_line(x3, y2, x4, y2)
            e = canvas.create_line(x1, y3, x2, y3)
            f = canvas.create_line(x3, y3, x4, y3)
            g = canvas.create_line(x2, y3, x2, y4)
            h = canvas.create_line(x3, y3, x3, y4)
            shape = [a, b, c, d, e, f, g, h]
        elif rn == 12:
            x1 += 5
            x2 = x1 + 5
            x3 = x2 + 40
            x4 = x3 + 5
            y1 += 5
            y2 = y1 + 45
            y3 = y2 + 10
            a = canvas.create_line(x1, y1, x4, y1)
            b = canvas.create_line(x1, y1, x1, y2)
            c = canvas.create_line(x4, y1, x4, y2)
            d = canvas.create_line(x1, y2, x2, y2)
            e = canvas.create_line(x2, y2, x2, y3)
            f = canvas.create_line(x3, y2, x4, y2)
            g = canvas.create_line(x3, y2, x3, y3)
            shape = [a, b, c, d, e, f, g]
        elif rn == 13:
            x1 += 5
            x2 = x1 + 5
            x3 = x2 + 40
            x4 = x3 + 5
            y2 = y1 + 10
            y3 = y2 + 45
            a = canvas.create_line(x1, y3, x4, y3)
            b = canvas.create_line(x1, y2, x1, y3)
            c = canvas.create_line(x4, y2, x4, y3)
            d = canvas.create_line(x1, y2, x2, y2)
            e = canvas.create_line(x2, y1, x2, y2)
            f = canvas.create_line(x3, y1, x3, y2)
            g = canvas.create_line(x3, y2, x4, y2)
            shape = [a, b, c, d, e, f, g]
        elif rn == 14:
            x2 = x1 + 10
            x3 = x2 + 45
            y1 += 5
            y2 = y1 + 5
            y3 = y2 + 40
            y4 = y3 + 5
            a = canvas.create_line(x1, y2, x2, y2)
            b = canvas.create_line(x2, y2, x2, y1)
            c = canvas.create_line(x2, y1, x3, y1)
            d = canvas.create_line(x3, y1, x3, y4)
            e = canvas.create_line(x3, y4, x2, y4)
            f = canvas.create_line(x2, y4, x2, y3)
            g = canvas.create_line(x2, y3, x1, y3)
            shape = [a, b, c, d, e, f, g]
        elif rn == 15:
            x1 += 5
            x2 = x1 + 45
            x3 = x2 + 10
            y1 += 5
            y2 = y1 + 5
            y3 = y2 + 40
            y4 = y3 + 5
            a = canvas.create_line(x3, y2, x2, y2)
            b = canvas.create_line(x2, y2, x2, y1)
            c = canvas.create_line(x2, y1, x1, y1)
            d = canvas.create_line(x1, y1, x1, y4)
            e = canvas.create_line(x1, y4, x2, y4)
            f = canvas.create_line(x2, y4, x2, y3)
            g = canvas.create_line(x2, y3, x3, y3)
            shape = [a, b, c, d, e, f, g]
        else:
            x2 = x1 + 60
            y2 = y1 + 60
            a = canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='white')
            shape = [a]
        return shape

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

z = 0.67
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
    a = len(map_frame) - 2
    b = len(map_frame[0]) - 2
    shapes = make_array(a, b)
    for y in range(len(map_frame)):
        for x in range(len(map_frame[y])):
            shapes[y][x] = map_frame[y][x].draw_room()
            tk.update()
            time.sleep(0.01)
    return shapes

c = make_map(a, b)
d = draw_map(c)
g = input("Got a pic yet? (y/n) ")
if g == "y":
    pass
else:
    pass
def test_map(frame, shapes):
    set = False
    set_num = 0
    sets = {}
    for y in range(1, len(frame)):
        for x in range(1, len(frame[0])):
            if frame[y][x].top == True or frame[y][x].bottom == True or frame[y][x].left == True or frame[y][x].right == True:
                a = y
                b = x
                print("starting from: ", b, a)
                set = True
                set_num += 1
                set_size = 0
                fork_rooms = []
                counted_rooms = []
                origin_room = {"X":x, "Y":y, "Room":frame[y][x]}
                count = 0
                while set == True:
                    count += 1
                    tk.update()
                    c = frame[a][b].test_direction()
                    t = frame[a - 1][b].test_direction()
                    d = frame[a + 1][b].test_direction()
                    l = frame[a][b - 1].test_direction()
                    r = frame[a][b + 1].test_direction()
                    if c['top'] == True and t['bottom'] == True:
                        #go up
                        if (c['bottom'] == True and d['top'] == True) or (c['left'] == True and l['right'] == True) or (c['right'] == True and r['left'] == True):
                            frame[a][b].top = False
                            frame[a - 1][b].bottom = False
                            fork_rooms.append(frame[a][b])
                            print("Forking at {0} {1} and going Top".format(b, a))
                        else:
                            counted_rooms.append(frame[a][b])
                            frame[a][b] = frame_room
                            frame[a][b].y = a
                            frame[a][b].x = b
                            set_size += 1
                            print("Deleting {0} {1} and going Top".format(b, a))
                            for q in shapes[a][b]:
                                canvas.delete(q)
                        a -= 1
                    elif c['bottom'] == True and d['top'] == True:
                        #go down
                        if (c['left'] == True and l['right'] == True) or (c['right'] == True and r['left'] == True):
                            frame[a][b].bottom = False
                            frame[a + 1][b].top = False
                            fork_rooms.append(frame[a][b])
                            print("Forking at {0} {1} and going Bottom".format(b, a))
                        else:
                            counted_rooms.append(frame[a][b])
                            frame[a][b] = frame_room
                            frame[a][b].y = a
                            frame[a][b].x = b
                            set_size += 1
                            print("Deleting {0} {1} and going Bottom".format(b, a))
                            for q in shapes[a][b]:
                                canvas.delete(q)
                        a += 1
                    elif c['left'] == True and l['right'] == True:
                        #go left
                        if c['right'] == True and r['left'] == True:
                            frame[a][b].left = False
                            frame[a][b - 1].right = False
                            fork_rooms.append(frame[a][b])
                            print("Forking at {0} {1} and going Left".format(b, a))
                        else:
                            counted_rooms.append(frame[a][b])
                            frame[a][b] = frame_room
                            frame[a][b].y = a
                            frame[a][b].x = b
                            set_size += 1
                            print("Deleting {0} {1} and going Left".format(b, a))
                            for q in shapes[a][b]:
                                canvas.delete(q)
                        b -= 1
                    elif c['right'] == True and r['left'] == True:
                        #go right
                        counted_rooms.append(frame[a][b])
                        frame[a][b + 1].left = False
                        frame[a][b] = frame_room
                        frame[a][b].y = a
                        frame[a][b].x = b
                        set_size += 1
                        print("Deleting {0} {1} and going Right".format(b, a))
                        for q in shapes[a][b]:
                            canvas.delete(q)
                        b += 1
                    else:
                        if len(fork_rooms) > 0:
                            #go back to last split and run while again
                            check = False
                            print("Deleting {0} {1} and jumping back".format(b, a))
                            counted_rooms.append(frame[a][b])
                            frame[a][b] = frame_room
                            frame[a][b].y = a
                            frame[a][b].x = b
                            for q in shapes[a][b]:
                                canvas.delete(q)
                            while check == False and len(fork_rooms) > 0:
                                z = fork_rooms.pop()
                                a = z.y
                                b = z.x
                                for g in counted_rooms:
                                    if g.x == z.x and g.y == z.y:
                                        check = False
                                        print("Fork at {0} {1} already counted".format(b, a))
                                        break
                                    else:
                                        check = True


                            else:
                                if check == True:
                                    print("going back to fork at {0} {1}".format(b, a))
                                    set_size += 1
                                elif len(fork_rooms) == 0:
                                    print("Ending")
                                    set_size += 1
                                    sets["Set #{0}".format(set_num)] = set_size
                                    set = False

                        else:
                            print("deleting {0} {1} and ending".format(b, a))
                            counted_rooms.append(frame[a][b])
                            frame[a][b] = frame_room
                            frame[a][b].y = a
                            frame[a][b].x = b
                            for q in shapes[a][b]:
                                canvas.delete(q)
                            set_size += 1
                            sets["Set #{0}".format(set_num)] = set_size
                            set = False
                            #end set
                        tk.update()
                        time.sleep(0.5)
                if set_size > 2:
                    print("How many times set == True ran: ", count)
                    print("set number: ", set_num)
                    print("set size: ", set_size)
                    print("the origin room: ", origin_room)
    for x in sets:
        if sets[x] > 1:
            print(x, sets[x])

test_map(c, d)
g = input("Quit? (y/n) ")
if g == "y":
    pass
else:
    pass
