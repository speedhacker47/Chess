from classes import *

def get_position(reset=False):
    list = []
    for i in piece.all_pieces:
        temp = [i.type,i.color,i.position]
        list.append(temp)
    return list
