# Day13.py
#
# First attempt at doing Day 13 of Advent of Code 2022

import sys
sys.path.append("..")

from perf import calc_perf
from ast import literal_eval
from functools import cmp_to_key

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    count = read_list.count('')
    for idx in range(0, count):
        read_list.remove('')

    final_list = [literal_eval(i) for i in read_list]

    return final_list


def compare(A,B):
    if A < B:
        return 1  # pass
    elif A > B:
        return 0  # fail
    elif A == B:
        return -1  # continue

def evaluate(a,b):
    # print(f'comparing: {a},{b}')
    if type(a) is int and type(b) is int:
        a, b = [a], [b]
    elif type(a) is int and type(b) is list:
        a = [a]
    elif type(a) is list and type(b) is int:
        b = [b]
    for A, B in zip(a, b):
        # print(f'comparing after zip: {A},{B}')
        if type(A) is int and type(B) is int:
            status = compare(A, B)
            # print(f'status: {status}')
            if status == 1 or status == 0:
                return status
            else:
                continue
        elif type(A) is int and type(B) is list:
            A = [A]
            return evaluate(A, B)
        elif type(A) is list and type(B) is int:
            B = [B]
            return evaluate(A, B)
        elif type(A) is list and type(B) is list:
            for pair in zip(A, B):
                status = evaluate(pair[0], pair[1])
                if status == 1 or status == 0:
                    return status
        if len(A) < len(B):
            return 1  # pass
        elif len(A) > len(B):
            return 0  # fail
        else:
            continue
    if len(a) < len(b):
        return 1  # pass
    elif len(a) > len(b):
        return 0  # fail


def count_indices(input_list):
    success = []
    for idx, line in enumerate(input_list):
        if line == [[2]] or line == [[6]]:
            success.append(idx+1)

    return success


def grab_first_element(input_list, count=0):
    try:
        if input_list == [[2]]:
            return 1.9
        if input_list == [[6]] and count == 0:
            return 5.9
        if type(input_list[0]) is int:
            return input_list[0] + count
        else:
            return grab_first_element(input_list[0], count=count+0.1)
    except IndexError:
        return -1


def main():
    ## Part 1
    # b = read_input("Day13_test_input.txt")
    b = read_input("Day13_input.txt")

    correct = []
    for idx, (A,B) in enumerate(zip(b[::2],b[1::2])):# Each pair of packets
        # print(A,B)
        status = evaluate(A,B)
        if status == 1:
            correct.append(idx +1)
        # print(status)
        # print(f'success:{correct}')
    answer = sum(correct)
    print(f'Sum of packets in right order is {answer}.')

def main2():
    # Part 2
    # a = read_input("Day13_test_input2.txt")
    a = read_input("Day13_input2.txt")

    sort_index = []
    for line in a:
        sort_index.append(grab_first_element(line))

    sorted_list = [x for _,x in sorted(zip(sort_index,a), key=lambda pair: pair[0])]

    success = count_indices(sorted_list)

    answer2 = 1
    for val in success:
        answer2 *= val

    print(f'Product of Divider Packet Indices is {answer2}.')



if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
