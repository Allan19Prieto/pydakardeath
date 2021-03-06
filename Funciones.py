#import csv
import pygame
from pygame.image import load
import os
from pygame.locals import *

#Fuentes
#Crea una ruta a una imagen, que esté en assets/sprites
def load_sprite(name, with_alpha=True):
    #arquivo = os.path.join('img', arquivo)
    path = "img"
    #Carga la imagen usando load
    loaded_sprite = load(path)

    #Convierte la imagen en un formato que se adapte mejor a la pantalla
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

# La función del puntaje
def muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y, consolas, puntuacion, red):
    tipo_letra = pygame.font.Font(fuente, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)
    muestra_texto(pantalla, consolas, str(puntuacion), red, 40, 700, 50)


def cargar_imagem(arquivo, transparencia=None, imagens=None):

    arquivo = os.path.join('botones', arquivo)
    image = pygame.image.load(arquivo)

    if imagens is None:
        if transparencia == 1:
            return image.convert_alpha()

        return image.convert()
    else:
        imgs = []
        for img_area in imagens:
            img = pygame.Surface(Rect(img_area).size).convert()
            img.blit(image, (0, 0), img_area)
            if transparencia == 1:
                colorkey = img.get_at((0, 0))
                img.set_colorkey(colorkey, RLEACCEL)
            imgs.append(img)
        return imgs


