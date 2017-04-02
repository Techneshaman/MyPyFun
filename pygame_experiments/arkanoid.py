import pygame
import sys
import time

pygame.init()

canvas_size = (400, 600)
background_rgb = (100, 200, 100)

game_screen = pygame.display.set_mode(canvas_size)
game_screen.fill(background_rgb)

ball = pygame.image.load("/Users/michalwitkowski/PyWorkspace/MyPyFun/pygame_experiments/assets/ball.png")
ball_rect = ball.get_rect()

paddle = pygame.image.load("/Users/michalwitkowski/PyWorkspace/MyPyFun/pygame_experiments/assets/paddle.png")
paddle_rect = paddle.get_rect()

now = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    current_keystate = pygame.key.get_pressed()

    game_screen.blit(ball, ball_rect)
    game_screen.blit(paddle, paddle_rect)

    print(current_keystate[K_RIGHT])

    if current_keystate[K_RIGHT] == 1:
        paddle_rect = paddle_rect.move((5,0))

    if current_keystate[K_LEFT] == 1:
        paddle_rect = paddle_rect.move((-5,0))

    game_screen.blit(paddle, paddle_rect)
    pygame.display.flip()