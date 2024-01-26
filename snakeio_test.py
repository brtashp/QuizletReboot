import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Study Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Snake start position
    x1 = width / 2
    y1 = height / 2

    x1_change = 0       
    y1_change = 0

    # Main game loop
    while not game_over:

        while game_close:
            game_display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)
        pygame.draw.rect(game_display, white, [x1, y1, snake_block, snake_block])

        pygame.display.update()

        # Check for boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
