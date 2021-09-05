
from turtle import *
import turtle

t = turtle.Turtle()
def draw_circle(color, radius, x, y):
  t.penup()
  t.fillcolor(color)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  t.pendown()
 
def star():
       t.color('white')
       t.fillcolor('white')
       t.begin_fill()
       for i in range(5):
           t.forward(135)
           t.right(144)
       t.end_fill()

 

def eye():
    t.penup()
    t.width(2)
    draw_circle("#af050f",180, -25, -150)
    draw_circle("white",150, -25, -120)
    draw_circle("#af050f", 110, -26,-80)
    draw_circle("#116cd9", 73, -25, -45)
    
    t.color('#116cd9', 'blue')
    t.pendown()
    
     

eye()

t.goto(-90, 50)
star()
