# Day6.py
#
# First attempt at doing Day 6 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.readlines()

    return read_list

def calc_terms(input):
    for idx in range(3, len(input)):
        if len(set(input[idx-4:idx])) == 4:
            index = idx
            break

    return index

def calc_terms_fourteen(input):
    for idx in range(13, len(input)):
        if len(set(input[idx-14:idx])) == 14:
            index = idx
            break

    return index

def main():
    ## Part 1
    # For Testing
    # b = read_input("Day6_test_input.txt")
    b = read_input("Day6_input.txt")
    for j in b:
        answer = calc_terms(j)
        print(f'After character {answer}.')


def main2():
    # Part 2
    # a = read_input("Day6_test_input.txt")
    a = read_input("Day6_input.txt")
    for j in a:
        answer = calc_terms_fourteen(j)
        print(f'After character {answer}.')


if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
