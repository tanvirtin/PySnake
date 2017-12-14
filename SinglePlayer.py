from Snake import Snake
from Food import Food
import pygame
import random


class SinglePlayer(object):
    def __init__(self, screen, speed):
        self.screen = screen
        self.snakes_speed = speed
        self.background_color = pygame.Color(73, 73, 73)
        # takes in x, y of the snake and the speed of the snake
        self.snake = Snake(50, 50, self.snakes_speed, 800, 600)
        self.food_stack = [Food(random.randint(0, 700), random.randint(0, 500))]


    def consumption_check(self):
        if (self.snake.get_x() < self.food_stack[0].get_x() + self.food_stack[0].get_size() and self.snake.get_x() + self.snake.get_size() > self.food_stack[0].get_x() and self.snake.get_y() < self.food_stack[0].get_y() + self.food_stack[0].get_size() and self.snake.get_y() + self.snake.get_size() > self.food_stack[0].get_y()):
            return True
        else:
            return False

    def self_collision_check(self):
        # THERE IS A BUG HERE PLS FIX THIS
        bodies = self.snake.get_body()

        seg_count = 0
        for segment in bodies:
            # we check for collision only if theres more than 2 head
            if seg_count > 2:
                if (self.snake.get_x() < segment.get_x() + segment.get_size() and self.snake.get_x() + segment.get_size() > segment.get_x() and self.snake.get_y() < segment.get_y() + segment.get_size() and self.snake.get_y() + self.snake.get_size() > segment.get_y()):
                    return True
            seg_count += 1

        # False is returend if and ONLY if we get out of the loop and have iterated over every single segment and found no collision
        # this prevents the check from just checking one segment finding no collision and returning
        return False


    def game_loop(self, key_input = None):
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

        return self.self_collision_check()
