import pygame
import random
from Food import Food
import time
import keyboard
from Snake import Snake
from SinglePlayer import SinglePlayer

random.seed(42)

class SnakeGame(object):
    def __init__(self, ai_mode = False):
        self.screen = pygame.display.set_mode((800, 600), pygame.HWSURFACE)
        self.snakes_speed = 10

        if not ai_mode:
            self.sp = SinglePlayer(self.screen, self.snakes_speed)

    def sp_game_loop(self, action = None):
        return self.sp.game_loop(action)

if __name__ == "__main__":
    game = SnakeGame()

    direction = None

    while not keyboard.is_pressed("q"):
        if keyboard.is_pressed("w"):
            direction = "up"

        elif keyboard.is_pressed("s"):
            direction = "down"

        elif keyboard.is_pressed("a"):
            direction = "left"

        elif keyboard.is_pressed("d"):
            direction = "right"

        end = game.sp_game_loop(direction)

        if end:
            game.sp.snake = Snake(50, 50, 10, 800, 600)
        time.sleep(0.05)
