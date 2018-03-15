import pygame
from game_objects.puck import Puck
from game_objects.paddle import Paddle
import utils.Color as Color

pygame.init()
clock = pygame.time.Clock()

FPS = 60
DISPLAY_X = 600
DISPLAY_Y = 400
PADDLE_WIDTH = 10 
PADDLE_HEIGHT = 50
PADDLE_DISTANCE_FROM_GOAL = 30
PUCK_RADIUS = 10
PUCK_SPEED = 5
PADDLE_SPEED = 10 
gameDisplay = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))

puck = Puck(gameDisplay, board_width=DISPLAY_X, board_height=DISPLAY_Y,
            speed=PUCK_SPEED, radius=PUCK_RADIUS)
paddle_left = Paddle(gameDisplay, x=PADDLE_DISTANCE_FROM_GOAL,
                     board_height=DISPLAY_Y, height=PADDLE_HEIGHT,
                     width=PADDLE_WIDTH, speed = PADDLE_SPEED)
paddle_right = Paddle(gameDisplay, x=DISPLAY_X-PADDLE_DISTANCE_FROM_GOAL,
                      board_height=DISPLAY_Y, height=PADDLE_HEIGHT,
                      width=PADDLE_WIDTH, speed = PADDLE_SPEED)


def game_loop():
    game_exit = False
    while not game_exit:

        # EVENT HANDLER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_exit = True
                if event.key == pygame.K_UP:
                    paddle_right.set_speed(-1)
                elif event.key == pygame.K_DOWN:
                    paddle_right.set_speed(1)
                if event.key == pygame.K_w:
                    paddle_left.set_speed(-1)
                elif event.key == pygame.K_s:
                    paddle_left.set_speed(1)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    paddle_right.set_speed(0)
                if event.key == pygame.K_DOWN:
                    paddle_right.set_speed(0)
                if event.key == pygame.K_w:
                    paddle_left.set_speed(0)
                elif event.key == pygame.K_s:
                    paddle_left.set_speed(0)


        puck.checkPaddle(paddle_left)
        puck.checkPaddle(paddle_right)
        puck.update()
        paddle_left.update()
        paddle_right.update()

        gameDisplay.fill(Color.BLACK)
        puck.show()
        paddle_left.show()
        paddle_right.show()
        pygame.display.update()
        
        clock.tick(FPS)


game_loop()

pygame.quit()
quit()

