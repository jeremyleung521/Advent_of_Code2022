# Day18.py
#
# First attempt at doing Day 18 of Advent of Code 2022

import sys
sys.path.append("..")

from perf import calc_perf
from tqdm.auto import tqdm, trange
import time
from collections import deque

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    coords = set([tuple([int(j) for j in i]) for i in [line.split(',') for line in read_list]])

    return coords

def sub_duplicates(input_list):
    count = 6 * len(input_list)
    for idx, i_val in enumerate(tqdm(input_list)):
        for jdx, j_val in enumerate(input_list):
            diff = 0
            for kdx in range(3):
                diff += abs(j_val[kdx] - i_val[kdx])
            if diff == 1:
                count -= 1

    return count


def bfs_optimize(input_list):

    directions = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))

    xMin, yMin, zMin = [min(point[i] for point in input_list) for i in range(3)]
    xMax, yMax, zMax = [max(point[i] for point in input_list) for i in range(3)]

    queue = deque()
    queue.append((xMin - 1, yMin - 1, zMin - 1))
    visited = set([(xMin - 1, yMin - 1, zMin - 1)])
    surface = 0
    while queue:
        x, y, z = queue.pop()
        for dx, dy, dz in directions:
            if x + dx in range(xMin - 1, xMax + 2) and y + dy in range(yMin - 1, yMax + 2) and z + dz in range(zMin - 1,
                                                                                                               zMax + 2):
                if (x + dx, y + dy, z + dz) in input_list:
                    surface += 1
                elif (x + dx, y + dy, z + dz) not in visited:
                    visited.add((x + dx, y + dy, z + dz))
                    queue.append((x + dx, y + dy, z + dz))

    return surface


def main():
    ## Part 1
    # coords = read_input("Day18_test_input.txt")
    coords = read_input("Day18_input.txt")
    answer = sub_duplicates(coords)

    print(f'{answer} number of sides.')

def main2():
    # Part 2
    # coords = read_input("Day18_test_input.txt")
    coords = read_input("Day18_input.txt")
    answer = bfs_optimize(coords)

    print(f'{answer} number of sides.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
