import pygame
import sys

pygame.init()

height,width , border = 700,1000, 40  # put dimensions in multiple of 8
win = pygame.display.set_mode((width,height))

white = (255,255,255)

block_size = 70 # size of a block , also of images

rook = pygame.image.load("images/black-rook.png")
rook = pygame.transform.scale(rook, (block_size, block_size))

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
    
    # Drawing Pieces
    
    #win.blit(rook, (0,0))

    # Texts
    alpha = ["a","b","c","d","e","f","g","h"]
    font = pygame.font.SysFont('comicsans', 15, True)
    for i,x in enumerate(range(border,border+block_size*8,block_size)):
        text = font.render(alpha[i], 1,(black))
        win.blit(text,(x+block_size/3,border+block_size*8))
    for i,y in enumerate(reversed(range(border,border+block_size*8,block_size))):
        text = font.render(str(i+1), 1,(black))
        win.blit(text,(border-13,y+block_size/3))




def inputs():  # Take all inputs of player
    for event in pygame.event.get():
            if event.type == pygame.QUIT:      # Check if you player clicked X to close window
                pygame.quit()
                sys.exit()

game_loop()