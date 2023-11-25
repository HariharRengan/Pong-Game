import pygame
import random
import tkinter as tk
from tkinter import simpledialog

pygame.init()

wix = 800
wiy = 600

win = pygame.display.set_mode((wix, wiy))
pygame.display.set_caption("Pong")

x = 5
y = wiy / 2
width = 20
height = 80
vel = 5

bx = wix / 2
by = wiy / 2
bwidth = 30
bheight = 30
bvel = 4

score = 0

pygame.draw.rect(win, (255, 255, 255), (bx, by, bwidth, bheight))
pygame.display.update()
normal = ["by += bvel", "by -= bvel"][random.randint(0, 1)]
normalx = "bx -= bvel"

root = tk.Tk()
root.withdraw()
name = simpledialog.askstring("Input", "Enter your name:")

run = True
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < wiy - width - vel:
        y += vel

    if bx < bvel:
        run = False
    if bx > wix - bwidth - bvel:
        normalx = "bx -= bvel"
        score += 1
        bvel += 0.05

    if by < bvel:
        normal = "by += bvel"
    elif by > wiy - bwidth - bvel:
        normal = "by -= bvel"

    exec(normal)

    win.fill((0, 0, 0))
    paddle = pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    ball = pygame.draw.rect(win, (255, 255, 255), (bx, by, bwidth, bheight))
    pygame.display.update()

    collide = paddle.collidepoint((bx, by))
    if collide:
        normalx = "bx += bvel"
    exec(normalx)

pygame.quit()

with open('highscores.txt', 'r') as f:
    lines = f.readlines()
    uname, uscore = lines

if not lines or int(lines[1]) < score:
    with open('highscores.txt', 'w') as f:
        f.write(name + '\n' + str(score))
        uname, uscore = name, score

tk.messagebox.showinfo(title="Score", message="Your score is " + str(score) + ".")
tk.messagebox.showinfo(title="Highscore", message="The highscore is " + str(uscore) + " by " + str(uname) + ".")
