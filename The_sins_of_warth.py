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
 

t = turtle.Turtle()
t.color('#090909', '#090909')

def drawRectangle_1(x,y,width,height,s):
    t.penup()
    
    t.fillcolor("#faf1f1")
    t.begin_fill()
    t.goto(x,y) 
    t.left(s)
    t.forward(width)  
    t.left(90)       
    t.forward(height)   
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.pendown()

def triangle(x,y,length,base,height,s):
    t.penup()
    t.begin_fill()
    t.goto(x,y) 
    t.left(s)
    t.forward(base)
    t.left(30)
    t.forward(height)
    t.left(30)
    t.forward(base)
    t.left(30)
    t.end_fill()
    t.pendown()
def eye():
  
    draw_circle("#faf1f1",150, 20, -200)
    draw_circle("#090909",140, 20, -190)

    draw_circle("#faf1f1",30, 130, 15)

    
    draw_circle("#faf1f1",10,60,15)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,65,25)
    draw_circle("#faf1f1",10,70,25)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,75,35)
    drawRectangle_1(55,20,30,55,-55)
    
    draw_circle("#faf1f1",10,115,115)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,110,105)
    draw_circle("#faf1f1",10,110,100)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,105,90)
    

    drawRectangle_1(120,72,30,55,45)

    draw_circle("#090909",15, 125, 35)
    draw_circle("#faf1f1",7, 125, 45)
  
    draw_circle("#faf1f1",10,180,5)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,185,0)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, 150, -20)
    draw_circle("#090909",18, 150, -15)
    draw_circle("#faf1f1",7, 150, -5)

    draw_circle("#faf1f1",10,190,-60)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,195,-65)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, 160, -80)
    draw_circle("#090909",18, 160, -75)
    draw_circle("#faf1f1",7, 165, -65)

    draw_circle("#faf1f1",10,170,-140)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,165,-145)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, 140, -140)
    draw_circle("#090909",18, 140, -135)
    draw_circle("#faf1f1",7, 145, -125)

    draw_circle("#faf1f1",10,120,-200)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,115,-205)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, 100, -190)
    draw_circle("#090909",18, 100, -185)
    draw_circle("#faf1f1",7, 105, -180)

    draw_circle("#faf1f1",10,45,-225)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,38,-225)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, 40, -215)
    draw_circle("#090909",18, 40, -210)
    draw_circle("#faf1f1",7, 45, -200)

    draw_circle("#faf1f1",10,-25,-225)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,-35,-225)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, -20, -215)
    draw_circle("#090909",18, -20, -210)
    draw_circle("#faf1f1",7, -15, -205)

    draw_circle("#faf1f1",10,-90,-185)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,-95,-180)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, -80, -180)
    draw_circle("#090909",18, -80, -175)
    draw_circle("#faf1f1",7, -80, -165)

    draw_circle("#faf1f1",10,-145,-120)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,-150,-115)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, -120, -125)
    draw_circle("#090909",18, -120, -120)
    draw_circle("#faf1f1",7, -120, -115)

    draw_circle("#faf1f1",10,-150,-55)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,-155,-50)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, -130, -60)
    draw_circle("#090909",18, -130, -55)
    draw_circle("#faf1f1",7, -130, -50)

    draw_circle("#faf1f1",10,-125,40)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,-120,45)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, -100, 10)
    draw_circle("#090909",18, -100, 15)
    draw_circle("#faf1f1",7, -95, 25)

    draw_circle("#faf1f1",10,-35,100)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,-25,105)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, -30, 60)
    draw_circle("#090909",18, -30, 65)
    draw_circle("#faf1f1",7, -30, 75)

    draw_circle("#faf1f1",10,55,105)
    t.color('#090909', 'blue')
    draw_circle("#090909",10,65,105)
    t.color('#faf1f1', 'blue')
    draw_circle("#faf1f1",25, 55, 60)
    draw_circle("#090909",18, 55, 65)
    draw_circle("#faf1f1",7, 55, 75)
    #turtle.hideturtle()


if __name__ == '__main__':
    screensize(8000, 6000, "#090909")
    turtle.Screen().bgcolor("#090909")
    chris = turtle.Turtle()
  
    pensize(3)
    speed(9)
    eye()
    
    
 
