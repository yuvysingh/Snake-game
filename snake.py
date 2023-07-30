# snake code plan


# snake square object
# x,y
# direction

# update x,y
# display square

# snake square linked list
# head

# update all directions
# update x,y
# display all squares

import pygame

GREEN = (127, 255, 0)


class square:  # each square of the snake is an object
    def __init__(self, x, y, direction):
        self.co_ords = [x, y]
        self.direction = direction
        self.blocksize = 20

    def update_pos(self):  # the co-ords x,y respectively are changed by the dir vector
        self.co_ords[0] += self.direction[0]
        self.co_ords[1] += self.direction[1]

    def display_square(
        self, screen
    ):  # Creates a rect with the co-ords and size, displays the rect
        rect = pygame.Rect(
            self.co_ords[0] * self.blocksize,
            self.co_ords[1] * self.blocksize,
            self.blocksize,
            self.blocksize,
        )
        pygame.draw.rect(screen, GREEN, rect, 0)


class snake_obj:  # Stores the array of snake squares
    def __init__(self):
        self.snake = [
            square(10, y, [0, -1]) for y in range(16, 19)
        ]  # produces intial three squares
        self.head = self.snake[0]  # the head square
        self.length = 3  # how many squares

    def update_all_directions(
        self, head_direction
    ):  # For each square, the direction of the square infront is new direction
        for i in range(
            self.length - 1, 0, -1
        ):  # iterates through the list backwards, each sqaure takes the direction the square in front
            self.snake[i].direction = self.snake[i - 1].direction

        self.head.direction = (
            head_direction  # the head square dir is based on user input
        )

    def update_snake_pos(self):  # updates x,y for all squares
        for square in self.snake:
            square.update_pos()

    def display_snake(self, screen):  # displays all the squares
        for square in self.snake:
            square.display_square(screen)
