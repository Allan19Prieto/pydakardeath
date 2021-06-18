import pygame

AZUL2 = (64, 64, 255)
NEGRO = (0, 0, 0)

class Jugador(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/car1.png").convert()
        self.image.set_colorkey(AZUL2)
        self.rect = self.image.get.rect()
        self.rect.center = (200, 200)
        self.velocidad_x = 0
        self.velocidad_y = 0


class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("img/tiro.png").convert(),(10, 20))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get.rect()
        self.rect.bottom = y
        self.centerx = x

    def update(self):
        self.rect.x += 25
        if self.rect.bottom < 0:
            self.kill()

