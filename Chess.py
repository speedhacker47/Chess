import pygame
from classes import *
from functions import get_position
import variables
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
        match position[0]:
            case 0:
                if position[1]==1:
                    win.blit(pawn_b,(position[2][0],position[2][1]))
                else:
                    win.blit(pawn_w,(position[2][0],position[2][1]))
            case 1:
                if position[1]==1:
                    win.blit(knight_b,(position[2][0],position[2][1]))
                else:
                    win.blit(knight_w,(position[2][0],position[2][1]))
            case 2:
                if position[1]==1:
                    win.blit(bishop_b,(position[2][0],position[2][1]))
                else:
                    win.blit(bishop_w,(position[2][0],position[2][1]))
            case 3:
                if position[1]==1:
                    win.blit(rook_b,(position[2][0],position[2][1]))
                else:
                    win.blit(rook_w,(position[2][0],position[2][1]))
            case 4:
                if position[1]==1:
                    win.blit(queen_b,(position[2][0],position[2][1]))
                else:
                    win.blit(queen_w,(position[2][0],position[2][1]))
            case 5:
                if position[1]==1:
                    win.blit(king_b,(position[2][0],position[2][1]))
                else:
                    win.blit(king_w,(position[2][0],position[2][1]))


def inputs():  # Take all inputs of player
    for event in pygame.event.get():
            if event.type == pygame.QUIT:      # Check if you player clicked X to close window
                pygame.quit()
                sys.exit()

def create_pieces():
    ######## PAWNS ##############
    for i,j in enumerate(variables.pawn_pos_w):
        globals()[f"pawn_w{i}"] = pawns(0,variables.block_positions[j])  # Creating objects in pawn class (white color)
    for i,j in enumerate(variables.pawn_pos_b):
        globals()[f"pawn_b{i}"] = pawns(1,variables.block_positions[j]) # blck color

    ######## ROOK ################
    for i,j in enumerate(variables.rook_pos_w):globals()[f"rook_w{i}"] = rook(0,variables.block_positions[j])
    for i,j in enumerate(variables.rook_pos_b):globals()[f"rook_b{i}"] = rook(1,variables.block_positions[j])
                         
    ###### BISHOP #############
    for i,j in enumerate(variables.bishop_pos_w):globals()[f"bishop_w{i}"] = bishop(0,variables.block_positions[j])
    for i,j in enumerate(variables.bishop_pos_b):globals()[f"bishop_b{i}"] = bishop(1,variables.block_positions[j])

    ######## KNIGHT #############
    for i,j in enumerate(variables.knight_pos_w):globals()[f"knight_w{i}"] = knight(0,variables.block_positions[j])
    for i,j in enumerate(variables.knight_pos_b):globals()[f"knight_b{i}"] = knight(1,variables.block_positions[j])

    ####### Queen ######

    queen_b  = queen(1,variables.block_positions["d8"])
    queen_w  = queen(0,variables.block_positions["d1"])

    ###### King #############

    king_b = king(1,variables.block_positions["e8"])
    king_w = king(0,variables.block_positions["e1"])

create_pieces()
positions = get_position()
game_loop()