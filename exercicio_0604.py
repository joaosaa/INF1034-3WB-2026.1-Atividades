from pygame import *
import sys

init()

mixer.init()

flash_img = image.load("flash.png")
flash_img = transform.scale(flash_img, (200, 200))

flash_font = font.Font("FLASH.ttf",50)

mixer.music.load("theflash.mp3")
mixer.music.play(-1)

window = display.set_mode((1280, 720))

window.fill((0, 221, 255))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    #casa
    draw.rect(window, (29, 128, 1), (0, 550, 1500, 300))
    draw.rect(window, (48, 32, 33), (300, 300, 200, 250))
    draw.rect(window, (30, 103, 176), (320, 410, 60, 60))
    draw.rect(window, (105, 46, 17), (400, 410, 75, 140))
    draw.circle(window, (0, 0, 0), (410, 490), 5)
    draw.polygon(window, (153, 63, 14), ((400, 100), (300, 300), (500,300)))

    #sol
    draw.circle(window, (255, 247, 0), (150, 150), 50)
    draw.line(window, (255, 255, 0), (150, 80), (150, 50), 5)
    draw.line(window, (255, 255, 0), (150, 220), (150, 250), 5)
    draw.line(window, (255, 255, 0), (80, 150), (50, 150), 5)
    draw.line(window, (255, 255, 0), (220, 150), (250, 150), 5)
    draw.line(window, (255, 255, 0), (100, 100), (75, 75), 5)
    draw.line(window, (255, 255, 0), (200, 200), (225, 225), 5)
    draw.line(window, (255, 255, 0), (100, 200), (75, 225), 5)
    draw.line(window, (255, 255, 0), (200, 100), (225, 75), 5)

    #árvore
    draw.rect(window, (107, 73, 43), (900, 350, 50, 200))
    draw.circle(window, (13, 128, 20), (925, 330), 100)   

    #núvem
    draw.circle(window, (255, 255, 255), (850, 100), 40)   
    draw.circle(window, (255, 255, 255), (900, 100), 40)  
    draw.circle(window, (255, 255, 255), (950, 100), 40)  
    draw.circle(window, (255, 255, 255), (1000, 100), 40)   
     

    window.blit(flash_img, (600, 355)) 
    flash_text = flash_font.render("I am the fatest", True, (0, 0, 0))
    window.blit(flash_text, (250,20))

    display.update()