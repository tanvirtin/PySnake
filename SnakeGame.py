import pygame
import random
from Food import Food
from Snake import Snake
from SinglePlayer import SinglePlayer
from util import *

random.seed(42)

class SnakeGame(object):
    def __init__(self, ai_mode = False):
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.HWSURFACE)
        self.snakes_speed = SPEED

        if not ai_mode:
            self.sp = SinglePlayer(self.screen, self.snakes_speed)

    def sp_game_loop(self, action = None):
        return self.sp.game_loop(action)
