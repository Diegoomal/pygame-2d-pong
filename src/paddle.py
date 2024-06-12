import pygame

class Paddle:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.speed_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def move(self, screen_height):
        self.y += self.speed_y
        if self.y < 0:
            self.y = 0
        elif self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def set_speed(self, speed):
        self.speed_y = speed
