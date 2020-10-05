from intcode import Intcode
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
    
def get_map(seq,input_instruction):
    computer = Intcode()
    computer.initialize_memory(seq)
    computer.set_pointer(0)
    mapping = defaultdict(int)
    # initial position
    color, direc = computer.calculate(input_instruction)
    curr_pos = [0,0]
    curr_ang = 0
    # running Intcode
    while computer.pointer != -1:
        mapping[str(curr_pos[0])+','+str(curr_pos[1])] = color
        if direc == 0:
            # left 90 degrees
            curr_ang += 90
        elif direc == 1:
            # right 90 degrees
            curr_ang -= 90
        # adjusting to a range from 0-360
        if curr_ang == -90:
            curr_ang = 270
        elif curr_ang == 360:
            curr_ang = 0
        # moving one step in the defined direction
        if curr_ang == 0:
            curr_pos = [curr_pos[0]+1,curr_pos[1]]
        elif curr_ang == 90:
            curr_pos = [curr_pos[0],curr_pos[1]+1]
        elif curr_ang == 180:
            curr_pos = [curr_pos[0]-1,curr_pos[1]]
        elif curr_ang == 270:
            curr_pos = [curr_pos[0],curr_pos[1]-1]
        # getting next coordinates
        color, direc = computer.calculate(mapping[str(curr_pos[0])+','+str(curr_pos[1])])
    return mapping

def part1(input_instruction):
    with open('inputs/day11.txt') as f:
        seq = f.read().rstrip('\n').split(',')
        mapping = get_map(seq,input_instruction) 
    return len(mapping)

def part2(input_instruction):
    with open('inputs/day11.txt') as f:
       seq = f.read().rstrip('\n').split(',')
       mapping = get_map(seq,input_instruction)
       # getting limits
       x_min = int(min(mapping.keys(),key=lambda k: int(k.split(',')[0])).split(',')[0])
       x_max = int(max(mapping.keys(),key=lambda k: int(k.split(',')[0])).split(',')[0])
       y_min = int(min(mapping.keys(),key=lambda k: int(k.split(',')[1])).split(',')[1])
       y_max = int(max(mapping.keys(),key=lambda k: int(k.split(',')[1])).split(',')[1])
       # creating an image
       height = x_max - x_min
       width  = y_max - y_min
       image  = np.zeros((height*2,width*2),dtype=np.uint8)
       # setting the origin
       o_x = height
       o_y = width
       # painting
       for k,v in mapping.items():
           x,y = [int(i) for i in k.split(',')]
           image[o_x+x,o_y+y] = v
       # slicing to get rid of extra pixels
       image = image[o_x+x_min:o_x+x_max+1,o_y+y_min:o_y+y_max+1]
       # rotating the image
       image = np.rot90(image,2)
       # plotting
       plt.imshow(image)
       plt.xticks([])
       plt.yticks([])
    return None

print(part1(0))
print(part2(1))