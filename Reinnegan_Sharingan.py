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
t.color('#c9b4bc', 'blue')

def eye():
    draw_circle("Black",700, -22, -150)
    draw_circle("#c9b4bc", 695, -22, -145)
    draw_circle("Black",600, -22, -60)
    draw_circle("#c9b4bc", 595, -22, -55)
    draw_circle("Black",500, -22, 20)
    draw_circle("#c9b4bc", 495, -22, 25)
    draw_circle("Black",400, -22, 110)
    draw_circle("#c9b4bc", 395, -22, 115)
    draw_circle("Black",300, -22, 200)
    draw_circle("#c9b4bc", 295, -22, 205)
    draw_circle("Black",200, -22, 300)
    draw_circle("#c9b4bc", 195, -22, 305)
    draw_circle("black",100, -22, 400)
    draw_circle("#987e88", 95, -22, 405)
    draw_circle("black", 30, -22, 475)
 

    t.color('Black', 'blue')

    draw_circle("Black",25, -32, 385)
    t.color('#c9b4bc', 'blue')
    draw_circle("#c9b4bc", 25, -40, 385)
    t.color('Black', 'blue')
    draw_circle("Black",27, -36, 390)

    draw_circle("Black",25, 80, 500)
    t.color('#c9b4bc', 'blue')
    draw_circle("#c9b4bc", 25, 82, 490)
    t.color('Black', 'blue')
    draw_circle("Black",27,76 , 490)

    draw_circle("Black",25, -102, 547)
    t.color('#c9b4bc', 'blue')
    draw_circle("#c9b4bc", 25, -102, 555)
    t.color('Black', 'blue')
    draw_circle("Black",27, -94,547)



    draw_circle("Black",25, 120, 333)
    t.color('#c9b4bc', 'blue')
    draw_circle("#c9b4bc", 25, 112, 325)
    t.color('Black', 'blue')
    draw_circle("Black",27, 108, 330)

    draw_circle("Black",25, -215, 443)
    t.color('#c9b4bc', 'blue')
    draw_circle("#c9b4bc", 25, -218, 453)
    t.color('Black', 'blue')
    draw_circle("Black",27, -208, 452)

    draw_circle("Black",22, 20, 688)
    t.color('#c9b4bc', 'blue')
    draw_circle("#c9b4bc", 25, 24, 675)
    t.color('Black', 'blue')
    draw_circle("Black",27, 18, 670)
    turtle.hideturtle()


if __name__ == '__main__':
    screensize(12000, 10000, "#f0f0f0")
    turtle.Screen().bgcolor("#c9b4bc")
  
    pensize(3)
    speed(9)
    eye()
