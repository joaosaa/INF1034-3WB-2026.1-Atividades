from pygame import *

init()
window = display.set_mode((1280, 720))
running = True
clock = time.Clock()

sol_x = 150
nuvem_x = 800
background_color = 0, 221, 255
velocidade_nuvem = 3

while running:
    clock.tick(60)
    
    
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    dt = clock.get_time()/1000
    keys = key.get_pressed()

    if keys[K_d]:
        sol_x = sol_x + 100 * dt
    elif keys[K_a]:
        sol_x = sol_x - 100 * dt

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

