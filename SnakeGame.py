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
        self.snake = Snake(50, 50, self.snakes_speed, 800, 600)
        self.food_stack = [Food(random.randint(0, 700), random.randint(0, 500))]


    def consumption_check(self):
        if (self.snake.get_x() < self.food_stack[0].get_x() + self.food_stack[0].get_size() and self.snake.get_x() + self.snake.get_size() > self.food_stack[0].get_x() and self.snake.get_y() < self.food_stack[0].get_y() + self.food_stack[0].get_size() and self.snake.get_y() + self.snake.get_size() > self.food_stack[0].get_y()):
            return True
        else:
            return False

    def self_collision_check(self):
        bodies = self.snake.get_body()

        seg_count = 0
        for segment in bodies:
            # we check for collision only if theres more than 2 head
            if seg_count > 2:
                if (self.snake.get_x() < segment.get_x() + segment.get_size() and self.snake.get_x() + segment.get_size() > segment.get_x() and self.snake.get_y() < segment.get_y() + segment.get_size() and self.snake.get_y() + self.snake.get_size() > segment.get_y()):
                    return True
                else:
                    return False
            seg_count += 1


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

        return self.self_collision_check()



if __name__ == "__main__":
    game = SnakeGame()

    while not keyboard.is_pressed("q"):
        if keyboard.is_pressed("w"):
            end = game.single_player_loop("up")

        elif keyboard.is_pressed("s"):
            end = game.single_player_loop("down")

        elif keyboard.is_pressed("a"):
            end = game.single_player_loop("left")

        elif keyboard.is_pressed("d"):
            end = game.single_player_loop("right")

        else:
            end = game.single_player_loop()
        if end:
            break;
        time.sleep(0.05)

    # while not keyboard.is_pressed("q"):
    #     action = random.randint(0, 4)
    #     if action == 0:
    #         game.single_player_loop("up")
    #
    #     elif action == 1:
    #         game.single_player_loop("down")
    #
    #     elif action == 2:
    #         game.single_player_loop("left")
    #
    #     elif action == 3:
    #         game.single_player_loop("right")
    #
    #     else:
    #         game.single_player_loop()
    #     time.sleep(0.05)
