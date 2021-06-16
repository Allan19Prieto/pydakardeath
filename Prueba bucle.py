import pygame
import os
import sys
from pygame.locals import *

#Iniciación del Pygame
pygame.init ()

#Pantalla - ventana
W,H = 626, 417
Pantalla = pygame.display.set_mode ((W,H ))
FPS = 60
Reloj = pygame.time.Clock ()
#Fondo del juego
Fondo = pygame.image.load ("img/desert fondo.jpg").convert()
x=0

#Bucle del juego
while True:
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            sys.exit ()
    x_relativa = x % Fondo.get_rect ().width
    Pantalla.blit(Fondo, (x_relativa - Fondo.get_rect ().width, 0))
    if x_relativa < W:
        Pantalla.blit(Fondo,(x_relativa, 0))

    x += 10
    pygame.display.update()
    Reloj.tick (FPS)