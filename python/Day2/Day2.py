# Day2.py
#
# First attempt at doing Day 2 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf

chose_dict = {'X': 1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C': 3} # (X,A) is rock, (Y,B) is paper, (Z,C) is scissors
point_dict = {0:3, 1:0, 2:6, -1:6, -2: 0} # Diff 0 == Draw (3 points), Diff 2 or -1 == Win (6 points), Diff 1 or -2 == Lose (0 points)
condition_dict = {'XA':'Z', 'XB':'X', 'XC':'Y', 'YA':'X', 'YB':'Y', 'YC':'Z', 'ZA':'Y', 'ZB':'Z', 'ZC':'X' } # X: Lose, Y: Draw, Z:Win


def loop_point(input_list):
    count = 0
    for pair in input_list:
        count += chose_dict[pair[1]]
        count += point_dict[chose_dict[pair[0]]-chose_dict[pair[1]]]
    return count

def fig_move(input_list):
    count = 0
    for idx, pair in enumerate(input_list):
        input_list[idx,1] = condition_dict[pair[1]+pair[0]]
    return input_list

def main():
    ## Part 1
    #b = numpy.loadtxt("Day2_test_input.txt", dtype=str)
    b = numpy.loadtxt("Day2_input.txt", dtype=str)
    answer = loop_point(b)
    print(f'I won {answer} number of points following this guide.')

def main2():
    # Part 2
    #a = numpy.loadtxt("Day2_test_input.txt", dtype=str)
    a = numpy.loadtxt("Day2_input.txt", dtype=str)
    answer2 = fig_move(a)
    answer2 = loop_point(answer2)
    print(f'I won {answer2} number of points following this guide.')


if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
