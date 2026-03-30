from turtle import *
from time import sleep

t = Turtle()
t.speed(100)

def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()
    t.hideturtle()

def desenha_circulo(x, y, tam, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(tam)
    t.end_fill()
    t.hideturtle()

def desenha_bandeira_polonia():
    desenha_retangulo(-250,125,400,125,'white')
    desenha_retangulo(-250,0,400,125,'red')

desenha_bandeira_polonia()
sleep(3)
t.clear()

def desenha_bandeira_japao():
    desenha_retangulo(-250,125,400,250,'white')
    desenha_circulo(-50,-50,50,'red')

desenha_bandeira_japao()
sleep(3)
t.clear()

def desenha_bandeira_niger():
    desenha_retangulo(-250,125,500,100,'#E05206')
    desenha_retangulo(-250,25,500,100,'white')
    desenha_retangulo(-250,-75,500,100,'#0DB02B')
    desenha_circulo(0,-50,30,'#E05206')

desenha_bandeira_niger()
sleep(3)
t.clear()

def desenha_bandeira_botsuana():
    desenha_retangulo(-250,125,500,120,'#ABCAE9')
    desenha_retangulo(-250,5,500,10,'white')
    desenha_retangulo(-250,-6,500,45,'black')
    desenha_retangulo(-250,-47,500,10,'white')
    desenha_retangulo(-250,-58,500,120,'#ABCAE9')

desenha_bandeira_botsuana()
sleep(3)
t.clear()

def desenha_bandeira_costa_rica():
    desenha_retangulo(-250,125,500,50,'#00205B')
    desenha_retangulo(-250,75,500,50,'white')
    desenha_retangulo(-250,25,500,100,'#EF3340')
    desenha_retangulo(-250,-75,500,50,'white')
    desenha_retangulo(-250,-125,500,50,'#00205B')

desenha_bandeira_costa_rica()
sleep(3)
t.clear()

def desenha_bandeira_monaco():
    desenha_retangulo(-250,125,400,125,'red')
    desenha_retangulo(-250,0,400,125,'white')

desenha_bandeira_monaco()
sleep(3)
t.clear()

def desenha_bandeira_ucrania():
    desenha_retangulo(-250,125,400,125,'#0057B7')
    desenha_retangulo(-250,0,400,125,'#FFDD00')

desenha_bandeira_ucrania()
sleep(3)
t.clear()

def desenha_bandeira_alemanha():
    desenha_retangulo(-250,125,500,100,'black')
    desenha_retangulo(-250,25,500,100,'red')
    desenha_retangulo(-250,-75,500,100,'yellow')

desenha_bandeira_alemanha()
sleep(3)
t.clear()

def desenha_bandeira_russia():
    desenha_retangulo(-250,125,500,100,'white')
    desenha_retangulo(-250,25,500,100,'blue')
    desenha_retangulo(-250,-75,500,100,'red')

desenha_bandeira_russia()
sleep(3)
t.clear()

def desenha_bandeira_holanda():
    desenha_retangulo(-250,125,500,100,'red')
    desenha_retangulo(-250,25,500,100,'white')
    desenha_retangulo(-250,-75,500,100,'blue')

desenha_bandeira_holanda()
sleep(3)
t.clear()

def desenha_bandeira_bulgaria():
    desenha_retangulo(-250,125,500,100,'white')
    desenha_retangulo(-250,25,500,100,'#00966E')
    desenha_retangulo(-250,-75,500,100,'#D62612')

desenha_bandeira_bulgaria()
sleep(3)
t.clear()

color1 = textinput("Escolhar a cor", "Digite a cor desejada:")
color2 = textinput("Escolhar a cor", "Digite a cor desejada:")
color3 = textinput("Escolhar a cor", "Digite a cor desejada:")
def desenha_bandeira_franca():
    desenha_retangulo(-250,125,175,300,color1)
    desenha_retangulo(-75,125,175,300,color2)
    desenha_retangulo(100,125,175,300,color3)

desenha_bandeira_franca()
sleep(3)
t.clear()

def desenha_bandeira_italia():
    desenha_retangulo(-250,125,175,300,'green')
    desenha_retangulo(-75,125,175,300,'white')
    desenha_retangulo(100,125,175,300,'red')

desenha_bandeira_italia()
sleep(3)
t.clear()

def desenha_bandeira_belgica():
    desenha_retangulo(-250,125,175,300,'black')
    desenha_retangulo(-75,125,175,300,'yellow')
    desenha_retangulo(100,125,175,300,'red')

desenha_bandeira_belgica()
sleep(3)
t.clear()

def desenha_bandeira_nigeria():
    desenha_retangulo(-250,125,175,300,'green')
    desenha_retangulo(-75,125,175,300,'white')
    desenha_retangulo(100,125,175,300,'green')

desenha_bandeira_nigeria()
sleep(3)
t.clear()

def desenha_bandeira_irlanda():
    desenha_retangulo(-250,125,175,300,'#169B62')
    desenha_retangulo(-75,125,175,300,'white')
    desenha_retangulo(100,125,175,300,'#FF883E')

desenha_bandeira_irlanda()
sleep(3)
t.clear()

def desenha_bandeira_bangladesh():
    desenha_retangulo(-250,125,400,250,'#006A4E')
    desenha_circulo(-50,-50,50,'#F42A41')

desenha_bandeira_bangladesh()
sleep(3)
t.clear()



mainloop()
    