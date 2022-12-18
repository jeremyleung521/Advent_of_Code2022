# Day18.py
#
# First attempt at doing Day 18 of Advent of Code 2022

import sys
sys.path.append("..")

from perf import calc_perf
from tqdm.auto import tqdm, trange
import time

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    coords = [[int(j) for j in i] for i in [line.split(',') for line in read_list]]

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

def gen_neighbors(x, y, z):
    yield [x+1, y, z]
    yield [x-1, y, z]
    yield [x, y+1, z]
    yield [x, y-1, z]
    yield [x, y, z+1]
    yield [x, y, z-1]

def bfs_optimize(input_list, start):
    visited = []

    queue = deque()
    queue.append(start)
    #print(end)
    while queue:
        [x,y,z] = queue.popleft()
        if u not in visited and u not in input_list:
            visited.append(u)

        if min(x,y,z) < -1 or max(x,y,z) > 22:
            return False

        for n in gen_neighbors(x, y, z):
            # print(n)
            # if u in end:
            #     print(f'Shortest path between {start} and {end} is {d[u]} steps.')
            #     return parent, d
            if n not in d and n not in input_list:
                queue.append(n)
    return True


def sub_duplicates_two(input_list):
    count = 6 * len(input_list)
    special = []
    for idx, i_val in enumerate(tqdm(input_list)):
        for jdx, j_val in enumerate(input_list):
            diff = 0
            for kdx in range(3):
                diff += abs(j_val[kdx] - i_val[kdx])
            if diff == 1:
                count -= 1
            if diff < 20 and diff > 1:
                special.append([int((jc + ic) / 2) for jc, ic in zip(i_val, j_val)])

    print(len(special))

    excl_special = []
    [excl_special.append(i) for i in tqdm(special) if (i not in excl_special and i not in input_list)]

    return count, excl_special

def check_special(input_list, special_list):
    identity = [[1,0,0], [0,1,0],[0,0,1]]
    real_special_list = []
    not_too_special = []
    count = 0
    for special in tqdm(special_list):
        counter = 0
        for check in identity:
            for multiplicity in range(1,10):
                if list(map(int.__sub__, special, multiplicity * check)) in input_list:
                    counter += 1
                    break
        for check in identity:
            for multiplicity in range(1,10):
                if list(map(int.__add__, special, multiplicity * check)) in input_list:
                    counter += 1
                    break

        if counter == 6 and special not in input_list:
            # count += 6
            real_special_list.append(special)


    count = sub_duplicates(real_special_list)


    return count, real_special_list



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
    answer, special = sub_duplicates_two(coords)

    # print(special)

    print(len(special))
    #diff, real_special = check_special(coords, special)
    # print(real_special)
    diff = 0
    for val in special:
        if bfs_optimize(corrds, val):
            diff += 1

    print(f'{answer - diff} number of sides.')
    print(f'{real_special} are trapped.')


if __name__ == "__main__":
    ## Part 1
    # calc_perf(main())

    ## Part 2
    startTime = time.perf_counter()
    calc_perf(main2())
    print(f'{time.perf_counter() - startTime} sec.')
