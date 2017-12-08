import pygame
import random
import math
from Food import Food
import time
import keyboard
from Snake import Snake

random.seed(42)

class SnakeGame(object):
    def __init__(self, ai_mode = False):
        self.screen = pygame.display.set_mode((800, 600), pygame.HWSURFACE)
        self.background_color = pygame.Color(73, 73, 73)
        self.snakes_speed = 4

        # takes in x, y of the snake and the speed of the snake
        self.snake = Snake(50, 50, self.snakes_speed, 800, 600)
        self.food_stack = [Food(random.randint(0, 700), random.randint(0, 500))]

    def single_player_loop(self, key_input = None):
        # self.food_stack.pop()
        # self.food_stack.append(Food(random.randint(0, 700), random.randint(0, 500)))
        pygame.event.pump()

        self.screen.fill(self.background_color)

        for food in self.food_stack:
            food.draw(self.screen)

        if not key_input:
            self.snake.draw(self.screen)

        else:
            self.snake.change_direction(key_input)
            self.snake.draw(self.screen)

        pygame.display.flip()



if __name__ == "__main__":
    game = SnakeGame()

    while not keyboard.is_pressed("q"):
        if keyboard.is_pressed("w"):
            game.single_player_loop("up")

        elif keyboard.is_pressed("s"):
            game.single_player_loop("down")

        elif keyboard.is_pressed("a"):
            game.single_player_loop("left")

        elif keyboard.is_pressed("d"):
            game.single_player_loop("right")

        else:
            game.single_player_loop()
        time.sleep(0.05)
