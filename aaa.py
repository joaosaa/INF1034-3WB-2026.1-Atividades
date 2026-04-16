from pygame import *

init()
window = display.set_mode((1280, 720))
running = True
clock = time.Clock()

sol_x = 150
nuvem_x = 800
velocidade_nuvem = 3
modo_fundo = False

uuu=255
iii=188
ooo=99
background_color = (uuu, iii, ooo)

modo_mouse = False

aaa = (uuu-(600//5.75))
bbb = (iii+(600//25))
ccc = (ooo+(600//3.95))

while running:
    clock.tick(60)
    key_pressed = key.get_pressed()

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False

        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                modo_fundo = not modo_fundo
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_x:
                modo_mouse = not modo_mouse


        if ev.type == MOUSEBUTTONDOWN:
            if sol_x >0 and sol_x < 430 and modo_fundo == False:
                if ev.button == 2:
                    baby1.play()

        if ev.type == MOUSEBUTTONDOWN:
            if sol_x >430 and sol_x < 860 and modo_fundo == False:
                if ev.button == 2:
                    baby2.play()

        if ev.type == MOUSEBUTTONDOWN:
            if sol_x >860 and sol_x < 1350 and modo_fundo == False:
            #if background_color == (13, 29, 92):
                if ev.button == 2:
                    baby3.play()

        if ev.type == MOUSEBUTTONDOWN:
            if modo_fundo == True:
                if ev.button == 2:
                    feijao.play()

        if modo_fundo:
            background_color = (245,178,64)
        else:
                if modo_mouse == False:
                    if sol_x < 600:
                        background_color = (uuu-(sol_x)//5.75, iii+(sol_x//25), ooo+(sol_x//3.95))
                    else:
                        if sol_x >= 600:
                            background_color = (aaa-((sol_x-600)//5), bbb-((sol_x-600)//4.3), ccc-((sol_x-600)//4.5))
                else:
                    if modo_mouse == True:
                        if sol_x < 600:
                            background_color = (uuu-(sol_x)//5.75, iii+(sol_x//25), ooo+(sol_x//3.95))
                        else:
                            if sol_x >= 600:
                                background_color = (aaa-((sol_x-600)//5), bbb-((sol_x-600)//4.3), ccc-((sol_x-600)//4.5))

        dt = clock.get_time()/1000
    keys = key.get_pressed()

    mouse_x, mouse_y = mouse.get_pos()



    #teclas

    if modo_mouse == True:
        sol_x = (mouse_x)


    #if modo_mouse == False:
    if sol_x<1350:
        if keys[K_d]:
                sol_x = sol_x + 100 *dt
    if sol_x > 10:
        if keys[K_a]:
                sol_x = sol_x - 100 *dt
    if sol_x <1350:
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                sol_x = sol_x + 100 *dt
    if sol_x > -50:
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 3:
                sol_x = sol_x - 100 *dt

    window.fill(background_color)

    draw.circle(window, (255, 247, 0), (sol_x, 150), 50)
    draw.line(window, (255, 255, 0), (sol_x, 80), (sol_x, 50), 5)
    draw.line(window, (255, 255, 0), (sol_x, 220), (sol_x, 250), 5)
    draw.line(window, (255, 255, 0), (sol_x - 70, 150), (sol_x - 100, 150), 5)
    draw.line(window, (255, 255, 0), (sol_x + 70, 150), (sol_x + 100, 150), 5)
    draw.line(window, (255, 255, 0), (sol_x - 50, 100), (sol_x -75, 75), 5)
    draw.line(window, (255, 255, 0), (sol_x + 50, 200), (sol_x + 75, 225), 5)
    draw.line(window, (255, 255, 0), (sol_x - 50, 200), (sol_x - 75, 225), 5)
    draw.line(window, (255, 255, 0), (sol_x + 50, 100), (sol_x + 75, 75), 5)



    
    display.update()
