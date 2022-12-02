# Day2.py
#
# First attempt at doing Day 2 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf

chose_dict = {'X': 1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C': 3} # (X,A) is rock, (Y,B) is paper, (Z,C) is scissors
point_dict = {0:3, 1:0, 2:6, -1:6, -2: 0} # Diff 0 == Draw (3 points), Diff 2 or -1 == Win (6 points), Diff 1 or -2 == Lose (0 points)
condition_dict = {'X':[]} # X: Lose, Y: Draw, Z:Win


def loop_point(input_list):
    count = 0
    for pair in input_list:
        count += chose_dict[pair[1]]
        count += point_dict[chose_dict[pair[0]]-chose_dict[pair[1]]]
    return count

def fig_move(input_list):
    count = 0
    for pair in input_list:
        
        # X: Lose, Y: Draw, Z: Win
    
    
    return input_list

def main():
    ## Part 1
    #b = numpy.loadtxt("Day2_test_input.txt", dtype=str)
    b = numpy.loadtxt("Day2_input.txt", dtype=str)
    answer = loop_point(b)
    print(f'I won {answer} number of points following this guide.')

def main2():
    # Part 2
    # a = read_input("Day2_test_input.txt")
    #a = read_input("Day2_input.txt")
    #answer2 = return_top3(a)
    #print(f'Elves {answer2[1] + 1} have {answer2[0]} calories worth of food.')
    pass

if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    #calc_perf(main2())
