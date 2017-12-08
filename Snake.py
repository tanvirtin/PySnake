from SnakeSegment import SnakeSegment
import pygame

# Snake is a SnakeSegment itself and also contains other SnakeSegments
class Snake(SnakeSegment):
    def __init__(self, x, y, speed, boundary_x, boundary_y, default_direction = "up"):
            super().__init__(x, y, speed, boundary_x, boundary_y, head = True)
            # contains the segments which make up the body
            self.body = []
            self.reward = 0
            self.current_direction = default_direction

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
        # then I change the current_direction itself to the new direction provided
        self.current_direction = direction


    def grow(self):
        # NOTE the x and y value of the SnakeSegment doesn't matter atm as it gets updated when it gets drawn
        self.body.append(SnakeSegment(0, 0, self.speed, self.boundary_x, self.boundary_y, False))
        self.reward += 1

    # MAIN GAME LOGIC TO UPDATE THE BODIES
    # this function will be invoked and the head's previous x and y coordinates
    # before it is about to be redrawn again in the current game loop will be passed in
    def update_body(self, screen, prev_x, prev_y):
        # a 15 directional gap between each segments
        segment_distance = 15
        # each segment in the body will return its previous x and y coordinates before it gets updated
        for segment in self.body:
            # each segment basically gets updated by the previous x and y coordinates of the segment it, the x and y coordinate
            # is the previous segments x and y coordinates before it gets redrawn, kind of tricky to understand
            prev_x, prev_y = segment.draw(screen, prev_x, prev_y)

    # draws the segment
    def draw(self, screen):
        # previous x and y coordinates to be passed on to the segments
        prev_x = self.coordinates[0]
        prev_y = self.coordinates[1]

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

        self.update_body(screen, prev_x, prev_y)
