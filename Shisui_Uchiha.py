from turtle import *
import turtle

t = turtle.Turtle()
def draw_circle(color, radius, x, y):
  t.penup()
  t.fillcolor(color,)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  t.pendown()

t = turtle.Turtle()
t.color('red', 'blue')

def eye():
    
    draw_circle("Black",210, -22, -150)
    draw_circle("Red", 196, -20, -135)
  
if __name__ == '__main__':
    screensize(8000, 6000, "#f0f0f0")
    turtle.Screen().bgcolor("#dceaf6")
  
    pensize(3)
    speed(5)
    eye()
    t.penup()
    t.goto(-40,-135)
    t.fillcolor('BLACK')
    t.color('red', 'black')
    t.begin_fill()
    t.goto(90,40)
    t.goto(170,40)
    t.goto(10,170)
    t.goto(20,250)
    t.goto(-140,90)
    t.goto(-210,90)
    t.goto(-50,-60)
    t.end_fill()
    t.pendown()

    draw_circle("red",50,-20,10)
    draw_circle("black",15,-20,40)





    
 
