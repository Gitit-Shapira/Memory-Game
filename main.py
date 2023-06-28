rom functools import partial
from tkinter import *
import random

WINDOW_SIZE = "610x480+300+200"

root = Tk()
root.geometry(WINDOW_SIZE)
root.title("Memory Game")
root.resizable(0, 0)

clicked = []
texts = ["CAR", "CAR", "STAR", "STAR", "SKY", "SKY", "BALL", "BALL",
         "CHILD", "CHILD", "BOTTLE", "BOTTLE", "DOG", "DOG", "SONG", "SONG"]
text_button = dict.fromkeys(range(1, 17))

for i in range(1, 17):
    index = random.randint(0, len(texts) - 1)
    text_button[i] = texts.pop(index)


def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED)


def enable_all_buttons():
    for button in buttons:
        button.config(state=NORMAL)


def labels(button):
    global clicked
    if not button["text"] in range(17):
        button["state"] = "disable"
        return
    text = text_button[int(button["text"])]
    clicked.append((button, button["text"]))
    button["state"] = "disable"
    button["text"] = text
    if len(clicked) == 2:
        disable_all_buttons()


def next():
    enable_all_buttons()
    if len(clicked) == 2:
        if clicked[0][0]["text"] == clicked[1][0]["text"]:
            clicked.clear()
            return
        for i in range(2):
            b = clicked.pop()
            b[0]["state"] = "normal"
            b[0]["text"] = b[1]


buttons = []
for i in range(1, 17):
    widget = Button(root, text=i, width=20, height=5)
    widget.config(command=partial(labels, widget))
    buttons.append(widget)

location = []
for i in range(4):
    for j in range(4):
        location.append((i, j))
for b, l in zip(buttons, location):
    b.grid(row=l[0], column=l[1], sticky=EW, padx=1, pady=5)

next = Button(root, text="next", width=80, height=5, command=next)
next.grid(column=0, columnspan=4, row=4, sticky=EW, padx=1, pady=5)

root.mainloop()
