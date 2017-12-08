import pygame
import random
import math
from Food import Food
import time
import keyboard

random.seed(42)


class SnakeGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600), pygame.HWSURFACE)
        self.background_color = pygame.Color(73, 73, 73)

        self.food_stack = [Food(random.randint(0, 700), random.randint(0, 500))]

    def play(self):
        self.food_stack.pop()
        self.food_stack.append(Food(random.randint(0, 700), random.randint(0, 500)))
        pygame.event.pump()

        self.screen.fill(self.background_color)

        for food in self.food_stack:
            food.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    game = SnakeGame()

    while not keyboard.is_pressed("q"):
        game.play()
        time.sleep(1)
