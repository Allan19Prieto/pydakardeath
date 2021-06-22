import pygame
import os
import sys
import random
from pygame.locals import *
from Clases import *

#Iniciación del Pygame
pygame.init ()

#Pantalla - ventana
W,H = 1361, 716
win = pygame.display.set_mode ((W,H ))
window_rect = win.get_rect()
FPS = 20
Reloj = pygame.time.Clock ()
Rojo = (255,0,0)
pos_x = 300
pos_y = 260
#Fondo del juego
Fondo = Image("img", "Desert fond.jpg", (W, H), win, window_rect)
x=0

#Bucle del juego
while True:
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            sys.exit ()
    obstacles = []
    #def redrawWindow():
        #win.blit(bg, (bgX, 0))
        #win.blit(bg, (bgX2, 0))
        #runner.draw(win)
        #pygame.display.update()


    pygame.time.set_timer(USEREVENT + 1, 500)
    pygame.time.set_timer(USEREVENT + 2, 3000)
    speed = 30

    # Loops through all obstacles
#        for obstacle in obstacles:
           # bgX -= 10
           # bgX2 -= 10
           # if bgX < bg.draw.rect.get_width() * -1:
           #     bgX = bg.draw.rect.get_width()
           # if bgX2 < bg.draw.rect.get_width() * -1:
           #     bgX2 = bg.draw.rect.get_width()
           # if event.type == USEREVENT + 2:
           #     r = random.randrange(0, 2)
           #     if r == 0:
           #         obstacles.append(saw(810, 310, 64, 64))
           #     elif r == 1:
           #         obstacles.append(spike(810, 0, 48, 310))
            # obstacle.draw(win)
    pygame.draw.rect(win, Rojo, (pos_x, pos_y, 40, 40))
    #pygame.time.set_timer(USEREVENT + 2, random.randrange(2000, 3500))
# Lógica
    pos_x += 5
    if pos_x > W:
        pos_x = 0

#Dibujos
    x_relativa = x % Fondo.rect.width
    win.blit(Fondo.image, (x_relativa - Fondo.rect.width, 0))
    if x_relativa < W:
        win.blit(Fondo.image,(x_relativa, 0))
        pygame.draw.rect(win, Rojo, (pos_x, pos_y, 40, 40))


#Constantes
    x -= 10
    Reloj.tick(FPS)

    pygame.display.update()

    #pygame.time.delay ()