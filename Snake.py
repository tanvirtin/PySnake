from GameObj import GameObj

import pygame

class Snake(GameObj):
    def __init__(self, x, y, speed, boundary_x, boundary_y):
        super().__init__(x, y, 12, 12, "white")
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.speed = speed
        self.direction = "down"

    def draw(self, screen, key_input = None):
        if key_input:
            self.direction = key_input
        # in pygame the y coordinates start at the maximum value or in other words it is flipped
        if self.direction == "up":
            # up direction
            self.coordinates[1] -= self.speed

        elif self.direction == "down":
            # down direction
            self.coordinates[1] += self.speed

        elif self.direction == "right":
            # down direction
            self.coordinates[0] += self.speed

        elif self.direction == "left":
            # down direction
            self.coordinates[0] -= self.speed

        self.__boundary_check()

        pygame.draw.rect(screen, self.color, pygame.Rect(self.coordinates[0], self.coordinates[1], self.dimensions[0], self.dimensions[1]))


    def __boundary_check(self):
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
