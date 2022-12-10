# Day10.py
#
# First attempt at doing Day 10 of Advent of Code 2022

import sys
sys.path.append("..")

from perf import calc_perf

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    read_list = [i.split(' ') for i in read_list]

    # print(read_list)
    return read_list

def loop_commands(input_list, track_list):
    count = 1
    queue = 0
    jdx = 0
    save = []
    for idx in range(1, int(len(input_list)*2+1)):
        if queue != 0:
            count += queue
            queue = 0
        else:
            if jdx < len(input_list) and input_list[jdx][0] == 'addx':
                queue = int(input_list[jdx][1])
            jdx += 1
        #print(count)
        if idx in track_list:
            print(idx+1, count, (idx+1) * count)
            save.append((idx+1) * count)

    return save

def draw_pixel(input_list, track_list):
    count = 1
    queue = 0
    jdx = 0 # readline rows)
    display = []
    for i in range(0,240):
        display.append(' ')

    for idx in range(1, 241): #int(len(input_list)*2+1)):
        if abs(count - ((idx -1)%40)) <= 1:
            display[(idx-1)] = '#'
        else:
            display[(idx-1)] = '.'

        if queue != 0:
            count += queue
            queue = 0
        else:
            if jdx < len(input_list) and input_list[jdx][0] == 'addx':
                queue = int(input_list[jdx][1])
            jdx += 1

    string = ''
    for j in range(1, 241):
        if j % 40 == 0:
            string += f'{display[j-1]}\n'
        else:
            string += display[j-1]

    print(string)

def main():
    ## Part 1
    # b = read_input("Day10_test_input.txt")
    # b = read_input("Day10_test_input2.txt")
    b = read_input("Day10_input.txt")
    # loop_commands(b, [i for i in range(0, 5)])
    check = [19 + i*40 for i in range(0, 6)]
    answer = loop_commands(b, check)

    print(f'{sum(answer)}')

def main2():
    # Part 2
    # a = read_input("Day10_test_input2.txt")
    a = read_input("Day10_input.txt")
    check = [19 + i*40 for i in range(0, 6)]
    draw_pixel(a, check)


if __name__ == "__main__":
    ## Part 1
    # calc_perf(main())

    ## Part 2
    calc_perf(main2())
