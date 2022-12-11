# Day11.py
#
# First attempt at doing Day 11 of Advent of Code 2022

import sys
sys.path.append("..")

from perf import calc_perf
from math import lcm
from functools import reduce

class Monkey(object):
    def __init__(self):
        self.items = []
        self.new_iter = []
        self.post_opt = []
        self.val = 0
        self.operation = []
        self.inspected = 0

    def test(self, item): # Does the test for Part 1
        new_val = item // 3
        if new_val % self.val == 0:
            return new_val, self.post_opt[0]
        else:
            return new_val, self.post_opt[1]

    def test2(self, item): # Does the test for Part 2
        if item % self.val == 0:
            return item, self.post_opt[0]
        else:
            return item, self.post_opt[1]

    def perform_opt(self, item):
        if self.operation[0] == '+':
            item += int(self.operation[1])
        elif self.operation[0] == '*':
            if self.operation[1] == 'old':
                item *= item
            else:
                item *= int(self.operation[1])
        return item


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()
        read_list = [line.split(': ') for line in read_list]

    gen_list = []

    for line in read_list:
        if line[0].lstrip().startswith('Monkey'):
            curr_monkey = Monkey()
            gen_list.append(curr_monkey)
        elif line[0].lstrip().startswith('Starting items'):
            for item in line[1].split(', '):
                curr_monkey.items.append(int(item))
        elif line[0].lstrip().startswith('Operation'):
            splited_lines = line[1].split(' ')
            curr_monkey.operation = [splited_lines[-2],splited_lines[-1]]
        elif line[0].lstrip().startswith('Test'):
            curr_monkey.val = int(line[-1].split(' ')[-1])
        elif line[0].lstrip().startswith("If"):
            curr_monkey.post_opt.append(int(line[1][-1]))

    return gen_list

def cycle(input_list):
    # Perform passes
    for monkey in input_list:
        items_to_pop = len(monkey.items)
        for item in monkey.items:
            new_item = monkey.perform_opt(item)
            val, pass_to = monkey.test(new_item)
            input_list[pass_to].items.append(val)
            monkey.inspected += 1
        for idx in range(0, items_to_pop):
            monkey.items.pop(0)

def cycle2(input_list, common_div):
    # Perform passes
    for monkey in input_list:
        items_to_pop = len(monkey.items)
        for item in monkey.items:
            new_item = monkey.perform_opt(item)
            val, pass_to = monkey.test2(new_item)
            input_list[pass_to].items.append(val%common_div)
            monkey.inspected += 1
        for idx in range(0, items_to_pop):
            monkey.items.pop(0)

def main():
    ## Part 1
    # b = read_input("Day11_test_input.txt")
    b = read_input("Day11_input.txt")

    for idx in range(0,20):
        cycle(b)
        # Debug:
        # for monkey in b:
        #     print(f'{monkey.items}')
        #
        # print(f'Inspected:{[monkey.inspected for monkey in b]}')

    val = sorted([monkey.inspected for monkey in b], key=lambda x:-x)
    print(f'Monkey Business: {val[0]*val[1]}')

def main2():
    # Part 2
    # a = read_input("Day11_test_input.txt")
    a = read_input("Day11_input.txt")
    common_div = reduce(lcm,([i.val for i in a]))

    for idx in range(0,10000):
        cycle2(a, common_div)

    print(f'Inspected:{[monkey.inspected for monkey in a]}')
    val = sorted([monkey.inspected for monkey in a], key=lambda x:-x)
    print(f'Monkey Business: {val[0]*val[1]}')

if __name__ == "__main__":
    ## Part 1
    calc_perf(main())

    ## Part 2
    calc_perf(main2())
