import pygame
import config
from score import Score
from paddle import Paddle
from ball import Ball
from environment import GameEnvironment

from game_funcs import detect_collision, compute_score

# Pygame initalization
pygame.init()

# Screen config
pygame.display.set_caption(config.GAME_TITLE)
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

# Create the Paddle, Ball e GameEnvironment
score = Score(screen, 10, config.WHITE)

environment = GameEnvironment(screen, 10, 10, config.WHITE)

ball = Ball(config.SCREEN_WIDTH // 2 - 10, config.SCREEN_HEIGHT // 2 - 10, 20, 5, 5, config.WHITE)

paddle_left = Paddle(30, config.SCREEN_HEIGHT // 2 - 50, 10, 100, 10, config.WHITE)
paddle_right = Paddle(config.SCREEN_WIDTH - 40, config.SCREEN_HEIGHT // 2 - 50, 10, 100, 10, config.WHITE)

# Set score
score_left = 0
score_right = 0

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_left.set_speed(-paddle_left.speed)
            elif event.key == pygame.K_s:
                paddle_left.set_speed(paddle_left.speed)
            elif event.key == pygame.K_UP:
                paddle_right.set_speed(-paddle_right.speed)
            elif event.key == pygame.K_DOWN:
                paddle_right.set_speed(paddle_right.speed)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle_left.set_speed(0)
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_right.set_speed(0)

    # Move screen itens - Paddles and Ball
    paddle_left.move(config.SCREEN_HEIGHT)
    paddle_right.move(config.SCREEN_HEIGHT)
    ball.move(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

    # Detect colision 
    detect_collision(ball, paddle_left, paddle_right)

    # Score - return updated score
    score_left, score_right = compute_score(ball, score_left, score_right)

    # Draw screen
    screen.fill(config.BLACK)
    environment.draw()
    ball.draw(screen)
    paddle_left.draw(screen)
    paddle_right.draw(screen)
    score.draw(score_left, score_right)

    pygame.display.flip()
    pygame.time.Clock().tick(config.CLOCKS)

pygame.quit()
