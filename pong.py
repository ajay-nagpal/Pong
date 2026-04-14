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

cpu = pygame.Rect(0, 0, 20, 100)
cpu.centery =screen_height//2

player = pygame.Rect(0, 0, 20, 100)
player.midright =(screen_width,screen_height//2)

while not exit_game:
    #1 event handling
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            exit_game=True
            break

    #2 update position

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pass
            elif event.key==pygame.K_RIGHT:
                pass
            elif event.key==pygame.K_DOWN:
                pass
            elif event.key==pygame.K_UP:
                pass
    
    
    #3 drawing
    screen.fill(dark_grey_blue)
    
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.rect(screen,light_grey,cpu)
    pygame.draw.rect(screen,light_grey,player)

    pygame.draw.aaline(screen,light_grey,(screen_width//2,0),(screen_width//2,screen_height))
    #update the display
    pygame.display.update()
    clock.tick(100)
        

#quit pygame
pygame.quit()

sys.exit()