import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
#colour = pygame.color.Color('#0A32F4')

pygame.draw.circle(background, (0,0,0), (150,150), 130, 4)
pygame.draw.circle(background, (0,0,255), (100,120), 25, 0)
pygame.draw.circle(background, (0,0,255), (200,120), 25, 0)
pygame.draw.ellipse(background, (255,0,255),[135, 130, 30, 80], 0)
pygame.draw.arc(background, (255,0,0), [80, 130, 150, 120], 3.4, 6.1, 9)
pygame.display.flip()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()