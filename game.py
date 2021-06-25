import pygame
class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    #Nos retorna la posicion del carro actual
    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    #El jugador y su movimiento/posicion
    def play(self, player, move):
        self.moves[player] = move

    #Jugor al True o False
    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    #Para permitir la vista de cada cliente
    def resetWent(self):
        self.p1Went = False
        self.p2Went = False