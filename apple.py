# apple plan

# x,y


# next co-ords gen (snake co-ords) to generate the next co-ordinates we have a list of all possible co-ords
# we delete co-ords which are inhibited the snake, then we choose a random pair of co-ords
# check if eaten
# display_apple

# how it fits into game logic

# snake starts with apple displayed infront at starting x,y
# once a loop check if eaten is true by taking the pos of head snake
# if so add one to length add a new instance of square
# next-coords of apple
# display apple
import pygame
import random

RED = (199, 55, 47)


class Apple:
    def __init__(self, co_ords):
        self.co_ords = co_ords
        self.blocksize = 20

    def check_if_eaten(
        self, head_co_ords
    ):  # checks if the head of snake is on the apple
        if self.co_ords == head_co_ords:
            return True

        return False

    def display_apple(self, screen):  # displays apple
        rect = pygame.Rect(
            self.co_ords[0] * self.blocksize,
            self.co_ords[1] * self.blocksize,
            self.blocksize,
            self.blocksize,
        )
        pygame.draw.rect(screen, RED, rect, 0)


def generate_co_ords(
    grid, taken_squares
):  # finds the squares which the snake is not on and choose one randomly
    valid_co_ords = [co_ords for co_ords in grid if co_ords not in taken_squares]
    return random.choice(valid_co_ords)
