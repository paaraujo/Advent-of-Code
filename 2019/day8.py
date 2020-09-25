from collections import defaultdict
from operator import itemgetter
import matplotlib.pyplot as plt

def part1():
    with open('inputs/day8.txt') as f:
        seq = f.read().rstrip('\n')
        w = 25
        t = 6
        num_pixels = w * t
        layers  = [seq[i:i+num_pixels] for i in range(0,len(seq),num_pixels)]
        labeled = []
        for l in layers:
            d = defaultdict(int)
            for c in l:                
                d[c] += 1
            labeled.append(d)
        sortedByZeros = sorted(labeled,key=itemgetter('0'))
        numOf1s = sortedByZeros[0]['1']
        numOf2s = sortedByZeros[0]['2']
    return numOf1s*numOf2s

def part2():
    with open('inputs/day8.txt') as f:
        seq = f.read().rstrip('\n')
        w = 25
        t = 6
        num_pixels = w * t
        layers = [seq[i:i+num_pixels] for i in range(0,len(seq),num_pixels)]
        image  = list(layers[0])
        for i in range(1,len(layers)):
            l = list(layers[i])
            for j in range(len(l)):
                if image[j] == '2':
                    image[j] = l[j]
        image = [image[i:i+w] for i in  range(0,len(image),w)]
        image = [list(map(int,i)) for i in image]
        plt.imshow(image,cmap='binary')
    return image

print(part1())
print(part2())