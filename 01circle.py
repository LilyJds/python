import pygame
pygame.init()																	#�Ұ�Pygame

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize) 	#�إ�ø�ϵ���
colour = pygame.color.Color('#FFFFFF')				#�զ�

done = False     #flag�Ϊk1
while not done:  #flag�Ϊk2
    pygame.draw.circle(screen, colour, [200, 150], 50)
    pygame.display.flip()											#��sø��
    for event in pygame.event.get():
        if event.type == pygame.QUIT:					#�ϥΪ̫������s
            done = True  #flag�Ϊk3
pygame.quit()																	#����ø�ϵ���