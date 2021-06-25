import json
import pygame
from pygame.draw import rect

BLACK = (0, 0, 0)
from Ejemplo_json import h

pygame.surface.Surface(size=(500, 500))
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont("comicsans", 30)
f = open("archivojson.json")
data = json.load(f)
text = str(h["Jugador"] + h["Puntuacion"])

text = font.render("Jugador", 1, (255, 255, 255))
text = font.render("Puntuacion", 1, (255, 255, 255))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, BLACK))
    pygame.draw.rect()
    pygame.display.flip()

pygame.font.quit()
