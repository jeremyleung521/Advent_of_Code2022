# Day4.py
#
# First attempt at doing Day 4 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = [line.split(',') for line in f.read().splitlines()]

    return read_list

def check_range(input_list):
    count = 0
    for pair in input_list:
        min1,max1 = pair.pop().split('-')
        min2,max2 = pair.pop().split('-')
        if int(min1) >= int(min2) and int(max1) <= int(max2):
            count += 1
        elif int(min2) >= int(min1) and int(max2) <= int(max1):
            count += 1
    assert count <= len(input_list)

    return count

def check_range2(input_list):
    count = 0
    for pair in input_list:
        min1,max1 = pair.pop().split('-')
        min2,max2 = pair.pop().split('-')
        if int(min1) >= int(min2) and int(min1) <= int(max2):
            count += 1
        elif int(max1) >= int(min2) and int(max1) <= int(max2):
            count += 1
        elif int(min2) >= int(min1) and int(min2) <= int(max1):
            count += 1
        elif int(max2) >= int(min1) and int(max2) <= int(max1):
            count += 1
    assert count <= len(input_list)

    return count

def main():
    ## Part 1
    # b = read_input("Day4_test_input.txt")
    b = read_input("Day4_input.txt")
    answer = check_range(b)
    print(f'There are {answer} number of overlap assignments.')

def main2():
    # Part 2
    # a = read_input("Day4_test_input.txt")
    a = read_input("Day4_input.txt")
    answer2 = check_range2(a)
    print(f'There are {answer2} number of overlap assignments.')

if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
