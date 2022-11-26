import pygame
pygame.init()
white = (255,255,255)
display_surface = pygame.display.set_mode((1500,900))
pygame.display.set_caption('Display image')
image_name = pygame.image.load(r'E:\SPIDERMAN.png.jpeg')

while True:
    display_surface.fill(white)
    display_surface.blit(image_name,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            paygame.quit()
            quit()
        pygame.display.update()    
            
        
    
