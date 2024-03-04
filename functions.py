
# Some Functions are written here , to make main code less messed up

from classes import *
import variables

def get_position(reset=False):
    list = []
    for i in piece.all_pieces:
        temp = [i.type,i.color,i.position]
        list.append(temp)
    return list

def check_clicked(mouse):
    block_num = []
    block_pos = []
    block_size = 70
    for i,next_point in enumerate(variables.inside_block_positions):
        if mouse[0] < next_point:
            block_num.append(i+1)
            block_pos.append(next_point-block_size)
            break
    for i,next_point in enumerate(variables.inside_block_positions):
        if mouse[1] < next_point:
            block_num.append(i+1)
            block_pos.append(next_point-block_size)
            break
    return block_pos


