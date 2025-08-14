
import pygame
import sys
import settings


#pygame initialization 
pygame.init()

#display setup
WIDTH, HEIGHT = 1900, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Quit Game")

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((50, 18, 79))


    pygame.display.flip()