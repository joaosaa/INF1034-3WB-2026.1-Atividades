from pygame import *
import sys

init()

batman_img = image.load("batman.png")
batman_img = transform.scale(batman_img, (200,200))

batman_font = font.Font("BATMAN.ttf",50)

mixer.music.load("batman_1990.mp3")
mixer.music.play(-1)

window = display.set_mode((1280, 720))

window.fill((0, 221, 255))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    draw.rect(window, (255,0, 0), (200, 300, 100, 50))
    draw.circle(window, (255,0, 255), (500, 600), 200)
    draw.polygon(window, (255,0, 0), ((200, 300), (250, 150), (300,300)))
    draw.line(window, (255, 0, 255), (100, 100), (200, 200), 3)

    window.blit(batman_img, (0, 0))

    batman_text = batman_font.render("I am Batman", True, (0, 0, 0))
    window.blit(batman_text, (100,400))

    display.update()