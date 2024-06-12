import pygame
import config

class GameEnvironment:
    def __init__(self, screen, margin, line_thickness, color):
        self.screen = screen
        self.margin = margin
        self.line_thickness = line_thickness
        self.color = color

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            [
                self.margin, self.margin,
                config.SCREEN_WIDTH - 2 * self.margin,
                config.SCREEN_HEIGHT - 2 * self.margin
            ],
            self.line_thickness
        )
