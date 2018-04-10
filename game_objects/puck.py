import pygame
import utils.Color as Color
import random
from math import pi, cos, sin, degrees
from pygame.math import Vector2

class Puck:

    def __init__(
        self,
        gameDisplay,
        board_width,
        board_height,
        speed=1,
        radius=5):
        self.gameDisplay = gameDisplay
        self.board_height = board_height
        self.board_width = board_width
        self.speed = speed
        #        self.angle = random.uniform(0, 2*pi)
        #        print(self.angle)
        #        self.magnitude = 5
        self.radius = radius
        self.reset()

    def reset(self):
        self.x = self.board_width//2
        self.y = self.board_height//2
        self.dx = self.speed * self.board_width // self.board_height
        self.dy = self.speed

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.edges()

    def checkPaddle(self, paddle):
        paddle_top = paddle.y - paddle.height // 2
        paddle_bottom = paddle.y + paddle.height // 2
        paddle_left = paddle.x - paddle.width // 2
        paddle_right = paddle.x + paddle.width // 2
        puck_left = self.x - self.radius
        puck_right = self.x + self.radius
        puck_top = self.y - self.radius
        puck_bottom = self.y + self.radius
        intersects = not (
            puck_bottom < paddle_top or
            paddle_bottom < puck_top or
            puck_right < paddle_left or
            paddle_right < puck_left)
        if (intersects):
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
