import pygame

class GameObj(object):
    def __init__(self, x, y, w, h, color):
        self.coordinates = [x, y]
        self.dimensions = [w, h]
        self.color = pygame.color.Color(color)
