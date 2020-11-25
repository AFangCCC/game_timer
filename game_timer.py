import os
import sys
import time
import winsound
import tkinter as tk


class timer_module:
    def __init__(self, window, pos, buttom_name, dur_time=0, text=True, func=None):
        self.start_time = 0
        self.dur_time = dur_time
        self.outside_func = func
        self.iftext = text

        self.buttom_name = buttom_name
        self.text = tk.StringVar()
        self.label = tk.Label(window, textvariable=self.text, bg='lightGray', width=12, height=2)
        self.Button = tk.Button(window, text=self.buttom_name, command=self.funcc, width=12, height=2)

        self.Button.place(x=pos[0], y=pos[1], anchor='nw')
        if text:
            self.text.set("00:00")
            self.label.place(x=pos[0], y=pos[1] + 50, anchor='nw')

    def funcc(self):
        if self.outside_func:
            self.outside_func(self)
        else:
            self.start_time = int(time.time())

    def refreshText(self):
        if self.iftext:
            now_time = int(time.time())
            pass_time = self.start_time + self.dur_time - now_time
            if 1 < pass_time < 3:
                winsound.Beep(2000, 1000)

            if pass_time <= 0:
                self.text.set("00:00")
            else:
                minite = int(pass_time / 60)
                sec = pass_time % 60
                if minite < 10:
                    minite = "0" + str(minite)
                else:
                    minite = str(minite)
                if sec < 10:
                    sec = "0" + str(sec)
                else:
                    sec = str(sec)
                self.text.set(minite + ":" + sec)


def stop_program():
    os._exit(0)
    sys.exit()


def reset_dark(self):
    self.start_time = 0


def pos_generate(win_size="400x300", row=2, column=2, rate=15):
    n = row * column
    width = int(win_size.split('x')[0])
    hight = int(win_size.split('x')[1])
    width = width - width / rate
    hight = hight - hight / rate
    str_x = int(width / rate)
    str_y = int(str_x * (hight / width))
    x = [0] * column
    y = [0] * n
    for i in range(row):
        y[i * column:(i + 1) * column] = [str_y + i * int((hight / row))] * column
    for i in range(column):
        x[i] = str_x + i * int((width / column))
    x = x * row
    return x, y


def dynamic_refresh():
    global timer_list
    for i in timer_list:
        i.refreshText()

    window.after(200, dynamic_refresh)


win_size = '600x300'
row = 2
column = 4
pos_x, pos_y = pos_generate(win_size, row, column)

pos = list(zip(pos_x, pos_y))
button_name_list = ["福利", "彩票", "偷书", "结束", "收租", "除妖", "息屏", "复位"]
dur_time_list = [3600, 3600, 3600, 0, 1800, 1800, 580, 0]
iftext_list = [1, 1, 1, 0, 1, 1, 1, 0]
func_list = [None, None, None, stop_program, None, None, None, None]
timer_list = []

# 循环开始
window = tk.Tk()
window.title('大千世界计时器')
window.geometry(win_size)
for i in range(len(button_name_list)):
    m = timer_module(window, pos[i], button_name_list[i], dur_time_list[i], iftext_list[i], func_list[i])
    timer_list.append(m)

window.after(200, dynamic_refresh)
window.mainloop()