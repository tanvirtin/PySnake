from SnakeSegment import SnakeSegment
import pygame

# Snake is a SnakeSegment itself and also contains other SnakeSegments
class Snake(SnakeSegment):
    def __init__(self, x, y, speed, boundary_x, boundary_y):
            super().__init__(x, y, speed, boundary_x, boundary_y, head = True)
            # contains the segments which make up the body
            self.body = []
            self.reward = 0

    def grow(self):
        # depending on the direction I add the next body
        if len(self.body) > 0:
            # if the snake has a body then the direction of the last segment in the body
            # will decide which position the new segment will be in
            prev_segment = self.body[-1]
        else:
            # if the body is empty then the previous segment is the self itself
            prev_segment = self

        x = prev_segment.get_x()
        y = prev_segment.get_y()

        if prev_segment.current_direction == "up":
            self.body.append(SnakeSegment(x, y + 25, self.speed, self.boundary_x, self.boundary_y, False, prev_segment.current_direction))
        elif prev_segment.current_direction == "down":
            self.body.append(SnakeSegment(x, y - 25, self.speed, self.boundary_x, self.boundary_y, False, prev_segment.current_direction))
        elif prev_segment.current_direction == "left":
            self.body.append(SnakeSegment(x + 25, y, self.speed, self.boundary_x, self.boundary_y, False, prev_segment.current_direction))
        elif prev_segment.current_direction == "right":
            self.body.append(SnakeSegment(x - 25, y, self.speed, self.boundary_x, self.boundary_y, False, prev_segment.current_direction))

        self.reward += 1

    # MAIN GAME LOGIC TO UPDATE THE BODIES
    # this function will be invoked and the head's previous x and y coordinates
    # before it is about to be redrawn again in the current game loop will be passed in
    def update_body(self, prev_x, prev_y):
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


        self.update_body(prev_x, prev_y)
