# Day23.py
#
# First attempt at doing Day 23 of Advent of Code 2022

import time
import numpy
from operator import add, itemgetter
from collections import deque
from tqdm.auto import tqdm, trange


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    list_of_lists = [[j for j in i] for i in read_list]

    curr_occupied = [(idx, jdx) for idx, i in enumerate(list_of_lists) for jdx, j in enumerate(i) if j == '#']

    n_elves = len(curr_occupied)

    neighbour = dict()

    # print(f'Initialized: {curr_occupied}')

    # N, S, W, E, NE, NW, SE, SW
    directions = numpy.asarray([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)])

    consideration = deque([[0, 4, 5], [1, 6, 7], [2, 5, 7], [3, 4, 6]]) # Checks for N/S/W/E moves
    order = deque([0, 1, 2, 3])  # N, S, W, E

    return list_of_lists, curr_occupied, neighbour, n_elves, directions, consideration, order


def propagate(curr_occupied, neighbour, directions, consideration, order):
    # Refresh Neighbour List
    neighbour.clear()
    for j in curr_occupied:
        neighbour[j] = []

    new_location = {}
    count = 0
    flag = False
    for coord in curr_occupied:
        # Create neighbours map
        check_c = []
        for direction in directions:
            check = tuple(map(add, coord, direction))
            check_c.append(check)
            if check in curr_occupied:
                neighbour[coord].append(check)

        if not neighbour[coord]:  # If no neighbours, just stay in place
            # print('error where')
            count += 1
            new_location[coord] = coord
        else:
            for check_list, output in zip(consideration, order):
                check_check = [check_c[i] for i in check_list]
                if all(coord_c not in curr_occupied for coord_c in check_check):
                    new_location[coord] = tuple(map(add, coord, directions[output]))
                    # print(directions[output])
                    break
            if coord not in new_location.keys():
                # print('error there')
                count += 1
                new_location[coord] = coord

    if count == len(curr_occupied):
        # print('error here')
        flag = True
    # print(new_location)

    # Taking care of duplicates, Reject duplicates
    dupes = {}
    for key, value in new_location.items():
        dupes.setdefault(value, set()).add(key)

    result = [key for key, values in dupes.items() if len(values) > 1]

    for key, value in new_location.items():
        if value in result:
            new_location[key] = key

    # Answers and prep for next iteration
    curr_occupied = list(new_location.values())
    consideration.rotate(-1)
    order.rotate(-1)

    # print(f'New Iteration: {curr_occupied}')

    return new_location, curr_occupied, flag


def find_minmax(curr_occupied, n_elves):
    # print(curr_occupied)
    min_x = min(curr_occupied, key=itemgetter(0))[0]
    min_y = min(curr_occupied, key=itemgetter(1))[1]
    max_x = max(curr_occupied, key=itemgetter(0))[0]
    max_y = max(curr_occupied, key=itemgetter(1))[1]

    list_of_list = []
    for idx in range(min_x, max_x + 1):
        list_of_list.append([])
        for jdx in range(min_y, max_y + 1):
            if (idx, jdx) not in curr_occupied:
                list_of_list[idx - min_x].append('.')
            else:
                list_of_list[idx - min_x].append('#')
    #
    # print(f'New Iteration: \n')
    # for i in list_of_list:
    #     print(f'{i}')
    return (((max_y - min_y) + 1) * ((max_x - min_x) + 1)) - n_elves


def main():
    ## Part 1
    # initialize, curr_occupied, neighbour, n_elves, directions, conditions, order = read_input("Day23_smaller_input.txt")
    # initialize, curr_occupied, neighbour, n_elves, directions, conditions, order = read_input("Day23_test_input.txt")
    initialize, curr_occupied, neighbour, n_elves, directions, conditions, order = read_input("Day23_input.txt")

    for _ in trange(10):
        new_location, curr_occupied, flag = propagate(curr_occupied, neighbour, directions, conditions, order)
        answer = find_minmax(curr_occupied, n_elves)
        if flag is True:
            print(idx)

    print(f'There are {answer} empty spots in the minimum rectangle.')


def main2():
    # Part 2
    # initialize, curr_occupied, neighbour, n_elves, directions, conditions, order = read_input("Day23_smaller_input.txt")
    # initialize, curr_occupied, neighbour, n_elves, directions, conditions, order = read_input("Day23_test_input.txt")
    initialize, curr_occupied, neighbour, n_elves, directions, conditions, order = read_input("Day23_input.txt")

    for idx in trange(1000000):
        new_location, curr_occupied, flag = propagate(curr_occupied, neighbour, directions, conditions, order)
        answer = find_minmax(curr_occupied, n_elves)
        if flag is True:
            print(idx+1)
            answer2 = idx+1
            break

    print(f'It requires {answer2} moves to reach equilibrium.')


if __name__ == "__main__":
    ## Part 1
    # startTime = time.perf_counter()
    # main()
    # print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
