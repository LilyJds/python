import pygame
pygame.init()																	#啟動Pygame

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize) 	#建立繪圖視窗
colour = pygame.color.Color('#FFFFFF')				#白色

done = False     #flag用法1
while not done:  #flag用法2
    pygame.draw.circle(screen, colour, [200, 150], 50)
    pygame.display.flip()											#更新繪圖
    for event in pygame.event.get():
        if event.type == pygame.QUIT:					#使用者按關閉鈕
            done = True  #flag用法3
pygame.quit()																	#關閉繪圖視窗