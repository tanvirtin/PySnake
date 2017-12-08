from GameObj import GameObj
import pygame

# I will keep a stack in the main game object which will get popped
# when the snake eats the apple

class Food(GameObj):
    def __init__(self, x, y):
        super().__init__(x, y, 7, 7, "white")

    def draw(self, screen):
        # make this into a circle later
        pygame.draw.ellipse(screen, self.color, pygame.Rect(self.coordinates[0], self.coordinates[1], 7, 7))
