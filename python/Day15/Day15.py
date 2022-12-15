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

def eligible_list(manhattan_list, sensor_list, extra=1):
    eligible_list = []
    # Crawl along one side of the diamond edge and add those points to the eligible list
    for dist_idx, distance in enumerate(tqdm(manhattan_list)):
        new_list = []
        start = [sensor_list[dist_idx][0], sensor_list[dist_idx][1] - distance - extra]
        dist = distance + extra
        new_list.append(start)
        new_list.append([start[0], start[1]+ 2*dist])
        for flip_idx in range(1, dist+1):
            dist -= 1
            curr = [start[0]+1, start[1]+1]

            new_list.append(curr)
            new_list.append([curr[0], curr[1]+2 * dist])
            new_list.append([curr[0] - (2 * flip_idx), curr[1]+(2 * dist)])
            new_list.append([curr[0] - (2 * flip_idx), curr[1]])

            start = curr


        eligible_list += new_list

    return eligible_list

def loop(manhattan_list, sensor_list, beacon_list, max_x, y_line):
    count = 0
    exclude = len(set(list(numpy.where(beacon_list[1] == y_line)[0]))) # Remove number of beacons
    for index in trange(max_x[0], max_x[1]):
        for sensor_idx in range(0, len(manhattan_list)):
            if manhattan([index, y_line], sensor_list[sensor_idx]) <= manhattan_list[sensor_idx]:
                count += 1
                break
    return count - exclude

def loop2(manhattan_list, sensor_list, test_points, range_x, range_y):
    for [test_x, test_y] in tqdm(test_points):
        x_idx = test_x
        y_idx = test_y
        flag = []
        for sensor_idx in range(0, len(manhattan_list)):
            if manhattan([x_idx, y_idx], sensor_list[sensor_idx]) <= manhattan_list[sensor_idx]:
                flag.append(1)
            else:
                flag.append(0)
        if not any(flag) and \
                (x_idx < range_x[1]) and (x_idx > range_x[0]) and \
                (y_idx < range_y[1]) and (y_idx > range_y[0]):
            return x_idx, y_idx
    return None, None

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
    sensor += offset
    beacon += offset
    manhattan_list, min_x, max_x = determine_manhattan_list(sensor, beacon)

    test_points = eligible_list(manhattan_list, sensor, 1)
    answer_x, answer_y = loop2(manhattan_list, sensor, test_points, range_x, range_y)
    answer2 = calc_distress_freq(answer_x, answer_y)
    print(f'The beacon in ({answer_x}, {answer_y}) have a score of {answer2}.')


if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())