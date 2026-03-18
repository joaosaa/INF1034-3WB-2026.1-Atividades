from turtle import *

t = Turtle()

t.pu()
t.goto(-300,0)
t.lt(180)
t.lt(180)
t.pd()
t.goto(300,0)
t.stamp()
t.pu()
t.goto(0,-300)
t.lt(270)
t.lt(180)
t.pd()
t.goto(0,300)
t.stamp()

t.pu()
t.goto(200,100)
t.pd()
color = textinput("obter cor", "escolha uma cor")
t.begin_fill()
t.fillcolor(color)
for _ in range(3):
    t.fd(100)
    t.lt(120)
t.end_fill()

t.pu()
t.goto(-100,100)
t.pd()
color = textinput("obter cor", "escolha uma cor")
t.begin_fill()
t.fillcolor(color)
for _ in range(2):
    t.fd(100)
    t.lt(60)
    t.fd(100)
    t.lt(120)
t.end_fill()

mainloop()
