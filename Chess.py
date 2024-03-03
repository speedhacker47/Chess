import pygame
import sys

height,width , border = 700,1000, 40  # put dimensions in multiple of 8
win = pygame.display.set_mode((width,height))

white = (255,255,255)

block_size = 70 # size of a block , also of images

rook = pygame.image.load("images/black-rook.png")
rook = pygame.transform.scale(rook, (block_size, block_size))



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
    
    # Drawing Pieces
    
    win.blit(rook, (0,0))




def inputs():  # Take all inputs of player
    for event in pygame.event.get():
            if event.type == pygame.QUIT:      # Check if you player clicked X to close window
                pygame.quit()
                sys.exit()

game_loop()