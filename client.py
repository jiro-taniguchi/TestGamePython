import pygame
from pygame.locals import *

SIZE_WIN_X=480
SIZE_WIN_Y=480
CHAR_FILENAME='static/char.png'
pygame.init()
MAIN_WIN = pygame.display.set_mode((SIZE_WIN_X,SIZE_WIN_Y))
CHAR_IMAGE = pygame.image.load(CHAR_FILENAME).convert()
SURF_CHAR=pygame.Surface((40,50))
SURF_CHAR.blit(CHAR_IMAGE,(0,0),(0,0,40,50))

MAIN_WIN.blit(SURF_CHAR,(0,0))
pygame.display.flip()
BREAKOUT=True
while BREAKOUT:
    for event in pygame.event.get():
        if event.type == QUIT:
            BREAKOUT=False