import  pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

screen.fill(black)
screen.blit(ball, ballrect)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()



