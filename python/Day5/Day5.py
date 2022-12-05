# Day5.py
#
# First attempt at doing Day 5 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    for idx, val in enumerate(read_list):
        if val == '':
            break_num = idx

    listA, listB = read_list[:break_num], read_list[break_num+1:]
    max_val = int(max(listA[-1]))
    movement = []

    stack_list = [[charac] for charac in listA[-2][1:4*max_val:4]]

    for string in listA[-3::-1]:
        for idx, charac in enumerate(string[1:4*max_val:4]):
            if charac.isalpha():
                stack_list[idx].append(charac)

    # Sort out all moves into a list
    for j in listB:
        break_list = j.split(' ')
        movement.append([int(break_list[1]), int(break_list[3]), int(break_list[5])])

    return stack_list, movement

def move_things(input_list, movement):
    for moves in movement:
        # print(moves)
        for idx in range(moves[0],0,-1):
            crate = input_list[moves[1]-1].pop()
            input_list[moves[2]-1].append(crate)
        # print(input_list)

    return input_list

def move_things_crane(input_list, movement):
    for moves in movement:
        # print(moves)
        for idx in range(moves[0],0,-1):
            crate = input_list[moves[1]-1].pop(-idx)
            input_list[moves[2]-1].append(crate)
        # print(input_list)

    return input_list

def read_final_message(input_list):
    message = ''
    for stacks in input_list:
        message += stacks[-1]

    return message

def main():
    ## Part 1
    #stack_list, movement = read_input("Day5_test_input.txt")
    stack_list, movement = read_input("Day5_input.txt")
    stack_list = move_things(stack_list, movement)
    message = read_final_message(stack_list)
    print(f'Final Message is {message}.')

def main2():
    # Part 2
    # stack_list, movement = read_input("Day5_test_input.txt")
    stack_list, movement = read_input("Day5_input.txt")
    stack_list = move_things_crane(stack_list, movement)
    message2 = read_final_message(stack_list)
    print(f'Final Message is {message2}.')

if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
