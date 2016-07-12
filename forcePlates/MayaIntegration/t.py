import pygame

pygame.init()

options = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

screen=pygame.display.set_mode((500,500),options)

pygame.display.flip()
while True:
    pygame.event.pump()
    event=pygame.event.wait()
    if event.type==pygame.QUIT: pygame.display.quit()
    elif event.type==pygame.VIDEORESIZE:
        screen=pygame.display.set_mode(event.dict['size'],options)
        pygame.display.flip()