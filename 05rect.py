#�u���y�C��
import  pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]								#�t��
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball=pygame.Surface((100,50)) #create surface
ball.fill((33,66,99)) 				#color the surface blue
ballrect=ball.get_rect() 			#get the rectangle bounds for the surface

clock=pygame.time.Clock() 		#�إ߮ɶ�����

while 1:											#�L�a�j��
    clock.tick(30) 						#�C�����30��
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit() #�ϥΪ̫������s

    ballrect = ballrect.move(speed) #�H�t��speed = [2, 2]�bcoordinates�y�жb�W����
		#�I������ϼu
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()