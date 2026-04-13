from pygame import *

init()
window = display.set_mode((1280, 720))
running = True
clock = time.Clock()

nuvem_x = 800
background_color = 0, 221, 255

while running:
    clock.tick(60)
    
    
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    dt = clock.get_time()/1000
    nuvem_x = nuvem_x + 100 * dt
    if nuvem_x > 1100:
        nuvem_x = nuvem_x + -200 * dt

    window.fill(background_color)

    draw.circle(window, (255, 255, 255), (nuvem_x, 100), 40)   
    draw.circle(window, (255, 255, 255), (nuvem_x + 50, 100), 40)  
    draw.circle(window, (255, 255, 255), (nuvem_x + 100, 100), 40)  
    draw.circle(window, (255, 255, 255), (nuvem_x + 150, 100), 40) 
    
    display.update()

