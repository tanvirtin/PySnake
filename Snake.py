from SnakeSegment import SnakeSegment
import pygame

# Snake is a SnakeSegment itself and also contains other SnakeSegments
class Snake(SnakeSegment):
    def __init__(self, x, y, speed, boundary_x, boundary_y):
            super().__init__(x, y, speed, boundary_x, boundary_y, head = True)
            # contains the segments which make up the body
            self.body = []
            self.reward = 0

    def get_body(self):
        return self.body

    def grow(self):
        # NOTE the x and y value of the SnakeSegment doesn't matter atm as it gets updated when it gets drawn
        self.body.append(SnakeSegment(0, 0, self.speed, self.boundary_x, self.boundary_y, False))
        self.reward += 1

    # MAIN GAME LOGIC TO UPDATE THE BODIES
    # this function will be invoked and the head's previous x and y coordinates
    # before it is about to be redrawn again in the current game loop will be passed in
    def update_body(self, screen, prev_x, prev_y, previous_direction):
        # each segment in the body will return its previous x and y coordinates before it gets updated
        for segment in self.body:
            segment.change_direction(previous_direction)
            # each segment basically gets updated by the previous x and y coordinates of the segment it, the x and y coordinate
            # is the previous segments x and y coordinates before it gets redrawn, kind of tricky to understand

            prev_x, prev_y, previous_direction = segment.draw(screen, prev_x, prev_y)

    # draws the segment
    def draw(self, screen):
        # previous x and y coordinates to be passed on to the segments
        prev_x = self.coordinates[0]
        prev_y = self.coordinates[1]
        previous_direction = self.previous_direction

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

        self.boundary_check()

        pygame.draw.rect(screen, self.color, pygame.Rect(self.coordinates[0], self.coordinates[1], self.dimensions[0], self.dimensions[1]))

        self.update_body(screen, prev_x, prev_y, previous_direction)
