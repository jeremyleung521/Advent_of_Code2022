# Day8.py
#
# First attempt at doing Day 8 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    read_list = numpy.asarray([[x.split() for x in i] for i in read_list], dtype=int)

    return read_list

def check_if_visible(input_list, x_pos, y_pos):
    check = input_list[y_pos,x_pos]
    if numpy.all(input_list[:y_pos, x_pos] < check) or \
            numpy.all(input_list[y_pos+1:, x_pos] < check) or \
            numpy.all(input_list[y_pos, :x_pos] < check) or \
            numpy.all(input_list[y_pos, x_pos+1:] < check):
        return 1
    return 0

def count_trees(input_list):
    x_shape, y_shape = input_list.shape[0], input_list.shape[1]
    count = 2 * x_shape + 2 * y_shape - 4 #Perimeter trees, minus four overlapping corners

    # Loop through all trees
    for y in range(1, y_shape-1):
        for x in range(1, x_shape-1):
            count += check_if_visible(input_list,x,y)

    return count

def check_visible_trees(input_list, x_pos, y_pos):
    check = input_list[y_pos,x_pos]
    final_count = 1

    count = 0
    for height in reversed(input_list[:y_pos, x_pos]):
        count += 1
        if height >= check:
            break
    final_count *= count

    count = 0
    for height in reversed(input_list[y_pos, :x_pos]):
        count += 1
        if height >= check:
            break
    final_count *= count

    count = 0
    for height in input_list[y_pos+1:, x_pos]:
        count += 1
        if height >= check:
            break
    final_count *= count

    count = 0
    for height in input_list[y_pos, x_pos+1:]:
        count += 1
        if height >= check:
            break
    final_count *= count

    return final_count

def calc_score(input_list):
    x_shape, y_shape = input_list.shape[0], input_list.shape[1]
    curr_val = 0
    # Loop through all trees
    for y in range(1, y_shape-1):
        for x in range(1, x_shape-1):
            score = check_visible_trees(input_list, x, y)
            if score > curr_val:
                curr_val = score

    return curr_val

def main():
    ## Part 1
    # b = read_input("Day8_test_input.txt")
    b = read_input("Day8_input.txt")
    answer = count_trees(b)
    print(f'{answer} trees are visible.')

def main2():
    # Part 2
    # a = read_input("Day8_test_input.txt")
    a = read_input("Day8_input.txt")
    answer2 = calc_score(a)
    print(f'Best view has a score of {answer2}.')

if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
