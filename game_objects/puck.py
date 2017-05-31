import pygame
import utils.Color as Color
import random
from math import pi, cos, sin, degrees
from pygame.math import Vector2

class Puck:

    def __init__(self, gameDisplay, board_width, board_height, radius=5):
        self.gameDisplay = gameDisplay
        self.board_height = board_height
        self.board_width = board_width
#        self.angle = random.uniform(0, 2*pi)
#        print(self.angle)
#        self.magnitude = 5
        self.radius = radius
        self.reset()

    def reset(self):
        self.x = self.board_width//2
        self.y = self.board_height//2
        self.dx = 3 
        self.dy = 1

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.edges()

    def checkPaddle(self, paddle):
        if self.dx < 0: # LEFT PADDLE 
            if (paddle.x-paddle.width//2 < self.x-self.radius < paddle.x+paddle.width//2 or paddle.x-paddle.width//2 < self.x+self.radius < paddle.x+paddle.width//2) and paddle.y - paddle.height//2 < self.y < paddle.y+paddle.height//2:
                self.dx *=-1
        if self.dx > 0: # RIGHT PADDLE
            if (paddle.x-paddle.width//2 < self.x+self.radius < paddle.x + paddle.width//2 or paddle.x-paddle.width//2 < self.x+self.radius < paddle.x + paddle.width//2) and (paddle.y - paddle.height//2 < self.y-self.radius//2 < paddle.y+paddle.height//2 or paddle.y - paddle.height//2 < self.y+self.radius//2 < paddle.y+paddle.height//2):
                self.dx *=-1

    def edges(self):
        in_y_bounds = 0 < self.y < self.board_height
        left_goal = 0 > self.x
        right_goal = self.x > self.board_width

        if not in_y_bounds:
            self.dy *= -1
        if left_goal:
            self.reset()
        if right_goal:
            self.reset()


    def show(self):
        pygame.draw.circle(self.gameDisplay, Color.WHITE, (self.x, self.y), self.radius)
        
    

