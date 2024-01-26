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

vocab_terms = {
    "Ecosystem": "A biological community of interacting organisms and their physical environment.",
    "Mitosis": "A type of cell division that results in two daughter cells each having the same number and kind of chromosomes as the parent nucleus.",
    "Osmosis": "A process by which molecules of a solvent pass through a semipermeable membrane from a less concentrated solution into a more concentrated one.",
    # Add more terms and definitions here
}

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])
    
def draw_vocab_food(food_x, food_y, food_word):
    pygame.draw.rect(game_display, red, [food_x, food_y, snake_block, snake_block])
    food_text = font_style.render(food_word, True, black)
    game_display.blit(food_text, [food_x, food_y])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, white, [x[0], x[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False

    # Snake start position
    x1 = width / 2
    y1 = height / 2

    x1_change = 0       
    y1_change = 0

    current_definition, current_word = random.choice(list(vocab_terms.items()))
    word_choices = list(vocab_terms.keys())
    random.shuffle(word_choices)

    # Position for vocab 'food'
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        # Display current definition
        definition_text = font_style.render(current_definition, True, white)
        game_display.blit(definition_text, [50, 10])

        # Draw vocab 'food'
        for word in word_choices[:3]:  # Displaying three options
            draw_vocab_food(food_x, food_y, word)
            food_x += 70  # Adjust position for next word


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
