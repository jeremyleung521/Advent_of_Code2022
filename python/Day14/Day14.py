# Day14.py
#
# First attempt at doing Day 14 of Advent of Code 2022

import sys
sys.path.append("..")
import numpy

from perf import calc_perf
from ast import literal_eval

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    split_list = [line.split(' -> ') for line in read_list]

    processed_list = []
    for line in split_list:
        processed_list.append([(literal_eval(coord)) for coord in line])

    # Getting Min/Max values.
    combined_list = [(literal_eval(coord)) for line in read_list for coord in line.split(' -> ')]

    sort_x = sorted(combined_list, key=lambda x: x[0])
    sort_y = sorted(combined_list, key=lambda x: x[1])

    x_bound = (sort_x[0][0], sort_x[-1][0])
    y_bound = (sort_y[0][1], sort_y[-1][1])

    return processed_list, x_bound, y_bound

def propagate(curr_status, offset):
    pos = [500-offset,0]
    continue_flag = True
    while continue_flag:
        try:
            if curr_status[pos[0], pos[1] + 1] == '.':
                pos[1] += 1
            elif curr_status[pos[0] - 1, pos[1] + 1] == '.':
                pos[0] -= 1
                pos[1] += 1
            elif curr_status[pos[0] + 1, pos[1] + 1] == '.':
                pos[0] += 1
                pos[1] += 1
            else:
                continue_flag = False
        except IndexError:
            return [-1, -1]

    return pos

def gen_initial_config(input_list, x_bound, y_bound):
    offset = x_bound[0]
    config_array = numpy.full(((x_bound[1]-x_bound[0]+1),y_bound[1]+1), '.')

    for line in input_list:
        for start, end in zip(line, line[1:]):
            for x_coord in range((start[0]-offset), end[0]-offset+1):
                for y_coord in range(start[1], end[1]+1):
                    config_array[x_coord, y_coord] = '#'
            for x_coord in range((start[0]-offset), end[0]-offset-1, -1):
                for y_coord in range(start[1], end[1]-1, -1):
                    config_array[x_coord, y_coord] = '#'

    return config_array, offset

def loop(input_array, offset, target):
    count = 0
    new_pos = None
    while new_pos != [-1, -1]:
        count += 1
        new_pos = propagate(input_array, offset)
        if new_pos == [500-offset,0]:
            return count, input_array
        input_array[tuple(new_pos)] = 'o'
        # print(input_array.T)

    return count, input_array


def main():
    ## Part 1
    #input, min_coord, max_coord = read_input("Day14_test_input.txt")
    input, min_coord, max_coord = read_input("Day14_input.txt")

    config_array, offset = gen_initial_config(input, min_coord, max_coord)
    # print(config_array.T)
    # print(config_array.shape)
    answer, final_config = loop(config_array, offset, max_coord[1])
    # print(final_config.T)
    print(f'It takes {answer-1} cycles for a steady state.')

def main2():
    # Part 2
    # input, xlim, ylim = read_input("Day14_test_input.txt")
    input, xlim, ylim = read_input("Day14_input.txt")

    xlim = (xlim[0]-500, xlim[1]+500)
    ylim = (ylim[0], ylim[1]+2)

    inf_start = (xlim[0],ylim[1])
    inf_end = (xlim[1],ylim[1])

    input.append([inf_start, inf_end])

    config_array, offset = gen_initial_config(input, xlim, ylim)
    answer2, final_config = loop(config_array, offset, ylim[1])
    print(f'It takes {answer2} cycles for a steady state.')

if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
