from turtle import *

t = Turtle()

# Desenhando um quadrado
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)

# Para evitar a linha
t.pu()
t.goto(200, 300)
t.pd()

# Da pra fazer mais rapido?
t.color("red")
t.begin_fill()
t.fillcolor("blue")
for _ in range(4):
    t.fd(100)
    t.lt(90)
t.end_fill()

# Começo do plano cartesiano
t.color("blue")
t.pu()
t.goto(0, 0)
t.pd()

t.fd(300)
t.stamp()
t.pu()
t.goto(0, 300)
t.pd()

color = textinput("obter cor", "Digite a cor desejada")
t.begin_fill()
t.fillcolor(color)

t.circle(50)
t.end_fill()

mainloop()

