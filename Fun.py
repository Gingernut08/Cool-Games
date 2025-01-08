import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

HIGH_SCORE_FILE = "high_score.txt"

def get_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except(FileNotFoundError, ValueError):
        return 0

def save_high_score(high_score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(high_score))

def your_score(score, high_score):
    score_text = score_font.render(f"Your Score: {score}", True, BLUE)
    high_score_text = score_font.render(f"High Score: {high_score}", True, GREEN)
    screen.blit(score_text, [0, 0])
    screen.blit(high_score_text, [0, 40])

def our_snake(BLOCK_SIZE, snake_list):
    for i in snake_list:
        pygame.draw.rect(screen, GREEN, [i[0], i[1], BLOCK_SIZE, BLOCK_SIZE])
    pygame.draw.rect(screen, RED, [snake_list[-1][0], snake_list[-1][1], BLOCK_SIZE, BLOCK_SIZE])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    high_score = get_high_score()

    x1, y1 = WIDTH // 2, HEIGHT // 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:

            if length_of_snake - 1 > high_score:
                high_score = length_of_snake - 1
                save_high_score(high_score)

            screen.fill(BLACK)
            message("You lost! Press Q (QUIT) or C (PLAY AGAIN)", RED)
            your_score(length_of_snake - 1, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                if event.key == pygame.K_d:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                if event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -BLOCK_SIZE
                if event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = BLOCK_SIZE
        
        if x1 >= WIDTH or x1<0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True
        
        our_snake(BLOCK_SIZE, snake_list)
        your_score(length_of_snake - 1, high_score)

        pygame.draw.rect(screen, BLUE, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foodx = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1
        
        clock.tick(10)
    
    pygame.quit()
    quit()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

gameLoop()