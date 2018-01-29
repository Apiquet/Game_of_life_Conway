import pygame
from pygame.locals import *

Nbr_Cell_x= 70
Nbr_Cell_y=70

Cell_Size= 8

#Color cell = Blue
Cell_alive = (68,101,182)
Cell_dead = (0,0,0)

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
    pause = True
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            #pause game with space key
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pause = not pause
            #change cell state by clicking
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                x //= Cell_Size
                y //= Cell_Size
                board[y][x]= not board[y][x]            
        #update the board state to the next generation
        if not pause:
            board = update_board(board)
        #fill the window with only dead cells 
        window.fill(Cell_dead)
        #draw on the window each cell alive
        for y in range(Nbr_Cell_y):
            for x in range(Nbr_Cell_x):
                if board[y][x]:
                    pygame.draw.rect(window, Cell_alive, (x * Cell_Size, y * Cell_Size, Cell_Size, Cell_Size))
        #display the result
        pygame.display.update()
    
    
def initialize_board():
    return [[False for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]

def update_board(board):
    next_board= initialize_board()
    for x in range(Nbr_Cell_y):
        for y in range(Nbr_Cell_x):
            neighbors = find_cell_neighbors(board, y, x)
            if neighbors == 3:
                next_board[y][x] = True
            elif neighbors == 2:
                next_board[y][x] = board[y][x]
            else:
                pass
        return next_board
    
def find_cell_neighbors(board, x, y):
    neighbors = 0
    #TODO: find nbr of neighbors
    return neighbors
   
if __name__ == "__main__":
    main()