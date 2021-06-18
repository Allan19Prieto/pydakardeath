import pygame
import os
import sys
import random
from pygame.locals import *

#Iniciación del Pygame
pygame.init ()

#Pantalla - ventana
W,H = 626, 417
Pantalla = pygame.display.set_mode ((W,H ))
FPS = 20
Reloj = pygame.time.Clock ()
Rojo = (255,0,0)
pos_x = 300
pos_y = 260
#Fondo del juego
Fondo = pygame.image.load ("img/Desert fond.jpg").convert()
x=0

#Bucle del juego
while True:
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            sys.exit ()
    obstacles = []
    def redrawWindow():
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2, 0))
        runner.draw(win)
        pygame.display.update()


    pygame.time.set_timer(USEREVENT + 1, 500)
    pygame.time.set_timer(USEREVENT + 2, 3000)
    speed = 30

    # Loops through all obstacles
        for obstacle in obstacles:
            bgX -= 10
            bgX2 -= 10
            if bgX < bg.draw.rect.get_width() * -1:
                bgX = bg.draw.rect.get_width()
            if bgX2 < bg.draw.rect.get_width() * -1:
                bgX2 = bg.draw.rect.get_width()
            if event.type == USEREVENT + 2:
                r = random.randrange(0, 2)
                if r == 0:
                    obstacles.append(saw(810, 310, 64, 64))
                elif r == 1:
                    obstacles.append(spike(810, 0, 48, 310))
            # obstacle.draw(win)
    pygame.draw.rect(Pantalla, Rojo, (pos_x, pos_y, 40, 40))
    pygame.time.set_timer(USEREVENT + 2, random.randrange(2000, 3500))
# Lógica



    pos_x += 5
    if pos_x > W:
        pos_x = 0


#Dibujos

    x_relativa = x % Fondo.get_rect().width
    Pantalla.blit(Fondo, (x_relativa - Fondo.get_rect().width, 0))
    if x_relativa < W:
        Pantalla.blit(Fondo,(x_relativa, 0))
        pygame.draw.rect(Pantalla, Rojo, (pos_x, pos_y, 40, 40))


#Constantes
    x -= 10
    Reloj.tick(FPS)

    pygame.display.update()

    #pygame.time.delay ()