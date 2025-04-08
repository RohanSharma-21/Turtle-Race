import turtle
import random

font = ("Arial", 30, "bold")
tom = turtle.Turtle()
wm = turtle.Screen()
wm.setup(735,450)
tom.speed(0)
tom.penup()
tom.goto(-140,140)
for label in range(17):
  tom.write(label,align="center")
  tom.right(90)
  tom.forward(10)
  tom.pendown()
  tom.forward(150)
  tom.penup()
  tom.backward(160)
  tom.left(90)
  tom.forward(20)

max = turtle.Turtle()
max.color("red")
max.shape("turtle")
max.penup()
max.goto(-160,100)
max.pendown()

rohan = turtle.Turtle()
rohan.color("blue")
rohan.shape("turtle")
rohan.penup()
rohan.goto(-160,70)
rohan.pendown()

sam = turtle.Turtle()
sam.color("yellow")
sam.shape("turtle")
sam.penup()
sam.goto(-160,40)
sam.pendown()

harry = turtle.Turtle()
harry.color("green")
harry.shape("turtle")
harry.penup()
harry.goto(-160,10)
harry.pendown()



for turn in range(100):
  max.forward(random.randint(2,5))
  rohan.forward(random.randint(2,5))
  harry.forward(random.randint(2,5))
  sam.forward(random.randint(2,5))

winner = ""
if max.xcor() > rohan.xcor():
  if max.xcor() > sam.xcor():
    if max.xcor() > harry.xcor():
      winner = "Max"
    else:
      winner = "Harry"
  else:
    winner = "Sam"
else:
  winner = "Rohan"



tom.goto(-190,-100)
tom.write("The winner is " + winner, font=font)



 
