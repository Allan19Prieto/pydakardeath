import pygame
from network import Network
from player import Player
import pickle
from Clases import *
import time
import Ejemplo_json as js

pygame.font.init()
width = 1361
height = 716
FPS = 60
Reloj = pygame.time.Clock ()
win = pygame.display.set_mode((width, height))
window_rect = win.get_rect()
pygame.display.set_caption("Client")
Fondo = Image("img", "Desert fond.jpg", (width, height), win, window_rect)
#text = ""
#snInicio = pygame.mixer.Sound('sounds/go.wav')

x = 0
contador = 0
players = []
menu = "inicio"
nombre = ""
num_carro = None
live = 100
puntos = 0
movimiento2 = []

counter, text2 = 5, '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font2 = pygame.font.SysFont('Consolas', 30)

#tiempopo_enpantalla = 0
#tamano_letras = 200

#Colores
aqua = (127, 255, 212)
darkred = (139, 0, 0)

#Boton para salir con sus fuciones de click y dibujo
class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 60
        self.height = 60

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

#Funcion para poner pausa
def pausa():
    time_duration = 3.5
    time.sleep(time_duration)

#Funcion con la que ejecutaremos las vists del juego
def redrawWindow(win, game, p, pl, pl2):
    # Imagen con movimiento en la imagen
    x_relativa = x % Fondo.rect.width
    win.blit(Fondo.image, (x_relativa - Fondo.rect.width, 1))
    if x_relativa < width:
        win.blit(Fondo.image, (x_relativa, 1))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Esperando jugador...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 30)

        #Vista para el jugador 1
        if p == 1:
            conttex = font2.render(text2, True, (0, 0, 0))
            texto_nombre = font.render(nombre, 1, (0, 0, 0))
            texto_cronometro = font.render("Tiempo partida: ", 1, (255, 255, 255))
            texto_nombre_titulo = font.render("Nombre Jugador: ", 1, (255, 255, 255))

            win.blit(texto_cronometro, (400, 13))
            win.blit(conttex, (560, 12))
            win.blit(texto_nombre_titulo, (18, 13))
            win.blit(texto_nombre, (18, 33))
            pl.draw()
            #pl2.draw()

        #Vista para el jugador 2
        else:
            conttex = font2.render(text2, True, (0, 0, 0))
            texto_nombre = font.render(nombre, 1, (0, 0, 0))
            texto_cronometro = font.render("Tiempo partida: ", 1, (255, 255, 255))
            texto_nombre_titulo = font.render("Nombre Jugador: ", 1, (255, 255, 255))

            win.blit(texto_cronometro, (400, 13))
            win.blit(conttex, (560, 12))
            win.blit(texto_nombre_titulo, (18, 13))
            win.blit(texto_nombre, (18, 33))
            pl.draw()
            #pl2.draw()

        for btn in btns:
            btn.draw(win)

    pygame.display.update()

btns = [Button("Terminar", 1300, 350, (darkred))]
#Funcion principal del juego
def main(no, num):
    global x
    global Fondo
    global nombre
    nombre = no
    global num_carro
    num_carro = num
    global players
    global movimiento2
    global counter
    global text2
    global puntos
    global puntos

    #Jugador que ingrese
    players = [Player(win, 0, 460, f'img/car{num}.png'), Player(win, 0, 0, f'img/car{num}.png')]

    global menu

    if menu == "inicio":
        menu_screen()
    else:

        run = True
        clock = pygame.time.Clock()
        n = Network()
        player = int(n.getP())
        print("You are player", player)

        while run:
            clock.tick(60)
            try:
                game = n.send("get")
            except:
                run = False
                print("Couldn't get game")
                break

            if counter == 0 and player == 1 or counter == 0 and player == 0:
                pygame.time.delay(500)
                js.guardarPuntaje(player, puntos, nombre)
                try:
                    game = n.send("reset")
                except:
                    run = False
                    print("Couldn't get game")
                    break

                font = pygame.font.SysFont("comicsans", 90)

                text = font.render("Final Tiempo.!", 1, (255,0,0))
                text2 = font.render("Siguiente Nivel!", 1, (255, 100, 0))


                win.blit(text, (200,400))
                win.blit(text2,(200,460))
                pygame.display.update()
                pygame.time.delay(2000)
                #menu_screen()

            #Par asalir y el boton de terminar
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    text2 = str(counter).rjust(3) if counter > 0 else 'Next!'
                if event.type == pygame.QUIT:
                    menu = "inicio"
                    run = False
                    pygame.quit()
                if counter == -1:
                    counter = 90

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    pausa()
                    for btn in btns:
                        if btn.click(pos) and game.connected():
                            if player == 0:
                                pygame.quit()
                            else:
                                pygame.quit()

            # Constantes
            x -= 5

            pressed_key = pygame.key.get_pressed()

            print("Tecla "+ str(pressed_key))

            #Ejemplo puntos
            if player == 1:
                puntos += 5
                movimiento2 = game.get_player_move(player)
                player1 = players[0]
                player2 = players[1]
                player1.move(pressed_key, player)
                n.send(str(player1.getpos()))
            else:
                puntos += 15
                movimiento2 = game.get_player_move(player)
                player1 = players[0]
                player2 = players[1]
                player1.move(pressed_key, player)
                n.send(str(player1.getpos()))


            print("Posicion del jugador "+str(player)+" "+ str(player1.getpos()))
            print("Nombre del jugador "+nombre)
            #x = movimiento2

            print("tupla-tupla-tupla:  "+ str(movimiento2))

            Reloj.tick(FPS)
            pygame.display.update()
            redrawWindow(win, game, player, player1, player2)

#Funcinon para la pantalla de inicio
def menu_screen():
    global nombre
    global menu
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill(aqua)
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Click Para inicia..!", 1, (255,255,255))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu = "Final"
                run = False

    main(nombre, num_carro)

