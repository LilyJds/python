#彈跳球遊戲
import  pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]								#速度
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball=pygame.Surface((100,50)) #create surface
ball.fill((33,66,99)) 				#color the surface blue
ballrect=ball.get_rect() 			#get the rectangle bounds for the surface

clock=pygame.time.Clock() 		#建立時間元件

while 1:											#無窮迴圈
    clock.tick(30) 						#每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit() #使用者按關閉鈕

    ballrect = ballrect.move(speed) #以速度speed = [2, 2]在coordinates座標軸上移動
		#碰到牆壁反彈
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()