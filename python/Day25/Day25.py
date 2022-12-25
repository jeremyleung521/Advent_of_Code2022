# Day25.py
#
# First attempt at doing Day 25 of Advent of Code 2022

import time
import numpy


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return read_list

def reverse_map(val):
    unmap_dict = {2: '2', 1: '1', 0: '0', 4: '-', 3: '='}
    string = ''

    while val:
        val, r = divmod(val, 5)
        string += unmap_dict[r]
        if r in {3, 4}:
            val += 1

    return string


def loop(input_list):
    map_dict = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    count_list = [0]
    count = 0

    for string in input_list:
        val = 0
        for idx, digit in enumerate(string[::-1]):
            val += (5 ** idx) * map_dict[digit]
        count += val
        count_list.append(val)

    return count, count_list[1:]


def main():
    ## Part 1
    # b = read_input("Day25_test_input.txt")
    b = read_input("Day25_input.txt")
    answer, count_list = loop(b)
    #print(count_list)
    answer2 = reverse_map(answer)[::-1]

    print(f'Sum is {answer} or {answer2}.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')