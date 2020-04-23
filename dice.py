import math
from tkinter import Canvas

from ZONK.colors import Colors


class Dice:
    RADIUS = 10
    LENGTH = 90

    a = [0, 0]
    b = [0, 0]
    c = [0, 0]
    d = [0, 0]
    alpha = 0

    center_dot = [0, 0]
    left_top_dot = [0, 0]
    right_bottom_dot = [0, 0]
    center_right_dot = [0, 0]
    center_left_dot = [0, 0]
    right_top_dot = [0, 0]
    lef_bottom_dot = [0, 0]

    def __init__(self, x, y, angle):
        self.a = self.__get__rotate_coords(x, y, angle)
        self.b = self.__get__rotate_coords(x, y, angle, self.LENGTH, 0)
        self.c = self.__get__rotate_coords(x, y, angle, 0, self.LENGTH)
        self.d = self.__get__rotate_coords(x, y, angle, self.LENGTH, self.LENGTH)
        self.alpha = angle
        self.center_dot = [(self.a[0] + self.b[0] + self.c[0] + self.d[0]) * 0.25,
                           (self.a[1] + self.b[1] + self.c[1] + self.d[1]) * 0.25]
        self.left_top_dot = self.__get__rotate_coords(self.a[0], self.a[1], angle, self.LENGTH * 0.25,
                                                      self.LENGTH * 0.25)
        self.right_bottom_dot = self.__get__rotate_coords(self.a[0], self.a[1], angle, self.LENGTH * 0.75,
                                                          self.LENGTH * 0.75)
        self.right_top_dot = self.__get__rotate_coords(self.a[0], self.a[1], angle, self.LENGTH * 0.75,
                                                       self.LENGTH * 0.25)
        self.lef_bottom_dot = self.__get__rotate_coords(self.a[0], self.a[1], angle, self.LENGTH * 0.25,
                                                        self.LENGTH * 0.75)
        self.center_right_dot = self.__get__rotate_coords(self.a[0], self.a[1], angle, self.LENGTH * 0.75,
                                                          self.LENGTH * 0.5)
        self.center_left_dot = self.__get__rotate_coords(self.a[0], self.a[1], angle, self.LENGTH * 0.25,
                                                         self.LENGTH * 0.5)

    def draw(self, canvas: Canvas, value):
        canvas.create_polygon(self.a[0], self.a[1], self.b[0], self.b[1], self.d[0], self.d[1], self.c[0], self.c[1],
                              fill=Colors.BLACK)
        if value == 1 or value == 3 or value == 5:
            self.__draw_point(canvas, self.center_dot)
        if value == 2 or value == 3 or value == 5 or value == 4 or value == 6:
            self.__draw_point(canvas, self.left_top_dot)
            self.__draw_point(canvas, self.right_bottom_dot)
        if value == 4 or value == 5 or value == 6:
            self.__draw_point(canvas, self.right_top_dot)
            self.__draw_point(canvas, self.lef_bottom_dot)
        if value == 6:
            self.__draw_point(canvas, self.center_left_dot)
            self.__draw_point(canvas, self.center_right_dot)

    def __get__rotate_coords(self, rotate_point_x, rotate_point_y, alpha, delta_x=0.0, delta_y=0.0):
        return [rotate_point_x + delta_x * math.cos(to_rad(alpha)) - delta_y * math.sin(to_rad(alpha)),
                rotate_point_y + delta_y * math.cos(to_rad(alpha)) + delta_x * math.sin(to_rad(alpha))]

    def __draw_point(self, canvas: Canvas, dot):
        canvas.create_oval(dot[0] - self.RADIUS, dot[1] - self.RADIUS, dot[0] + self.RADIUS, dot[1] + self.RADIUS,
                           fill=Colors.WHITE)


def to_rad(degree):
        return degree * math.pi / 180
