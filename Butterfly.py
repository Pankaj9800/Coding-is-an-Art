import turtle
from turtle import *


def draw_circle(color, radius,x,y,s):
  t.penup()
  t.goto(x,y)
  t.left(s)
  t.fillcolor(color,)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()


def draw_circle1(color, radius,x,y,s):
  t.penup()
  t.goto(x,y)
  t.right(s)
  t.fillcolor(color,)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()


def draw_circle0(color, radius,x,y):
  t.penup()
  t.goto(x,y)
  t.fillcolor(color,)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

t = turtle.Turtle()
turtle .bgcolor("black")
turtle .pensize(2)
turtle .speed(9)
draw_circle("yellow",100,-40,40,5)

n=100
turtle.left(60)
x=-20
y=50
s=4

for i in range(1):
    n=100
    for colors in ["#0513a3","#0b1dd0","#293bee","#4251e0","#124bb3","#2564d7","#3d78e3","#299de8","#52ade8","#52e2e8","#6bdfe4","#19ebbb","#45f0c9","#45f09b","#45f067","#0ceb16","#28f131","#50eb0c","#99f53b","#bff53b","#cade06","#d6e91e","#e1f23c","#c2b605","#e4d822"]:
        draw_circle(colors,n,x,y,s)
        n=n-4
    n=100
    x=-100
    y=-35
    draw_circle("yellow",100,-100,-10,5)
    for colors in ["#0513a3","#0b1dd0","#293bee","#4251e0","#124bb3","#2564d7","#3d78e3","#299de8","#52ade8","#52e2e8","#6bdfe4","#19ebbb","#45f0c9","#45f09b","#45f067","#0ceb16","#28f131","#50eb0c","#99f53b","#bff53b","#cade06","#d6e91e","#e1f23c","#c2b605","#e4d822"]:
        draw_circle1(colors,n,x,y,s) 
        n=n-4
    draw_circle("#d3f505",20,-90,190,4)
    draw_circle("#9cb505",15,-90,190,4)
    draw_circle("#daf44d",10,-90,190,4)
    draw_circle("#171b01",5,-90,190,4)
    n=70
    x=110
    y=60
    s=7
    for colors in ["#e4a422","#de6b06","#de5206","#de3506","#f7400e","#f7250e","#f70e36","#af0202","#e70404","#bf141c"]:
        draw_circle(colors,n,x,y,s) 
        n=n-7
    draw_circle1("#d3f505",20,-260,-30,4)
    draw_circle1("#9cb505",15,-260,-30,4)
    draw_circle1("#daf44d",10,-260,-30,4)
    draw_circle1("#171b01",5,-260,-30,4)
    n=70
    x=-100
    y=-160
    for colors in  ["#e4a422","#de6b06","#de5206","#de3506","#f7400e","#f7250e","#f70e36","#af0202","#e70404","#bf141c"]:
        draw_circle1(colors,n,x,y,s)  
        n=n-7

    penup()
    draw_circle0("#042b53",20,-100,20)
    draw_circle0("#115193",15,-100,25)
    draw_circle0("#176abf",10,-100,30)


    draw_circle1("#0e0118",50,-45,-65,s)
    draw_circle1("#2b0449",45,-50,-60,s)
    draw_circle1("#450774",40,-55,-55,s)
    draw_circle1("#580894",35,-55,-50,s)  
    draw_circle1("#6e0cb8",30,-55,-45,s)
    draw_circle1("#8419d5",25,-55,-40,s)
    draw_circle1("#9436db",20,-55,-35,s)
    draw_circle1("#9c3be6",15,-55,-30,s)  
    draw_circle1("#9436db",10,-50,-25,s)


