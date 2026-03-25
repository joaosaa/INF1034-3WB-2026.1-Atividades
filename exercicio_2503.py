from turtle import *

t = Turtle()
from random import randint

def desenha_retafrente(x,y,tamanho):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fd(tamanho)
    t.stamp()

desenha_retafrente(-300,0,600)

def desenha_retacima(x,y,tamanho):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.lt(90)
    t.fd(tamanho)
    t.stamp()
    
desenha_retacima(0,-300,600)

def desenha_triangulo(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.fd(tamanho)
        t.lt(120)
    t.end_fill()

color = textinput("Escolhar a cor", "Digite a cor desejada:")
x= randint(100, 200)
y= randint(100, 200)
desenha_triangulo(x,y,100,color)

def desenha_losango(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(tamanho)
        t.lt(60)
        t.fd(tamanho)
        t.lt(120)
    t.end_fill()

color = textinput("Escolhar a cor", "Digite a cor desejada:")
x= randint(-200,0)
y=randint(0,200)
desenha_losango(x,y,100,color)

def desenha_hexagono(x,y,tamanho,color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(6):
        t.fd(tamanho)  
        t.rt(60) 
    t.end_fill()

color = textinput("Escolhar a cor", "Digite a cor desejada:")
x= randint(-200,-100)
y=randint(-300,-100)
desenha_hexagono(x,y,70,color)

def desenha_octogono(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(8):
        t.fd(tamanho)
        t.rt(45)
    t.end_fill()

color = textinput("Escolhar a cor", "Digite a cor desejada:")
x= randint(100,200)
y=randint(-300,-100)
desenha_octogono(x,y,50,color)



mainloop()