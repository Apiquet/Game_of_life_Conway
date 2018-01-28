import pygame
from pygame.locals import *

WITDH = 600
HEIGHT = 600

def main():
    #pygame initialized
    pygame.init()
    pygame.display.set_caption("game of life")
    #creation of the window
    window = pygame.display.set_mode((WITDH,HEIGHT))
    
    #creation of the board
    board= initialize_board()
    
    
    
    
def initialize_board():
    return [[False for x in range(NX)] for y in range(NY)]

    
    