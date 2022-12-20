# Day20.py
#
# First attempt at doing Day 20 of Advent of Code 2022

import time
import numpy
from copy import deepcopy
from collections import deque


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_list = [int(i) for i in read_list]

    return final_list


def loop(final_list):
    copy_list = deepcopy(final_list)
    mod = len(copy_list)
    neighbor_list = dict()
    for idx, val in enumerate(copy_list):
        neighbor_list[val] = [idx, copy_list[(idx-1) % mod], copy_list[(idx+1) % mod]]

    for idx in range(len(copy_list)):
        val = copy_list[idx]
        curr_pos = final_list.index(copy_list[idx]) # This doesn't account for duplicates
        # Doesn't work...
        while True:
            if final_list[(curr_pos-1) % mod] != copy_list[(curr_pos-1) % mod] and \
                final_list[(curr_pos-1) % mod] != copy_list[(curr_pos-1) % mod]:
                curr_pos = final_list.index(copy_list[idx], (curr_pos +1 % mod))
            else:
                break
        if val < 0:
            new_pos = (curr_pos + val) % mod -1
        else:
            new_pos = (curr_pos + val) % mod
        print('new_iter')
        print(curr_pos, new_pos)
        print('looking at: ', val)

        if new_pos == (idx % mod):
            pass
        else:
            final_list.remove(val)
            print(final_list)
            final_list.insert(new_pos, val)
        print(final_list)

def find_character(final_list, n):
    start = final_list.index(0)
    # print(start)
    mod = len(final_list)
    print(len(final_list))
    answer = []
    for i in n:
        answer.append(final_list[(start + i) % mod])

    # print(answer)
    return answer, sum(answer)

def main():
    ## Part 1
    b = read_input("Day20_test_input.txt")
    # b = read_input("Day20_input.txt")
    loop(b)
    answer, sum_answer = find_character(b, [1000, 2000, 3000])
    print(f'Sum of {answer} is {sum_answer}.')


def main2():
    # Part 2
    a = read_input("Day20_test_input.txt")
    # a = read_input("Day20_input.txt")
    answer2 = return_top3(a)
    print(f'Elves {answer2[1] + 1} have {answer2[0]} calories worth of food.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    #startTime = time.perf_counter()
    #main2()
    #print(f'{time.perf_counter() - startTime} sec.')
