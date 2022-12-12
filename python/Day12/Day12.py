# Day12.py
#
# First attempt at doing Day 12 of Advent of Code 2022

import numpy
import sys
sys.path.append("..")

from perf import calc_perf
from collections import deque

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_array = []
    for line in read_list:
        final_array.append([ord(chara) for chara in line])
    final_array = numpy.array(final_array)

    start = numpy.where(final_array==83)
    end = numpy.where(final_array==69)

    final_array[start[0][0], start[1][0]] = 97
    final_array[end[0][0], end[1][0]] = 122
    return final_array, (start[0][0], start[1][0]), (end[0][0], end[1][0])

def calc_possible_moves(input_array):
    # cost_array = numpy.zeros((len(a), len(a[0])))
    adj_array = dict({})
    index = [(-1,0),(1,0), (0,-1),(0,1)]
    for row in range(0, len(input_array)):
        for column in range(0, len(input_array[0])):
            candidates = []
            for diff in index:
                # If neighbour diff is too high not working
                try:
                    check = (row+diff[0],column+diff[1])
                    if any(i<0 for i in check):
                        pass
                    elif input_array[row+diff[0],column+diff[1]] <= input_array[row,column] + 1:
                        candidates.append((row + diff[0], column + diff[1]))
                except IndexError:
                    pass

            adj_array[(row,column)] = candidates

    return adj_array

def calc_possible_moves_inverse(input_array):
    # cost_array = numpy.zeros((len(a), len(a[0])))
    adj_array = dict({})
    index = [(-1,0), (1,0), (0,-1), (0,1)]
    for row in range(0, len(input_array)):
        for column in range(0, len(input_array[0])):
            candidates = []
            for diff in index:
                # If neighbour diff is too high not working
                try:
                    check = (row+diff[0], column+diff[1])
                    if any(i<0 for i in check):
                        pass
                    elif input_array[row,column] - 1 <= input_array[row+diff[0],column+diff[1]]:
                        candidates.append((row + diff[0], column + diff[1]))
                except IndexError:
                    pass

            adj_array[(row, column)] = candidates

    return adj_array


def find_possible_starts(input_array):
    all_a = []
    for row in range(0, len(input_array)):
        for column in range(0, len(input_array)):
            if input_array[row,column] == ord('a'):
                all_a.append((row, column))

    return all_a


def bfs_optimize(adj_array, start_x, start_y, end):
    parent = {(start_x,start_y): None}
    d = {(start_x, start_y): 0}
    visited = []

    queue = deque()
    queue.append((start_x, start_y))
    #print(end)
    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.append(u)
        for n in adj_array[u]:
            # print(n)
            if u in end:
                print(d[u])
                return parent, d
            if n not in d:
                if n not in parent:
                    parent[n] = []
                parent[n].append(u)
                d[n] = d[u] + 1
                queue.append(n)
    return parent, d

def main():
    ## Part 1
    # b, start_index, end_index = read_input("Day12_test_input.txt")
    b, start_index, end_index = read_input("Day12_input.txt")
    adj_array = calc_possible_moves(b)

    # print(adj_array)

    parent, dist = bfs_optimize(adj_array, start_index[0], start_index[1], [end_index])

    # print(parent,dist)

def main2():
    # Part 2
    # a, start_index, end_index = read_input("Day12_test_input.txt")
    a, start_index, end_index = read_input("Day12_input.txt")
    adj_array = calc_possible_moves_inverse(a)

    possible_starts = find_possible_starts(a)
    # print(adj_array)

    parent, dist = bfs_optimize(adj_array, end_index[0], end_index[1], possible_starts)

if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
