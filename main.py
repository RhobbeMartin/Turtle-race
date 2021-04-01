import turtle
import random

cameraMan = turtle.Turtle()
cameraMan.shape("triangle")

cameraMan.penup()
cameraMan.goto(-175, 140)
cameraMan.speed(0)

for i in range(16):
  cameraMan.write(i)
  cameraMan.right(90)
  cameraMan.forward(20)
  cameraMan.pendown()
  cameraMan.forward(200)
  cameraMan.left(180)
  cameraMan.penup()
  cameraMan.forward(220)
  cameraMan.right(90)
  cameraMan.forward(20)
cameraMan.hideturtle()

celine = turtle.Turtle()
celine.color("red")
celine.shape("turtle")
celine.penup()
celine.goto(-200, 100)

Rhobbe = turtle.Turtle()
Rhobbe.color("#000000")
Rhobbe.shape("turtle")
Rhobbe.penup()
Rhobbe.goto(-200, 60)

sonic = turtle.Turtle()
sonic.color("blue")
sonic.shape("turtle")
sonic.penup()
sonic.goto(-200, 20)

zoro = turtle.Turtle()
zoro.color("green")
zoro.shape("turtle")
zoro.penup()
zoro.goto(-200, -20)

luffy = turtle.Turtle()
luffy.color("orange")
luffy.shape("turtle")
luffy.penup()
luffy.goto(-200, -60)

celine.pendown()
Rhobbe.pendown()
sonic.pendown()
zoro.pendown()
luffy.pendown()

for i in range(40):
  celine.forward(random.randint(1,15))
  Rhobbe.forward(random.randint(1,15))
  sonic.forward(random.randint(1,15))
  zoro.forward(random.randint(1,15))
  luffy.forward(random.randint(1,15))
