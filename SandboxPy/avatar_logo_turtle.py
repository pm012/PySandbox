from turtle import *
import tkinter as tk

speed(0)
bgcolor('blue')
color('yellow')
hideturtle()
n = 1
p = True

while True:
    circle(n)
    if p:
        n = n - 1
    else:
        n = n + 1
    if n == 0 or n == 60:
        p = not p
    left(1)
    forward(3)
