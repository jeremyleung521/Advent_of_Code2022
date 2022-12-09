# Day9.py
#
# First attempt at doing Day 9 of Advent of Code 2022

import sys
sys.path.append("..")

from perf import calc_perf


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    read_list = [i.split(' ') for i in read_list]

    # print(read_list)
    return read_list

def track_tail(x_pos, y_pos, x, y, x_diff, y_diff):
    if abs(x_pos - x) <= 1 and abs(y_pos - y) <= 1:
        pass
    elif (x_pos == x) or (y_pos == y):
        x_pos += x_diff
        y_pos += y_diff
    else:
        if x > x_pos:
            x_pos += 1
        elif x < x_pos:
            x_pos -= 1
        if y > y_pos:
            y_pos += 1
        elif y < y_pos:
            y_pos -= 1

    return (x_pos, y_pos)

def move_head(direction, x_pos, y_pos, x, y):
    flag = False
    knot_move = (0,0)
    if x_pos == x and y_pos == y:
        flag = True
    if direction == 'U':
        y += 1
        if flag is False:
            (x_pos, y_pos) = track_tail(x_pos, y_pos, x, y, 0, 1)
            knot_move = (0,1)
    elif direction == 'D':
        y -= 1
        if flag is False:
            (x_pos, y_pos) = track_tail(x_pos, y_pos, x, y, 0, -1)
            knot_move = (0,-1)
    elif direction == 'L':
        x -= 1
        if flag is False:
            (x_pos, y_pos) = track_tail(x_pos, y_pos, x, y, -1, 0)
            knot_move = (-1,0)
    elif direction == 'R':
        x += 1
        if flag is False:
            (x_pos, y_pos) = track_tail(x_pos, y_pos, x, y, 1, 0)
            knot_move = (1,0)

    return (x_pos, y_pos, x, y, knot_move)

def track_occupancy(input_list):
    x_pos,y_pos = 0, 0 # Initialize tail
    x, y = 0, 0 # initialize head
    exclusive = set()

    for line in input_list:
        for times in range(0,int(line[1])):
            (x_pos, y_pos, x, y) = move_head(line[0], x_pos, y_pos, x, y)
            exclusive.add((x_pos,y_pos))
            # print((x_pos,y_pos))

    # print(exclusive)
    return len(exclusive)

def track_tail_nine(x_pos, y_pos, x, y, x_diff, y_diff):
    delta = [0,0]
    if abs(x_pos - x) <= 1 and abs(y_pos - y) <= 1:
        pass
    elif (x_pos == x) or (y_pos == y):
        x_pos += x_diff
        y_pos += y_diff
        delta[0] += x_diff
        delta[1] += y_diff
    else:
        if x > x_pos:
            x_pos += 1
            delta[0] += 1
        elif x < x_pos:
            x_pos -= 1
            delta[0] -= 1
        if y > y_pos:
            y_pos += 1
            delta[1] += 1
        elif y < y_pos:
            y_pos -= 1
            delta[1] -= 1

    return (x_pos, y_pos, delta)


def track_occupancy_nine(input_list):
    pos = [[0,0] for i in range(0,10)]
    prev_moves = [[0,0] for i in range(0,10)]

    exclusive = set()
    for line in input_list:
        print(line)
        for times in range(0, int(line[1])):
            (pos[1][0], pos[1][1], pos[0][0], pos[0][1], (prev_moves[0][0], prev_moves[0][1])) = \
                move_head(line[0], pos[1][0], pos[1][1], pos[0][0], pos[0][1])
            for knot in range(2, 10):
                if pos[knot][0] == pos[knot-1][0] and pos[knot][1] == pos[knot-1][1]:
                    pass
                else:
                    (pos[knot][0], pos[knot][1], prev_moves[knot-1]) = \
                        track_tail_nine(pos[knot][0], pos[knot][1], pos[knot-1][0],
                                   pos[knot-1][1], prev_moves[knot-1][0], prev_moves[knot-1][1])
            exclusive.add((pos[-1][0], pos[-1][1]))
            print(pos)

    # print(exclusive)
    return len(exclusive)

def main():
    ## Part 1
    # b = read_input("Day9_test_input.txt")
    b = read_input("Day9_input.txt")
    answer = track_occupancy(b)
    print(f'There are {answer} number of spots visited.')

def main2():
    # Part 2
    #a = read_input("Day9_test_input.txt")
    a = read_input("Day9_test_input2.txt")
    # a = read_input("Day9_input.txt")
    answer2 = track_occupancy_nine(a)
    print(f'There are {answer2} number of spots visited.')

if __name__ == "__main__":
    ## Part 1
    # calc_perf(main())

    ## Part 2
    calc_perf(main2())