import pygame
from classes import *
import functions
from functions import get_position
import variables
import sys

pygame.init()

height,width , border = 700,1000, 40  # put dimensions in multiple of 8
win = pygame.display.set_mode((width,height))

white = (255,255,255)

block_size = 70 # size of a block , also of images

block_clicked = []

holding = None

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
        move_piece()
        pygame.display.update()


def draw():
    global positions,valid_blocks
    win.fill(white)   # Blank White bg
    
    # Drawing Blocks
    
    dark = True
    count = 0 
    global holding
    #print(holding)
    for x in variables.block_positions_value_only:
        count += 1
        if dark:
            if holding is not None and x == holding.position : pygame.draw.rect(win,blue,(x[0],x[1],block_size,block_size),0)
            else : pygame.draw.rect(win,(90,90,90),(x[0],x[1],block_size,block_size),0)
        else:
            if holding is not None and x == holding.position : pygame.draw.rect(win,blue,(x[0],x[1],block_size,block_size),0)
            else : pygame.draw.rect(win,(90,90,90),(x[0],x[1],block_size,block_size),1)
        if count % 8 !=  0 : dark = not dark
    
    # Texts
    alpha = ["a","b","c","d","e","f","g","h"]
    font = pygame.font.SysFont('comicsans', 15, True)
    for i,x in enumerate(range(border,border+block_size*8,block_size)):
        text = font.render(alpha[i], 1,(black))
        win.blit(text,(x+block_size/3,border+block_size*8))
    for i,y in enumerate(reversed(range(border,border+block_size*8,block_size))):
        text = font.render(str(i+1), 1,(black))
        win.blit(text,(border-13,y+block_size/3))
    

        
    ######### VALID MOVES ###############
    for block in valid_blocks:
        #print(block[0])
        if block[0] >= 40 and block [0] < 600 and block[0] >= 40 and block[1] < 600:
            pygame.draw.rect(win,green,(block[0],block[1],block_size,block_size),0)

    for block in opponet_piece_in_path:
        pygame.draw.rect(win,red,(block[0],block[1],block_size,block_size),0)

    ########## PIECES ####################
    
    positions = get_position()
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
    global block_clicked
    global holding
    for event in pygame.event.get():
            if event.type == pygame.QUIT:      # Check if you player clicked X to close window
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                btn=pygame.mouse
                block_clicked = functions.check_clicked([pos[0],pos[1]])[0]
                holding = functions.check_clicked([pos[0],pos[1]])[1]

def create_pieces():
    ######## PAWNS ##############
    for i,j in enumerate(variables.pawn_pos_w):
        globals()[f"pawn_w{i}"] = pawns(0,variables.block_positions[j])  # Creating objects in pawn class (white color)
    for i,j in enumerate(variables.pawn_pos_b):
        globals()[f"pawn_b{i}"] = pawns(1,variables.block_positions[j]) # blck color

    ######## ROOK ################
    for i,j in enumerate(variables.rook_pos_w) : globals()[f"rook_w{i}"] = rook(0,variables.block_positions[j])
    for i,j in enumerate(variables.rook_pos_b) : globals()[f"rook_b{i}"] = rook(1,variables.block_positions[j])
                         
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

def move_piece():
    global block_clicked,holding
    if holding is not None : holding.position = block_clicked
    if holding is not None : move_rule()

def move_rule():
    global holding,block_size,valid_blocks,opponet_piece_in_path
    b = block_size
    valid_blocks = []
    
    x = holding.position[0]
    y = holding.position[1]

    if holding.color == 0 :
        match holding.type:
            case 0: #PAWN
                valid_blocks.append([x,y-block_size])
                if y == 460 : valid_blocks.append([x,y-2*block_size])
            case 3: #Rook
                for i in range(8):
                    valid_blocks.append([x,40+block_size*i])
                for i in range(8):
                    valid_blocks.append([40+block_size*i,y])
            case 1: # Knight
                valid_blocks.extend([[x+b,y-2*b],[x+b,y+2*b],[x-b,y+2*b],[x-b,y-2*b],[x-2*b,y+b],[x+2*b,y+b],[x-2*b,y-b],[x+2*b,y-b]])
            case 2: # Bishop
                last = 600
                first = 40
                for i in range(1,9):
                    if not(x+i*b > last or y+i*b > last): valid_blocks.append([x+i*b,y+i*b])
                    if not(x+i*b > last or y-i*b < first): valid_blocks.append([x+i*b,y-i*b])
                    if not(x-i*b < first or y-i*b > last): valid_blocks.append([x-i*b,y-i*b])
                    if not(x-i*b < first or y+i*b < first): valid_blocks.append([x-i*b,y+i*b])
            case 4: # Queen
                last = 600
                first = 40
                for i in range(1,9):
                    if not(x+i*b > last or y+i*b > last): valid_blocks.append([x+i*b,y+i*b])
                    if not(x+i*b > last or y-i*b < first): valid_blocks.append([x+i*b,y-i*b])
                    if not(x-i*b < first or y-i*b > last): valid_blocks.append([x-i*b,y-i*b])
                    if not(x-i*b < first or y+i*b < first): valid_blocks.append([x-i*b,y+i*b])
                for i in range(8):
                    valid_blocks.append([x,40+block_size*i])
                for i in range(8):
                    valid_blocks.append([40+block_size*i,y])
            case 5: # King
                valid_blocks.extend([[x+b,y],[x-b,y],[x,y+b],[x,y-b]])
        opponet_piece_in_path = [] # Opponent piece in path
        opponent_all_positions = [p.position for p in piece.all_pieces if p.color==1]
        for path in valid_blocks:
            if path in opponent_all_positions:
                opponet_piece_in_path.append(path)
        print(opponet_piece_in_path)
create_pieces()
valid_blocks = []
opponet_piece_in_path = []
game_loop()