import random
from tkinter import *
import zonk_scores_calculator
from dice import Dice, Colors


def kill_proccess():
    exit(0)


class Zonk:
    canvas = None
    score_label = None
    score_txt = None
    width = 0
    height = 0
    scores_calculator = zonk_scores_calculator.ScoresCalculator()
    value_list = [0, 0, 0, 0, 0, 0]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        window = Tk()
        window.geometry(str(width) + "x" + str(height + 300))
        window.title("Sn1cKa's ZONK")

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.create_rectangle(0, 0, width, height, fill=Colors.YELLOW)
        self.canvas.pack(side=TOP)

        frame = Frame(window, width=width, height=30)
        frame.pack()
        self.score_txt = StringVar(frame)
        self.score_txt.set("0 scores")
        self.score_label = Label(frame, textvariable=self.score_txt)
        throw_button = Button(frame, text="Throw", width=10, command=self.throw_bones)
        close_button = Button(frame, text="Close", width=10, command=kill_proccess)

        self.score_label.pack()
        throw_button.pack()
        close_button.pack()

        window.mainloop()

    def throw_bones(self):
        self.value_list = [0, 0, 0, 0, 0, 0]
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill=Colors.YELLOW)
        bones_count = random.randint(1, 6)
        for i in range(bones_count):
            self.create_bone_on_canvas(i - 1, self.canvas)
        self.score_txt.set(str(self.scores_calculator.calculate_points(self.value_list)) + " scores")

    def create_bone_on_canvas(self, i, canvas):
        a = random.randint(90, 510)
        b = random.randint(90, 510)
        angle = random.randint(0, 360)
        value = random.randint(1, 6)
        dice = Dice(a, b, angle)
        dice.draw(canvas, value)
        self.value_list[i] = value
