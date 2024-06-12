import pygame
import config

class Score:

    def __init__(self, screen, margin, color):
        self.screen = screen
        self.margin = margin
        self.color = color

    def draw(self, score_left, score_right):
        font = pygame.font.SysFont(None, config.FONT_SIZE)
        text = font.render(f"{score_left} - {score_right}", True, self.color)
        self.screen.blit(
            text,
            [
                config.SCREEN_WIDTH // 2 - text.get_width() // 2,
                self.margin + 25
            ]
        )