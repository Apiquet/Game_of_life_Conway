import pygame
from pygame.locals import *

import time

Nbr_Cell_x= 70
Nbr_Cell_y=70

Cell_Size= 8

#Color cell = Blue
Cell_alive = (68,101,182)
Cell_dead = (255,255,255)

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
    
    #number of the generation
    generation = 0 
    #speed of the game
    speed = 0  
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            #pause game with space key
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pause = not pause
                if event.key == K_r:
                    board=initialize_board() 
                if event.key == K_g:
                    board=glider_gun() 
                if event.key == K_UP:
                    speed+=1 
                
            #change cell state by clicking
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                x //= Cell_Size
                y //= Cell_Size
                board[y][x]= not board[y][x]
                #print coordinates in the right format to copy paste output in a function
                #allow to create a big structure once and after juste copy paste outputs in a function
                #like for def glider_gun()
                #print("board[{}][{}] = True".format(y,x))
        #update the board state to the next generation
        if not pause:
            time.sleep(speed/5)
            board = update_board(board)
            generation += 1
            #display generation number
            print("Generation {}".format(generation))            
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

def glider_gun():
    board = [[False for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]
    #coordinates come from outputs: print("board[{}][{}] = True".format(y,x))
    #thanks to the line above just need to click on the board to create the structure,
    #then, copy paste the outputs as I did for the following lines
    board[60][8] = True
    board[61][8] = True
    board[61][9] = True
    board[60][9] = True
    board[61][18] = True
    board[60][18] = True
    board[59][18] = True
    board[58][19] = True
    board[62][19] = True
    board[57][20] = True
    board[57][21] = True
    board[63][20] = True
    board[63][21] = True
    board[58][23] = True
    board[59][24] = True
    board[60][24] = True
    board[61][24] = True
    board[62][23] = True
    board[60][25] = True
    board[60][22] = True
    board[61][28] = True
    board[61][28] = True
    board[61][28] = True
    board[62][28] = True
    board[63][28] = True
    board[63][29] = True
    board[62][29] = True
    board[61][29] = True
    board[60][30] = True
    board[64][30] = True
    board[60][32] = True
    board[59][32] = True
    board[64][32] = True
    board[65][32] = True
    board[63][42] = True
    board[63][43] = True
    board[62][43] = True
    board[62][42] = True
    return board
    

def update_board(board):
    next_board= initialize_board()
    for x in range(Nbr_Cell_y):
        for y in range(Nbr_Cell_x):
            neighbors = find_cell_neighbors(board, x, y)
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
    if x < Nbr_Cell_x-1 and x > 0 and y < Nbr_Cell_y-1 and y > 0:
        if board[y][x+1]:
            neighbors+=1
        if board[y+1][x+1]:
            neighbors+=1
        if board[y-1][x+1]:
            neighbors+=1    
        if board[y][x-1]:
            neighbors+=1
        if board[y+1][x-1]:
            neighbors+=1 
        if board[y-1][x-1]:
            neighbors+=1  
        if board[y+1][x]:
            neighbors+=1 
        if board[y-1][x]:
            neighbors+=1    
    return neighbors
   
if __name__ == "__main__":
    main()