import pygame
from GameObj import GameObj
import random

class SnakeSegment(GameObj):
    def __init__(self, x, y, speed, boundary_x, boundary_y, head = False, default_direction = "up"):
        self.colors = ["red", "green", "blue", "orange", "purple", "black", "pink"]
        if head:
            super().__init__(x, y, 12, 12, "white")
        else:
            super().__init__(x, y, 12, 12, self.colors[random.randint(0, len(self.colors) - 1)])
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.speed = speed
        self.current_direction = default_direction
        self.previous_direction = self.current_direction

    def change_direction(self, direction):
        # we go down if and only if our current direction is not up, so we can go down if
        # we are already down, left or right
        if direction == "down" and self.current_direction == "up":
            return
        # similarly if we are
        if direction == "up" and self.current_direction == "down":
            return
        # similarly if you are going left you cant go right
        if direction == "left" and self.current_direction == "right":
            return
        # if you are going right you cant go left
        if direction == "right" and self.current_direction == "left":
            return
        # I change the previous_direction to to what current_direction is
        self.previous_direction = self.current_direction
        # then I change the current_direction itself to the new direction provided
        self.current_direction = direction


    # draws the segment
    def draw(self, screen, x, y):

        # the previous coordinates will be stored in variables and returned, for the segment before the values gets
        # updated to get redrawn
        prev_x = self.coordinates[0]
        prev_y = self.coordinates[1]
        prev_direction = self.previous_direction

        # change the coordinates of the segment to the coordinates of the x and y provided
        self.coordinates[0] = x
        self.coordinates[1] = y

        self.boundary_check()

        pygame.draw.rect(screen, self.color, pygame.Rect(self.coordinates[0], self.coordinates[1], self.dimensions[0], self.dimensions[1]))

        return prev_x, prev_y, prev_direction

    # checks the boundary for the segment
    def boundary_check(self):
        # y boundary check if we go too up
        if self.coordinates[1] < 0:
            self.coordinates[1] = self.boundary_y

        # y boundary check if we go too down
        elif self.coordinates[1] > self.boundary_y:
            self.coordinates[1] = 0


        # x boundary check if we go too right
        elif self.coordinates[0] > self.boundary_x:
            self.coordinates[0] = 0

        # x boundary check we go too left
        elif self.coordinates[0] < 0:
            self.coordinates[0] = self.boundary_x
