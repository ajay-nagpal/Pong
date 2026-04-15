import pygame,sys,random

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
cpu_paddle_speed=6

cpu_points,player_points=0,0

score_font=pygame.font.Font(None,70)#None=>use default font, 40 size

def reset_ball():
    ball.x=screen_width//2
    ball.y=screen_height//2

    #select ball direction randomly
    global ball_speed_x,ball_speed_y

    ball_speed_x*=random.choice([-1,1])
    ball_speed_y*=random.choice([-1,1])

def point_won(winner):
    global cpu_points,player_points

    if winner=="cpu":
        cpu_points+=1
    if winner=="player":
        player_points+=1

    reset_ball()

def animate_ball():
    global ball_speed_x,ball_speed_y,player_paddle

    ball.x+=ball_speed_x
    ball.y+=ball_speed_y

    if ball.bottom>=screen_height or ball.top<=0:
        #bounce it in opposite direction
        ball_speed_y*=-1

    if ball.right>=screen_width:
        #cpu wins point
        point_won("cpu")
        #bounce in random direction to start from fresh after miss

    if ball.left<=0:
        point_won("player")
        #bounce in random direction to start from fresh after miss
        #will do this in 
        
    #check ball collision with paddle
    if ball.colliderect(player_paddle) or ball.colliderect(cpu_paddle):
        #change balll direction horizontally
        ball_speed_x*=-1

def animate_player():
    #global player_paddle
    player_paddle.y+=player_paddle_speed

    if player_paddle.top<=0:
        player_paddle.top=0
    if player_paddle.bottom>=screen_height:
        player_paddle.bottom=screen_height

def animate_cpu():
     #manage cpy paddle direction based on ball center 
    global cpu_paddle_speed

    cpu_paddle.y+=cpu_paddle_speed
    if ball.centery<=cpu_paddle.centery:
        cpu_paddle_speed=-6
    if ball.centery>=cpu_paddle.centery:
        cpu_paddle_speed=6

    if cpu_paddle.top<=0:
        cpu_paddle.top=0
    if cpu_paddle.bottom>=screen_height:
        cpu_paddle.bottom=screen_height

while not exit_game:
    #1 event handling
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            exit_game=True
            break

        #key press
        if event.type==pygame.KEYDOWN:
            #move paddle
            if event.key==pygame.K_DOWN:
                player_paddle_speed=6
            elif event.key==pygame.K_UP:
                player_paddle_speed=-6
        
        #key release
        if event.type==pygame.KEYUP:
            #move paddle
            if event.key==pygame.K_DOWN:
                player_paddle_speed=0
            elif event.key==pygame.K_UP:
                player_paddle_speed=0
    
    animate_ball()
    
    animate_player()

    animate_cpu()
        
    #this willl stop traces of previous draw ball
    screen.fill(dark_grey_blue)

    player_score_surface=score_font.render(str(player_points),True,light_grey)
    cpu_score_surface=score_font.render(str(cpu_points),True,light_grey)

    screen.blit(player_score_surface,(3*screen_width//4,20))
    screen.blit(cpu_score_surface,(screen_width//4,20))

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