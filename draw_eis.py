#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys

from turtle import *

width = 16
height = 11
edge_len = 30
debug_centering = 0
invisible_turtle = 1


def triangle_lr():
    down()
    for i in range(3):
        forward(edge_len)
        left(120)
    up()
    forward(edge_len)


def triangle_rl():
    down()
    for i in range(3):
        forward(edge_len)
        right(120)
    up()
    forward(edge_len)


def draw_from_left_to_right():
    for j in range(width):
        triangle_lr()
    right(60)
    forward(edge_len)
    right(120)


def draw_from_right_to_left():
    for j in range(width):
        triangle_rl()
    left(60)
    forward(edge_len)
    left(120)


def stop_code(*argv):
    onclick(None)
    sys.exit(0)


def make_skos_travel():
    skos_steps = height + 1
    left(60)
    for i in range(skos_steps):
        forward(edge_len)
    right(60)


def make_horiz_travel():
    dst_pos = width / 2
    if debug_centering:
        tmp_format = 'dst_pos'; print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
    horiz_pos = (height) / 2
    if debug_centering:
        tmp_format = 'horiz_pos'; print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
    difference = dst_pos - horiz_pos
    if debug_centering:
        tmp_format = 'difference'; print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
    step_count = abs(difference)
    if debug_centering:
        tmp_format = 'step_count'; print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
    for i in range(int(step_count)):
        if difference > 0:
            forward(edge_len)
            if debug_centering:
                print("forward")
        else:
            backward(edge_len)
            if debug_centering:
                print("backward")


def move_to_center():
    if debug_centering:
        down()
        color("green")
    make_skos_travel()
    make_horiz_travel()


def draw_axes():
    move_to_center()
    color("red")
    for i in range(4):
        if 1:
            horiz_len = edge_len * int(width / 2)
            down()
            forward(horiz_len)
            up()
            backward(horiz_len)
            left(90)
        if 1:
            vert_len = edge_len * height
            down()
            forward(vert_len)
            up()
            backward(vert_len)
            left(90)


def draw_omega():
    color("magenta")
    down()
    left(120)
    forward(edge_len)
    up()


def main():
    onclick(stop_code)
    speed(0)
    if invisible_turtle:
        hideturtle()
    up()
    back(300)
    left(90)
    forward(300)
    right(90)
    down()
    for k in range(height):
        draw_from_left_to_right()
        draw_from_right_to_left()
    draw_axes()
    draw_omega()
    if invisible_turtle:
        showturtle()
    print("Click on turtle to exit from program.")
    mainloop()


main()
