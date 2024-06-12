import pygame
import random

class Ball:
    def __init__(self, x, y, size, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])

    def move(self, screen_width, screen_height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.y < 0 or self.y > screen_height - self.size:
            self.speed_y *= -1

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.choice([-self.speed_x, self.speed_x])
        self.speed_y = random.choice([-self.speed_y, self.speed_y])
