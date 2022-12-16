# Day16.py
#
# First attempt at doing Day 16 of Advent of Code 2022

import sys
sys.path.append("..")

from perf import calc_perf
from random import choice

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    split_list = [
        i.replace(' has', '; ').replace('rate=', '; ').replace('Valve ', '').replace('valve ', '; ').replace('valves ', '; ').split('; ') for i
        in read_list]

    flow_dict = dict()
    tunnel_dict = dict()
    for item in split_list:
        flow_dict[item[0]] = int(item[2])
        tunnel_dict[item[0]] = item[-1].split(', ')

    skip_dict = []
    for (key, vals) in flow_dict.items():
        if vals == 0:
            skip_dict.append(key)

    return flow_dict, tunnel_dict, skip_dict


def loop(flow_dict, tunnel_dict, skip, time):
    total_pressure = 0
    curr = 'AA'
    current_open = [curr]
    current_rates = [flow_dict[curr]]
    current_path = []
    print(skip)
    for time in range(1, time+1):
        total_pressure += sum(current_rates)
        if time % 2:
            current_path.append(curr)
        else:
            current_path.append(curr)
            pick = 'AA'
            for i in tunnel_dict[curr]:
                # Prioritize paths with higher rate
                if i not in skip and flow_dict[i] > flow_dict[pick]:
                    pick = i
            # If only choices with rate=0, then pick randomly something we haven't picked before:
            print(pick)
            if pick == 'AA':
                try:
                    pick = choice([i for i in tunnel_dict[curr] if i not in current_open])
                except IndexError:
                    pick = tunnel_dict[curr][0]

            curr = pick
            if pick not in current_open:
                current_open.append(pick)
                current_rates.append(flow_dict[pick])

    return total_pressure, current_open, current_rates, current_path

def return_top3(input_list):
    sorted_list = sorted(input_list, key=lambda x:-x)
    cal_sum = sum(sorted_list[0:3])
    where_three = numpy.where(input_list > sorted_list[3])[0]

    return [int(cal_sum), where_three]

def main():
    ## Part 1
    flow, path, skip = read_input("Day16_test_input.txt")
    # flow, path = read_input("Day16_input.txt")

    max_answer = 0
    # Loop through algorithm for 20 times
    for idx in range(1):
        answer, current_open, current_rates, current_path = loop(flow, path, skip, 30)
        if answer > max_answer:
            max_answer = answer
            max_open = current_open
            max_rates = current_rates
            max_path = current_path

    print(f'Path {max_path} has {max_open} with {max_answer} of pressure released.')

def main2():
    # Part 2
    # a = read_input("Day16_test_input.txt")
    a = read_input("Day16_input.txt")
    answer2 = return_top3(a)
    print(f'Elves {answer2[1] + 1} have {answer2[0]} calories worth of food.')

if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    # calc_perf(main2())
