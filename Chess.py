import pygame
from classes import *
from functions import get_position
import sys

pygame.init()

height,width , border = 700,1000, 40  # put dimensions in multiple of 8
win = pygame.display.set_mode((width,height))

white = (255,255,255)

block_size = 70 # size of a block , also of images

rook_w = pygame.transform.scale(pygame.image.load("images/white-rook.png"), (block_size, block_size))
rook_b = pygame.transform.scale(pygame.image.load("images/black-rook.png"), (block_size, block_size))
pawn_w = pygame.transform.scale(pygame.image.load("images/white-pawn.png"), (block_size, block_size))
pawn_b = pygame.transform.scale(pygame.image.load("images/black-pawn.png"), (block_size, block_size))
bishop_w = pygame.transform.scale(pygame.image.load("images/white-bishop.png"), (block_size, block_size))
bishop_b = pygame.transform.scale(pygame.image.load("images/black-bishop.png"), (block_size, block_size))
queen_w = pygame.transform.scale(pygame.image.load("images/white-queen.png"), (block_size, block_size))
queen_b = pygame.transform.scale(pygame.image.load("images/black-queen.png"), (block_size, block_size))
king_w = pygame.transform.scale(pygame.image.load("images/white-king.png"), (block_size, block_size))
king_b = pygame.transform.scale(pygame.image.load("images/black-king.png"), (block_size, block_size))
knight_w = pygame.transform.scale(pygame.image.load("images/white-knight.png"), (block_size, block_size))
knight_b = pygame.transform.scale(pygame.image.load("images/black-knight.png"), (block_size, block_size))



red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

pygame.display.set_caption("Chess")

def game_loop(): # Main Game Loop
    while True:
        pygame.event.pump
        inputs()
        draw()
        temp()
        pygame.display.update()


def draw():
    win.fill(white)   # Blank White bg
    
    # Drawing Blocks
    dark = True
    for x in range(border,border+block_size*8,block_size):
        dark = not dark
        for y in range(border,border+block_size*8,block_size):
            if dark:
                pygame.draw.rect(win,(90,90,90),(x,y,block_size,block_size),0)
                dark=False
            else:
                pygame.draw.rect(win,(90,90,90),(x,y,block_size,block_size),1)
                dark = True
    
    
    #win.blit(rook, (border,border))

    # Texts
    alpha = ["a","b","c","d","e","f","g","h"]
    font = pygame.font.SysFont('comicsans', 15, True)
    for i,x in enumerate(range(border,border+block_size*8,block_size)):
        text = font.render(alpha[i], 1,(black))
        win.blit(text,(x+block_size/3,border+block_size*8))
    for i,y in enumerate(reversed(range(border,border+block_size*8,block_size))):
        text = font.render(str(i+1), 1,(black))
        win.blit(text,(border-13,y+block_size/3))

    #pieces
    global positions
    print(positions)
    # pawns
    for position in positions:
        #print(i)
        win.blit(pawn_b,(position[2][0],position[2][1]))




def inputs():  # Take all inputs of player
    for event in pygame.event.get():
            if event.type == pygame.QUIT:      # Check if you player clicked X to close window
                pygame.quit()
                sys.exit()

def temp():
    pass
    #rook_1 = piece(1,[100,100],4)
    #n = functions.get_position(rook_1)
    #print(n)

def create_pieces():
    for i in range(8):
        globals()[f"pawn_b{i}"] = pawns(0,[border+block_size*i,border+block_size*6])
    for i in range(8):
        globals()[f"pawn_w{i}"] = pawns(0,[border+block_size*i,border])
    
    


create_pieces()
positions = get_position()
game_loop()