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
        self.snakes_speed = 10

        # takes in x, y of the snake and the speed of the snake
        self.snake = Snake(800 / 2, 600 /2, self.snakes_speed, 800, 600)
        self.food_stack = [Food(random.randint(0, 700), random.randint(0, 500))]


    def consumption_check(self):
        # as is snake size bs is apple size
        if (self.snake.get_x() < self.food_stack[0].get_x() + self.food_stack[0].get_size() and self.snake.get_x() + self.snake.get_size() > self.food_stack[0].get_x() and self.snake.get_y() < self.food_stack[0].get_y() + self.food_stack[0].get_size() and self.snake.get_y() + self.snake.get_size() > self.food_stack[0].get_y()):
            return True
        else:
            return False

    def single_player_loop(self, key_input = None):
        pygame.event.pump()

        self.screen.fill(self.background_color)

        for food in self.food_stack:
            food.draw(self.screen)

        if not key_input:
            self.snake.draw(self.screen)

        else:
            self.snake.change_direction(key_input)
            self.snake.draw(self.screen)

        # check here if the snake ate the food
        if self.consumption_check():
            # we pop the food from the stack
            self.food_stack.pop()
            # and push another food at another random location
            self.food_stack.append(Food(random.randint(0, 700), random.randint(0, 500)))

            # finally we grow the snake as well by adding a new segment to the snake's body
            self.snake.grow()


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
