import pygame
from pygame.locals import *

Nbr_Cell_x= 70
Nbr_Cell_y=70

Cell_Size= 8

WITDH = Nbr_Cell_x * Cell_Size
HEIGHT = Nbr_Cell_y * Cell_Size

def main():
    #pygame initialized
    pygame.init()
    pygame.display.set_caption("game of life")
    #creation of the window
    window = pygame.display.set_mode((WITDH,HEIGHT))
    
    #creation of the board
    board= initialize_board()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        
    
    
def initialize_board():
    return [[False for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]

    
if __name__ == "__main__":
    main()