# Day7.py
#
# First attempt at doing Day 7 of Advent of Code 2022

import sys

sys.path.append("..")
from perf import calc_perf


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    # Generate the following while looping through each line:
    #     * dir_dict: a dictionary of directories --> items/dir
    #     * weight_dict: a dictionary of items/dir --> size/weights
    dir_dict = {'/': []}
    weight_dict = {'/': 0}
    cwd = []
    for lines in read_list:
        vals = lines.split()
        string = ''
        for path in cwd[1:]:
            string += '/' + path
        if len(string) == 0:
            string = '/'
        if vals[0] == '$':  # If it's an executed command... change cwd or create a new key
            if vals[1] == 'cd':
                if vals[2] == '..':
                    cwd.pop(-1)
                else:
                    cwd.append(vals[2])
            elif vals[1] == 'ls':
                if string not in dir_dict:
                    dir_dict[string] = []
        elif vals[0] == 'dir':
            if len(string) == 1:
                expanded_string = string + vals[-1]
            else:
                expanded_string = string + '/' + vals[-1]
            if expanded_string not in dir_dict:
                dir_dict[expanded_string] = []
            dir_dict[string].append(vals[1])  # Add directory to the parent
        elif vals[0].isnumeric():  # Add in the file into this list
            if len(string) == 1:
                item_string = string + vals[1]
            else:
                item_string = string + '/' + vals[1]
            dir_dict[string].append(vals[1])  # Add item to directory list (only the lowest level)
            weight_dict[item_string] = int(vals[0])  # Add the weight of item

    return dir_dict, weight_dict


def loop_through(folder, input_list, weight_list, curr_name):
    count = 0
    for item in folder:
        try:
            if len(curr_name) == 1:
                count_var = curr_name + item
                count += weight_list[count_var]
            else:
                count_var = curr_name + '/' + item
                count += weight_list[count_var]
        except KeyError:
            count += loop_through(input_list[count_var], input_list, weight_list, count_var)

    return count


def sum_weights(input_list, weight_list):
    dir_weight_dict = {}
    for direct in input_list:
        count = 0
        for item in input_list[direct]:
            if len(direct) == 1:
                item_string = direct + item
            else:
                item_string = direct + '/' + item
            try:
                count += weight_list[item_string]
            except KeyError:
                count += loop_through(input_list[item_string], input_list, weight_list, item_string)
        dir_weight_dict[direct] = count
    return dir_weight_dict


def count_lesser(input_list, threshold):
    count = 0
    for val in input_list.values():
        if val <= threshold:
            count += val

    return count


def main():
    ## Part 1
    threshold = 100000
    # dir_dict, size_dict = read_input("Day7_test_input.txt")
    dir_dict, size_dict = read_input("Day7_input.txt")
    # print(dir_dict, size_dict)
    final_dict = sum_weights(dir_dict, size_dict)
    answer = count_lesser(final_dict, threshold)
    print(f'All directories <= {threshold} has a sum of {answer}.')

    # Part 2
    required = 30000000 - (70000000 - final_dict['/'])
    inv_dict = {v: k for k, v in final_dict.items()}
    sorted_list = sorted(final_dict.values(), key=lambda x: x)
    for j in sorted_list:
        if j >= required:
            break

    print(f'Delete directory {inv_dict[j]} of size {j}.')


if __name__ == "__main__":
    ## Part 1 + 2
    calc_perf(main())
