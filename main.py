# game loop plan

# take input
# change head square direction, all other squares direction is updated
# update pos , all squares move one unit in their direction
# draw grid
# display squares

import pygame
from snake import snake_obj
from apple import Apple
from apple import generate_co_ords

# RGB values
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
# dimensions
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def drawGrid(SCREEN):  # Draw the outline only for the grid
    blockSize = 20  # Set the size of the grid block

    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


GRID = []
# creates a grid with all co-ordinates
for x in range(0, 20):
    for y in range(0, 20):
        GRID.append([x, y])


def update_snake(
    snake, direction, screen, apple
):  # Updates the attributes of the snake then displays it
    snake.update_all_directions(direction)
    snake.update_snake_pos()
    if snake.detect_collision():  # if there is a collison the function will end
        return True

    screen.fill(BLACK)  # this covers up the previous green rects which we have drawn
    apple.display_apple(screen)
    snake.display_snake(screen)
    return False


def main():  # start the game
    pygame.init()
    # Declaring variables
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    snake = snake_obj()
    clock = pygame.time.Clock()
    direction = [0, -1]
    apple = Apple([10, 10])

    SCREEN.fill(BLACK)
    drawGrid(SCREEN)

    while True:  # Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.head.direction != [
                    0,
                    1,
                ]:  # snake can not change dir to the opposite dir
                    direction = [0, -1]
                elif event.key == pygame.K_LEFT and snake.head.direction != [1, 0]:
                    direction = [-1, 0]
                elif event.key == pygame.K_RIGHT and snake.head.direction != [-1, 0]:
                    direction = [1, 0]
                elif event.key == pygame.K_DOWN and snake.head.direction != [0, -1]:
                    direction = [0, 1]

        if update_snake(  # checks for collison, if there is one we end the fame
            snake, direction, SCREEN, apple
        ):  # takes in the previous or new direction
            pygame.quit()
            break

        if apple.check_if_eaten(
            snake.head.co_ords
        ):  # if the apple is eaten, we create a new one
            snake.add_square()
            apple = Apple(
                generate_co_ords(GRID, [square.co_ords for square in snake.snake])
            )
            apple.display_apple(SCREEN)

        drawGrid(SCREEN)
        pygame.display.update()
        clock.tick(10)  # 10 frames a second


main()
