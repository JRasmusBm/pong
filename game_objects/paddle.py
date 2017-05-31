import pygame
import utils.Color as Color

class Paddle:

    def __init__(self, gameDisplay, x, board_height, height=50, width=10):
        self.gameDisplay = gameDisplay
        self.board_height = board_height 
        self.x = x
        self.y = self.board_height//2
        self.dy = 0
        self.width = width
        self.height = height


    def update(self):
        if self.height//2 < self.y+self.dy < self.board_height-self.height//2:
            self.y += self.dy

    def set_speed(self, direction):
        if direction == 0:
            self.dy = 0
        if direction > 0:
            self.dy = 5
        if direction < 0:
            self.dy = -5

    def show(self):
        pygame.draw.rect(self.gameDisplay, Color.WHITE, [self.x-self.width//2, self.y-self.height//2, self.width, self.height])
         
