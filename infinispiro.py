
##############################################
#imports!
import turtle
import random
import time

#setting window options
wn = turtle.Screen()
wn.bgcolor("#49E496")
wn.title("Catch me if you can!")

#sets turtle options
s = turtle.Turtle()
s.color("#8D099A")
s.shape("turtle")

#sets turtle starting pos
s.penup()
s.goto(-50,0)
s.pendown()
##########################################
#a bit more turtle maneuver prep...
#tells the turtle to start moving!
go = True
#turtle's default speed is 3, this is a list of possible speeds that the turtle can be each loop!
#rSpeed = random.randrange(1,11)
#randomizes the turtle's color for each loop
#rColor = random.choice(["#8D099A", "#9A097A", "#58099A", "#47099A", "#9A0947", "#9A093A"])
################################################
#Turtle onclick func
def turtstop(x, y):
    global go
    go = False
################################################
#It's go time!
s.onclick(turtstop)
s.forward(350)
while go == True:
    rSpeed = random.randrange(4, 9)
    s.speed(rSpeed)
    rColor = random.choice(["#8D099A", "#9A097A", "#58099A", "#47099A", "#9A0947", "#9A093A"])
    s.color(rColor)
    s.left(161)
    s.forward(350)

if go == False:
    a = turtle.Turtle()
    a.penup()
    a.goto(-250,-200)
    a.write("You got me!")

time.sleep(3)
turtle.exitonclick()