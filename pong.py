import pygame,sys

pygame.init()

screen_width=1280
screen_height=800
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("PONG!")

clock=pygame.time.Clock()

exit_game=False

dark_grey_blue=(62, 68, 81)
light_grey=(200,200,200)

ball = pygame.Rect(0, 0, 30, 30)
ball.center =(screen_width//2,screen_height//2)

cpu_paddle = pygame.Rect(0, 0, 20, 100)
cpu_paddle.centery =screen_height//2

player_paddle = pygame.Rect(0, 0, 20, 100)
player_paddle.midright =(screen_width,screen_height//2)

ball_speed_x=6
ball_speed_y=6

player_paddle_speed=0

def animate_ball():
    global ball_speed_x,ball_speed_y

    ball.x+=ball_speed_x
    ball.y+=ball_speed_y

    if ball.bottom>=screen_height or ball.top<=0:
        #bounce it in opposite direction
        ball_speed_y*=-1

    if ball.right>=screen_width or ball.left<=0:
        #bounce it in opposite direction
        ball_speed_x*=-1

while not exit_game:
    #1 event handling
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            exit_game=True
            break

    #2 update position
        #key press
        if event.type==pygame.KEYDOWN:
            #move paddle
            if event.key==pygame.K_DOWN:
                player_paddle_speed=5
            elif event.key==pygame.K_UP:
                player_paddle_speed=-5
        
        #key release
        if event.type==pygame.KEYUP:
            #move paddle
            if event.key==pygame.K_DOWN:
                player_paddle_speed=0
            elif event.key==pygame.K_UP:
                player_paddle_speed=0
    
    animate_ball()
    player_paddle.y+=player_paddle_speed

    if player_paddle.top<=0:
        player_paddle.top=0
    if player_paddle.bottom>=screen_height:
        player_paddle.bottom=screen_height
        
    #3 drawing
    #this willl stop traces of previous draw ball
    screen.fill(dark_grey_blue)
    
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.rect(screen,light_grey,cpu_paddle)
    pygame.draw.rect(screen,light_grey,player_paddle)

    pygame.draw.aaline(screen,light_grey,(screen_width//2,0),(screen_width//2,screen_height))
    #update the display
    pygame.display.update()
    clock.tick(100)
        

#quit pygame
pygame.quit()

sys.exit()