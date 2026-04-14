import pygame,sys

pygame.init()
screen=pygame.display.set_mode((1280,800))

pygame.display.set_caption("PONG!")

clock=pygame.time.Clock()

exit_game=False

dark_grey_blue=(62, 68, 81)
light_grey=(200,200,200)

while not exit_game:
    #1 event handling
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            exit_game=True
            break

    #2 update position

        
    #3 update the display
    pygame.display.update()
    clock.tick(100)
        

#quit pygame
pygame.quit()

sys.exit()