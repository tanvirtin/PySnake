import pygame
from GameObj import GameObj

class SnakeSegment(GameObj):
    def __init__(self, x, y, speed, boundary_x, boundary_y, head = False, default_direction = "up"):
        if head:
            super().__init__(x, y, 12, 12, "white")
        else:
            super().__init__(x, y, 12, 12, "red")
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.speed = speed
        self.current_direction = default_direction
        self.previous_direction = self.current_direction

    def change_direction(self, direction):
        # I change the previous direction to what current_direction is
        self.previous_direction = self.current_direction
        # then I change the current_direction itself to the new direction provided
        self.current_direction = direction

    # draws the segment
    def draw(self, screen):
        # in pygame the y coordinates start at the maximum value or in other words it is flipped
        if self.current_direction == "up":
            # up direction
            self.coordinates[1] -= self.speed

        elif self.current_direction == "down":
            # down direction
            self.coordinates[1] += self.speed

        elif self.current_direction == "right":
            # down direction
            self.coordinates[0] += self.speed

        elif self.current_direction == "left":
            # down direction
            self.coordinates[0] -= self.speed

        self.__boundary_check()

        pygame.draw.rect(screen, self.color, pygame.Rect(self.coordinates[0], self.coordinates[1], self.dimensions[0], self.dimensions[1]))

    # checks the boundary for the segment
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
