import sys, pygame
pygame.init()

size = width, height = 600, 400
speed = [10, 3]
black = 100, 200, 100

screen = pygame.display.set_mode(size)

ball = pygame.image.load("/Users/michalwitkowski/PyWorkspace/MyPyFun/pygame_experiments/assets/ball.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.blit(ball, ballrect)
    pygame.display.flip()
    screen.fill(black)
