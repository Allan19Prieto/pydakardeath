import pygame
from pygame.locals import *

class Player():
    def __init__(self, pantalla, x, y, ruta):
        self.pantalla = pantalla
        self.x = x
        self.y = y
        self.tupla = (self.x, self.y)
        self.ruta = ruta
        self.vel = 3
        self.car_image = pygame.image.load(self.ruta)
        #self.player = player
        #self.pos = pos

    # Funcion para mapear la tecla que ha sido precionada
    def tecla(self, tecla, player):
        tecla_map = {'acelera': [K_UP, K_w], 'freno': [K_DOWN, K_s], \
                        'izquierda': [K_LEFT, K_a], 'derecha': [K_RIGHT, K_d]}
        if player == 0:
            return tecla_map[tecla][0]
        return tecla_map[tecla][1]

    def draw(self):
        self.pantalla.blit(self.car_image, self.tupla)

    def getpos(self):
        return self.x,self.y


    def move(self, movimineto, player):

        # Teclas que se usaran para que el carro se mueva
        self.acelerar, self.freno = self.tecla('acelera', player), self.tecla('freno', player)
        self.izquirda, self.derecha = self.tecla('izquierda', player), self.tecla('derecha', player)

        #keys = pygame.key.get_pressed()

        if movimineto[self.izquirda]:
            self.x -= self.vel

        if movimineto[self.derecha]:
            self.x += self.vel

        if movimineto[self.acelerar]:
            self.y -= self.vel

        if movimineto[self.freno]:
            self.y += self.vel

        self.update()

    def update(self):
        #self.rect = (self.x, self.y, self.width, self.height)
        #self.x = self.x, self.y = self.y
        self.tupla = (self.x, self.y)
