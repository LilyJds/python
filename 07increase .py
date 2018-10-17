import pygame
pygame.init()

width = 400
height = 300
windowSize = [width, height]
screen = pygame.display.set_mode(windowSize)

colour = pygame.color.Color('#F54455')
#[100, 100, 0]
c2=colour[2]

row = 0
done = False
while not done:
    increment = 255 / 100
    while row <= height:
        pygame.draw.rect(screen, colour, (0, row, width, row + increment))
        pygame.display.flip()
        if c2 + increment < 255:
            c2 += increment
            colour[2]=int(c2)
            #print(colour[0],colour[1],colour[2],increment)
        row += increment

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()