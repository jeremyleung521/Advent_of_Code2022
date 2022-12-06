# Day6.py
#
# First attempt at doing Day 6 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf

def read_input(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()


def calc_terms(input, num_len):
    for idx in range(num_len-1, len(input)):
        if len(set(input[idx-num_len:idx])) == num_len:
            return idx



def main():
    ## Part 1
    # For Testing
    # b = read_input("Day6_test_input.txt")
    b = read_input("Day6_input.txt")
    for j in b:
        answer = calc_terms(j,4)
        print(f'After character {answer}.')


def main2():
    # Part 2
    # a = read_input("Day6_test_input.txt")
    a = read_input("Day6_input.txt")
    for j in a:
        answer = calc_terms(j,14)
        print(f'After character {answer}.')


if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
