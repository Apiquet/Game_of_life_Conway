import pygame
from pygame.locals import *
from random import randint
import time

Nbr_Cell_x = 70
Nbr_Cell_y = 70

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
                    window.fill(Cell_dead)                    
                    board=initialize_board() 
                if event.key == K_a:                
                    window.fill(Cell_dead)                    
                    board=random_board() 
                if event.key == K_g:
                    window.fill(Cell_dead)
                    board=glider_gun() 
                if event.key == K_m:
                    window.fill(Cell_dead)
                    board=max_structure() 
                if event.key == K_b:
                    window.fill(Cell_dead)
                    board=spaceship() 
                #save structure
                if event.key == K_s:
                    for y in range(Nbr_Cell_y):
                        for x in range(Nbr_Cell_x):
                            if board[y][x]:
                                print("board[{}][{}] = True".format(y,x))                   
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
        text_on_window(window, "r: refresh, g: gun plane, m: max, b: spaceship, space: pause", 5, 5)
            
        
def text_on_window(screen, text, x, y, size = 28, color = (200, 000, 000), font_type = 'Comics San MS'):
    text = str(text)
    font = pygame.font.SysFont(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
    
def initialize_board():
    return [[False for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]
def random_board() :
    return [[randint(0,1) for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]
    
def glider_gun():
    board = [[False for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]
    #coordinates come from outputs: print("board[{}][{}] = True".format(y,x))
    #create a structure by clicking on the board
    #then click on the 's' key to save it to a new function
    board[57][20] = True
    board[57][21] = True
    board[58][19] = True
    board[58][23] = True
    board[59][18] = True
    board[59][24] = True
    board[59][32] = True
    board[60][8] = True
    board[60][9] = True
    board[60][18] = True
    board[60][22] = True
    board[60][24] = True
    board[60][25] = True
    board[60][30] = True
    board[60][32] = True
    board[61][8] = True
    board[61][9] = True
    board[61][18] = True
    board[61][24] = True
    board[61][28] = True
    board[61][29] = True
    board[62][19] = True
    board[62][23] = True
    board[62][28] = True
    board[62][29] = True
    board[62][42] = True
    board[62][43] = True
    board[63][20] = True
    board[63][21] = True
    board[63][28] = True
    board[63][29] = True
    board[63][42] = True
    board[63][43] = True
    board[64][30] = True
    board[64][32] = True
    board[65][32] = True
    return board

def spaceship():
    board = [[False for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]
    #coordinates come from outputs: print("board[{}][{}] = True".format(y,x))
    #create a structure by clicking on the board
    #then click on the 's' key to save it to a new function
    board[15][5] = True
    board[15][6] = True
    board[15][7] = True
    board[15][8] = True
    board[15][9] = True
    board[15][10] = True
    board[16][4] = True
    board[16][10] = True
    board[17][10] = True
    board[18][4] = True
    board[18][9] = True
    board[19][6] = True
    board[19][7] = True
    board[24][5] = True
    board[24][6] = True
    board[24][7] = True
    board[24][8] = True
    board[24][9] = True
    board[25][4] = True
    board[25][9] = True
    board[26][9] = True
    board[27][4] = True
    board[27][8] = True
    board[28][6] = True
    board[33][5] = True
    board[33][6] = True
    board[33][7] = True
    board[33][8] = True
    board[34][4] = True
    board[34][8] = True
    board[35][8] = True
    board[36][4] = True
    board[36][7] = True
    return board

def max_structure():
    board = [[False for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]
    #coordinates come from outputs: print("board[{}][{}] = True".format(y,x))
    #create a structure by clicking on the board
    #then click on the 's' key to save it to a new function
    board[23][44] = True
    board[24][43] = True
    board[24][44] = True
    board[24][45] = True
    board[25][38] = True
    board[25][39] = True
    board[25][40] = True
    board[25][45] = True
    board[25][46] = True
    board[26][37] = True
    board[26][40] = True
    board[26][41] = True
    board[26][42] = True
    board[26][45] = True
    board[26][47] = True
    board[26][48] = True
    board[27][36] = True
    board[27][40] = True
    board[27][42] = True
    board[27][45] = True
    board[27][47] = True
    board[28][36] = True
    board[28][41] = True
    board[28][43] = True
    board[28][45] = True
    board[28][47] = True
    board[28][49] = True
    board[28][50] = True
    board[29][38] = True
    board[29][43] = True
    board[29][45] = True
    board[29][49] = True
    board[29][50] = True
    board[30][26] = True
    board[30][27] = True
    board[30][28] = True
    board[30][29] = True
    board[30][35] = True
    board[30][37] = True
    board[30][42] = True
    board[30][46] = True
    board[30][48] = True
    board[30][49] = True
    board[30][50] = True
    board[31][26] = True
    board[31][30] = True
    board[31][31] = True
    board[31][33] = True
    board[31][35] = True
    board[31][36] = True
    board[31][37] = True
    board[31][39] = True
    board[31][40] = True
    board[31][50] = True
    board[31][51] = True
    board[32][26] = True
    board[32][32] = True
    board[32][33] = True
    board[32][39] = True
    board[33][27] = True
    board[33][30] = True
    board[33][31] = True
    board[33][33] = True
    board[33][36] = True
    board[33][39] = True
    board[33][41] = True
    board[33][42] = True
    board[34][33] = True
    board[34][35] = True
    board[34][37] = True
    board[34][39] = True
    board[34][41] = True
    board[34][43] = True
    board[34][49] = True
    board[34][50] = True
    board[34][51] = True
    board[34][52] = True
    board[35][27] = True
    board[35][30] = True
    board[35][31] = True
    board[35][33] = True
    board[35][36] = True
    board[35][39] = True
    board[35][42] = True
    board[35][43] = True
    board[35][45] = True
    board[35][47] = True
    board[35][48] = True
    board[35][52] = True
    board[36][26] = True
    board[36][32] = True
    board[36][33] = True
    board[36][37] = True
    board[36][39] = True
    board[36][41] = True
    board[36][45] = True
    board[36][46] = True
    board[36][52] = True
    board[37][26] = True
    board[37][30] = True
    board[37][31] = True
    board[37][33] = True
    board[37][35] = True
    board[37][36] = True
    board[37][39] = True
    board[37][42] = True
    board[37][45] = True
    board[37][47] = True
    board[37][48] = True
    board[37][51] = True
    board[38][26] = True
    board[38][27] = True
    board[38][28] = True
    board[38][29] = True
    board[38][35] = True
    board[38][37] = True
    board[38][39] = True
    board[38][41] = True
    board[38][43] = True
    board[38][45] = True
    board[39][36] = True
    board[39][37] = True
    board[39][39] = True
    board[39][42] = True
    board[39][45] = True
    board[39][47] = True
    board[39][48] = True
    board[39][51] = True
    board[40][39] = True
    board[40][45] = True
    board[40][46] = True
    board[40][52] = True
    board[41][27] = True
    board[41][28] = True
    board[41][38] = True
    board[41][39] = True
    board[41][41] = True
    board[41][42] = True
    board[41][43] = True
    board[41][45] = True
    board[41][47] = True
    board[41][48] = True
    board[41][52] = True
    board[42][28] = True
    board[42][29] = True
    board[42][30] = True
    board[42][32] = True
    board[42][36] = True
    board[42][41] = True
    board[42][43] = True
    board[42][49] = True
    board[42][50] = True
    board[42][51] = True
    board[42][52] = True
    board[43][28] = True
    board[43][29] = True
    board[43][33] = True
    board[43][35] = True
    board[43][40] = True
    board[44][28] = True
    board[44][29] = True
    board[44][31] = True
    board[44][33] = True
    board[44][35] = True
    board[44][37] = True
    board[44][42] = True
    board[45][31] = True
    board[45][33] = True
    board[45][36] = True
    board[45][38] = True
    board[45][42] = True
    board[46][30] = True
    board[46][31] = True
    board[46][33] = True
    board[46][36] = True
    board[46][37] = True
    board[46][38] = True
    board[46][41] = True
    board[47][32] = True
    board[47][33] = True
    board[47][38] = True
    board[47][39] = True
    board[47][40] = True
    board[48][33] = True
    board[48][34] = True
    board[48][35] = True
    board[49][34] = True    
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