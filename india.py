import turtle
from turtle import *
import time 
bgcolor("lightblue")
i=450
j=900
def A():
    speed(5999)
    penup()
    left(40)
    goto(-400,650)
    pendown()
    left(50)
    pendown()
    pensize(4)
    speed(10)
    left(180)
    forward(70)
    backward(70)
    left(-180)
    #forward(500)
    #orange
    color("orange")
    pensize(4)
    pencolor("black")
    begin_fill()
    right(90)
    forward(780)
    right(90)
    forward(i)  # flag height
    right(90)
    forward(780)
    end_fill()
    #white
    color("white")
    pencolor("black")
    begin_fill()
    left(90)
    forward(i)
    left(90)
    forward(780)
    left(90)
    forward(i)
    end_fill()
    #
    pencolor("black")
    left(90)
    forward(780)
    left(90)
    forward(j)
    #green
    color("green")
    pencolor("black")
    begin_fill()
    left(90)
    forward(780)
    left(90)
    # circle move
    forward(i)
    left(90)
    forward(780)
    end_fill()
    right(90)
    forward(i)
    right(90)
    # flag position
    forward(220)

    
  
  
      
def flag():
	speed(500)
	goto(-220,110)
	left(46.6)
	pendown()
	pensize(4)
	speed(10)
	left(180)
	forward(70)
	backward(70)
	left(-180)
	#forward(500)
#orange
	color("orange")
	pensize(4)
	pencolor("black")
	begin_fill()
	right(90)
	forward(450)
	right(90)
	forward(70)#flag hight
	right(90)
	forward(450)
	end_fill()
	right(90)
	forward(70)
	right(90)
	forward(450)
	right(90)
	forward(70)
	right(90)
	forward(450)
#white
	color("white")
	pencolor("black")
	begin_fill()
	left(90)
	forward(70)
	left(90)
	forward(450)
	left(90)
	forward(70)
	end_fill()
#
	pencolor("black")
	left(90)
	forward(450)
	left(90)
	forward(140)
#green
	color("green")
	pencolor("black")
	begin_fill()
	left(90)
	forward(450)
	left(90)
#circle move
	forward(70)
	left(90)
	forward(450)
	end_fill()
	right(90)
	forward(70)
	right(90)
	#flag position
	forward(220)
#circle
	speed(100)
	pencolor("blue")
	pensize(2)
	right(90)
	forward(46)

	pendown()
	for i in range(1,30):
		right(180)
		forward(45)
		left(90)
		circle(25,20)
		left(85)
		forward(45)
	#penup()
#	goto(10,10)
#	pendown()

    

def heart():
    pensize(17)
    speed(10000)
    penup()
    #goto(-10,200)
    color("red")
    begin_fill()
    penup()
    goto (-30,129)
    
    left(100)
    circle(200,20)
    circle(120,150)
    circle(440,71)
    pendown()
    speed(5)
    #circle start from here 
    #second circle
  #  for i in range(30):
   # speed(1000)
    left(40)
    penup()
    circle(440,0)
    pendown()
    circle(440,71)
    circle(130,80)
    circle(200,60)
    right(105)
    circle(200,60)
    circle(130,80)
    circle(440,75)
    speed(900)
    left(40)
    circle(450,21)
    speed(2)
    a=position()
    print(a)
    end_fill()
    penup()
    
   

    
    
A()
heart()
flag()
#turtle.clear()




time.sleep(1000)