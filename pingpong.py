import turtle as t

w = t.Turtle()
w.hideturtle()
w.color("red")
p = t.Turtle()
p.hideturtle()
p.color("white")
p.pu()
p.setpos(0,300)
n = 0

padspeed = 30
t.bgcolor("black")
t.speed(0)
t.pu()
t.setpos(-350,-350)
t.pd()
t.pencolor("white")
for i in range(4):
    t.fd(700)
    t.lt(90)

t.pu()
t.setpos(0,-250)
t.shape("square")
t.color("white")
t.shapesize(1,5)



def padr():
    x = t.xcor()
    y = t.ycor()
    x += padspeed
    t.setpos(x,y)
    if x>=300 or x<=-300:
        t.setx(300)

def padl():
    x = t.xcor()
    y = t.ycor()
    x -= padspeed
    t.setpos(x,y)
    if x>=300 or x<=-300:
        t.setx(-300)

t.listen()
t.onkey(padr,"Right")
t.onkey(padl,"Left")

bsx = 10
bsy = 8
ball = t.Turtle()
ball.shape("circle")
ball.color("green")
ball.seth(60)
ball.pu()
bx = ball.xcor()
by = ball.ycor()
while True:
    bx += bsx
    by += bsy
    ball.setpos(bx,by)
    if by == t.ycor()+10 and t.xcor()-50<bx<t.xcor()+50: bsy*=-1; n+=1;p.clear()
    if bx>=300 or bx<=-300: bsx *= -1
    if by>=300 or by<=-300: bsy *= -1
    if by<=-250: w.write("Game Over",move=False,align="center",font=("Arail",64,"normal"));break
    p.write("Point: %d"%n,False,"center",("Arail",16,"normal"))





    
    
    



    
