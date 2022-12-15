# Day15.py
#
# First attempt at doing Day 15 of Advent of Code 2022

import sys

sys.path.append("..")
import numpy

from perf import calc_perf
from tqdm.auto import tqdm, trange


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    split_list = [i.replace(', y=', 'x=').replace(': ', 'x=').split('x=') for i in read_list]

    sensor_list = numpy.asarray([[int(i[1]), int(i[2])] for i in split_list])
    beacon_list = numpy.asarray([[int(i[4]), int(i[5])] for i in split_list])

    combined_list = numpy.append(sensor_list, beacon_list, axis=0)

    sort_x = sorted(combined_list, key=lambda x: x[0])
    sort_y = sorted(combined_list, key=lambda x: x[1])

    x_bound = (sort_x[0][0], sort_x[-1][0])
    y_bound = (sort_y[0][1], sort_y[-1][1])

    if x_bound[0] < 0:
        x_offset = x_bound[0]
    else:
        x_offset = 0

    if y_bound[0] < 0:
        y_offset = y_bound[0]
    else:
        y_offset = 0

    offset = (x_offset, y_offset)

    sensor_list -= offset
    beacon_list -= offset

    return sensor_list, beacon_list, x_bound, y_bound, offset


def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


def calc_distress_freq(x,y):
    return (x * 4000000) + y


def determine_manhattan_list(sensor_list, beacon_list):
    manhattan_list = []
    min, max = 0, 0
    for sensor, beacon in zip(sensor_list, beacon_list):
        val = manhattan(sensor, beacon)
        manhattan_list.append(val)
        if sensor[0] - val < min:
            min = sensor[0] - val
        if sensor[0] + val > max:
            max = sensor[0] + val

    return manhattan_list, min, max

def eligible_list(manhattan_list, sensor_list, beacon_list):
    for

def loop(manhattan_list, sensor_list, beacon_list, max_x, y_line):
    count = 0
    exclude = len(set(list(numpy.where(beacon_list[1] == y_line)[0]))) # Remove number of beacons
    for index in trange(max_x[0], max_x[1]):
        for sensor_idx in range(0, len(manhattan_list)):
            if manhattan([index, y_line], sensor_list[sensor_idx]) <= manhattan_list[sensor_idx]:
                count += 1
                break
    return count - exclude

def loop2(manhattan_list, sensor_list, beacon_list, range_x, range_y, offset):
    min_range_x_offset = range_x[0] - offset[0]
    max_range_x_offset = range_x[1] - offset[0]
    min_range_y_offset = range_y[0] - offset[1]
    max_range_y_offset = range_y[1] - offset[1]

    for x_idx in trange(min_range_x_offset, max_range_x_offset):
        for y_idx in trange(min_range_y_offset, max_range_y_offset):
            flag = []
            for sensor_idx in range(0, len(manhattan_list)):
                if manhattan([x_idx, y_idx], sensor_list[sensor_idx]) <= manhattan_list[sensor_idx]:
                    flag.append(1)
                else:
                    flag.append(0)
            if not any(flag):
                return x_idx + offset[0], y_idx + offset[1]
    return None

def main():
    ## Part 1
    # y_line = 10
    # sensor, beacon, xlim, ylim, offset = read_input("Day15_test_input.txt")
    y_line = 2000000
    sensor, beacon, xlim, ylim, offset = read_input("Day15_input.txt")
    manhattan_list, min_x, max_x = determine_manhattan_list(sensor, beacon)
    answer = loop(manhattan_list, sensor, beacon, [min_x, max_x], y_line)
    print(f'There are {answer} impossible spots in y={y_line}.')


def main2():
    # Part 2
    # range_x, range_y = [0, 20], [0, 20]
    # sensor, beacon, xlim, ylim, offset = read_input("Day15_test_input.txt")
    range_x, range_y = [0, 4000000], [0, 4000000]
    sensor, beacon, xlim, ylim, offset = read_input("Day15_input.txt")
    manhattan_list, min_x, max_x = determine_manhattan_list(sensor, beacon)
    # print(manhattan_list)

    answer_x, answer_y = loop2(manhattan_list, sensor, beacon, range_x, range_y, offset)
    answer2 = calc_distress_freq(answer_x, answer_y)
    print(f'There beacon in ({answer_x}, {answer_y}) have a score of {answer2}.')


if __name__ == "__main__":
    ## Part 1
    # calc_perf(main())

    ## Part 2
    calc_perf(main2())