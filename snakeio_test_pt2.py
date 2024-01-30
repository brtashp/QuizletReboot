import pygame
import random
import time

pygame.init()

# Game variables
cell_size = 20
grid_width = 30
grid_height = 20
screen_width = grid_width * cell_size
screen_height = grid_height * cell_size
game_speed = 10

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake.io Game')

clock = pygame.time.Clock()

# Font for menus
font = pygame.font.SysFont('arial', 35)

# Snake initialization
snake_pos = [[grid_width//2, grid_height//2]]
snake_direction = 'UP'
snake_new_direction = snake_direction

# Food initialization
food_pos = [random.randint(0, grid_width-1), random.randint(0, grid_height-1)]

def draw_text(text, color, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    screen.blit(text_obj, text_rect)

def start_menu():
    menu_running = True
    while menu_running:
        screen.fill(black)
        draw_text("Press SPACE to start or Q to quit", white, screen_width // 2, screen_height // 2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_running = False  # Exit the menu if SPACE is pressed
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()  # Exit the game if Q is pressed

def pause_menu():
    paused = True
    while paused:
        screen.fill(black)
        draw_text("Paused. Press 'P' to continue", white, screen_width // 2, screen_height // 2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

# initializing start menu 
start_menu()

# Main game loop
running = True
pause = False 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_new_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_new_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_new_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_new_direction = 'RIGHT'

    # Update snake direction
    snake_direction = snake_new_direction

    # Move snake
    if snake_direction == 'UP':
        new_head = [snake_pos[0][0], snake_pos[0][1]-1]
    elif snake_direction == 'DOWN':
        new_head = [snake_pos[0][0], snake_pos[0][1]+1]
    elif snake_direction == 'LEFT':
        new_head = [snake_pos[0][0]-1, snake_pos[0][1]]
    elif snake_direction == 'RIGHT':
        new_head = [snake_pos[0][0]+1, snake_pos[0][1]]
    
    # Check for game over
    if new_head in snake_pos or new_head[0] < 0 or new_head[0] >= grid_width or new_head[1] < 0 or new_head[1] >= grid_height:
        running = False
        continue
    
    snake_pos.insert(0, new_head)
    
    # Check for food collision
    if new_head == food_pos:
        food_pos = [random.randint(0, grid_width-1), random.randint(0, grid_height-1)]
    else:
        snake_pos.pop()

    # Render
    screen.fill(black)
    for pos in snake_pos:
        pygame.draw.rect(screen, green, [pos[0]*cell_size, pos[1]*cell_size, cell_size, cell_size])
    pygame.draw.rect(screen, red, [food_pos[0]*cell_size, food_pos[1]*cell_size, cell_size, cell_size])
    
    pygame.display.update()
    clock.tick(game_speed)

pygame.quit()