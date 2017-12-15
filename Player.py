from Snake import Snake
from Food import Food
import pygame
import random

class Player(object):
    def __init__(self, screen, speed):
        self.screen = screen
        self.snakes_speed = speed
        self.background_color = pygame.Color(73, 73, 73)
        self.food_stack = [Food(random.randint(0, 700), random.randint(0, 500))]

    def collision(self, object_a, object_b):
        return object_a.get_x() < object_b.get_x() + object_b.get_size() and object_a.get_x() + object_b.get_size() > object_b.get_x() and object_a.get_y() < object_b.get_y() + object_b.get_size() and object_a.get_y() + object_a.get_size() > object_b.get_y()

    def spawn_food(self):
        # we pop the food from the stack
        self.food_stack.pop()
        # and push another food at another random location
        self.food_stack.append(Food(random.randint(0, 700), random.randint(0, 500)))
