# Day3.py
#
# First attempt at doing Day 3 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf

def split_list(read_list):
    split_list = []
    for line in read_list:
        split_list.append([line[:int(len(line)/2)], line[int(len(line)/2):]])

    return split_list

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return read_list

def gen_dict():
    uppercase_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_list = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}
    for alphabeta in uppercase_list:
        dict[alphabeta] = ord(alphabeta) - 38

    for alphabeta in lowercase_list:
        dict[alphabeta] = ord(alphabeta) - 96

    return dict

def map_dict(input_list, dict):
    new_list = []
    for line in input_list:
        new_list.append(dict[line.pop()])
    total = sum(new_list)

    return new_list, total

def return_top3(input_list):
    every_three = int(len(input_list)/3)

    common_list = [(set([chara for chara in input_list[3*jdx]
                         if (chara in input_list[3*jdx+1] and chara in input_list[3*jdx+2])]))
                   for jdx in range(0,every_three)]

    assert len(common_list) == every_three

    return common_list

def main():
    reference = gen_dict()

    ## Part 1
    # input_list = read_input("Day3_test_input.txt")
    read_list = read_input("Day3_input.txt")
    input_list = split_list(read_list)
    common_list = [(set([chara for chara in input[0] if chara in input[1]])) for input in input_list]
    assert len(common_list) == len(input_list)
    answer = map_dict(common_list, reference)

    print(f'Sum of priority is {answer[1]}.')
    # print(f'The list of priorities are {answer[0]}.')

def main2():
    reference = gen_dict()

    # Part 2
    #input_list = read_input("Day3_test_input.txt")
    input_list = read_input("Day3_input.txt")
    common_list = return_top3(input_list)
    answer2 = map_dict(common_list, reference)
    print(f'Sum of priority is {answer2[1]}.')
    # print(f'The list of priorities are {answer2[0]}.')

if __name__ == "__main__":

    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
