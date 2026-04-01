from turtle import *
from time import sleep

t = Turtle()
t.speed(0)

def plano_cartesiano():
    t.pu()
    t.goto(-300, 0)
    t.pd()
    t.goto(300, 0)
    t.stamp()
    t.pu()
    t.goto(0, -300)
    t.pd()
    t.setheading(90)
    t.goto(0, 300)
    t.stamp()
    t.setheading(0)
    t.hideturtle()

def f_raiz(x):
    return x ** 0.5

def f_inversa(x):
    return 1 / x

def f_exp(x):
    return 2 ** x

def f_p1(x):
    return 5 - (x ** 2)

def f_p2(x):
    return (x ** 2) - (5 * x) + 6

def f_cubica(x):
    return (x ** 3) - (x ** 2) - x + 1

def funcao_raiz():
    plano_cartesiano()
    t.color("red")
    t.pu()
    for x in range(0, 150):
        x = x / 10
        y = f_raiz(x)
        t.goto(x * 20, y * 20)
        t.pd()


funcao_raiz()
sleep(2)
t.clear()

def funcao_inversa():
    plano_cartesiano()
    t.color("blue")
    t.pu()
    for i in range(-100, -1):
        x = i / 10
        y = f_inversa(x)
        t.goto(x * 20, y * 50)
        t.pd()
    t.pu()
    for i in range(1, 101):
        x = i / 10
        y = f_inversa(x)
        t.goto(x * 20, y * 50)
        t.pd()

funcao_inversa()
sleep(2)
t.clear()

def funcao_exponencial():
    plano_cartesiano()
    t.color("green")
    t.pu()
    for x in range(-50, 50):
        x = x / 10
        y = f_exp(x)
        t.goto(x * 20, y * 20)
        t.pd()

funcao_exponencial()
sleep(2)
t.clear()

def funcao_parabola1():
    plano_cartesiano()
    t.color("yellow")
    t.pu()
    for x in range(-100, 101):
        x = x / 10
        y = f_p1(x)
        t.goto(x * 20, y * 20)
        t.pd()

funcao_parabola1()
sleep(2)
t.clear()

def funcao_parabola2():
    plano_cartesiano()
    t.color("orange")
    t.pu()
    for x in range(-100, 101):
        x = x / 10
        y = f_p2(x)
        t.goto(x * 20, y * 20)
        t.pd()

funcao_parabola2()
sleep(2)
t.clear()

def funcao_cubica():
    plano_cartesiano()
    t.color("black")
    t.pu()
    for x in range(-50, 51):
        x = x / 10
        y = f_cubica(x)
        t.goto(x * 20, y * 20)
        t.pd()

funcao_cubica()
sleep(2)

mainloop()