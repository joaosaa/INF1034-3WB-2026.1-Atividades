from pygame import *

init()
window = display.set_mode((1280, 720))
running = True
clock = time.Clock()

mixer.init()

flash_img = image.load("flash.png")
flash_img = transform.scale(flash_img, (200, 200))

flash_font = font.Font("FLASH.ttf",50)

mixer.music.load("theflash.mp3")
mixer.music.play(-1)

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

    #céu
    window.fill(background_color)
    
    #casa
    draw.rect(window, (29, 128, 1), (0, 550, 1500, 300))
    draw.rect(window, (48, 32, 33), (300, 300, 200, 250))
    draw.rect(window, (30, 103, 176), (320, 410, 60, 60))
    draw.rect(window, (105, 46, 17), (400, 410, 75, 140))
    draw.circle(window, (0, 0, 0), (410, 490), 5)
    draw.polygon(window, (153, 63, 14), ((400, 100), (300, 300), (500,300)))

    #sol
    draw.circle(window, (255, 247, 0), (sol_x, 150), 50)
    draw.line(window, (255, 255, 0), (sol_x, 80), (sol_x, 50), 5)
    draw.line(window, (255, 255, 0), (sol_x, 220), (sol_x, 250), 5)
    draw.line(window, (255, 255, 0), (sol_x - 70, 150), (sol_x - 100, 150), 5)
    draw.line(window, (255, 255, 0), (sol_x + 70, 150), (sol_x + 100, 150), 5)
    draw.line(window, (255, 255, 0), (sol_x - 50, 100), (sol_x -75, 75), 5)
    draw.line(window, (255, 255, 0), (sol_x + 50, 200), (sol_x + 75, 225), 5)
    draw.line(window, (255, 255, 0), (sol_x - 50, 200), (sol_x - 75, 225), 5)
    draw.line(window, (255, 255, 0), (sol_x + 50, 100), (sol_x + 75, 75), 5)

    #árvore
    draw.rect(window, (107, 73, 43), (900, 350, 50, 200))
    draw.circle(window, (13, 128, 20), (925, 330), 100)   

    #núvem
    nuvem_x += velocidade_nuvem


    if nuvem_x <= 20 or nuvem_x >= 1100:
        velocidade_nuvem = -velocidade_nuvem


    draw.circle(window, (255, 255, 255), (nuvem_x, 100), 40)   
    draw.circle(window, (255, 255, 255), (nuvem_x + 50, 100), 40)  
    draw.circle(window, (255, 255, 255), (nuvem_x + 100, 100), 40)  
    draw.circle(window, (255, 255, 255), (nuvem_x + 150, 100), 40)   
     

    window.blit(flash_img, (600, 355)) 
    flash_text = flash_font.render("I am the fatest", True, (0, 0, 0))
    window.blit(flash_text, (250,20))

    display.update()