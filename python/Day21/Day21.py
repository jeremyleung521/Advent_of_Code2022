# Day21.py
#
# First attempt at doing Day 21 of Advent of Code 2022

import time
from sympy.solvers import solve
from sympy import symbols

def read_input(file_name, fix=False):
    with open(file_name, 'r') as f:
        read_list = f.read().replace(':', '').splitlines()

    # print(read_list)

    final_list = [i.split(' ') for i in read_list]
    def_dict = dict()
    relation_dict = dict()

    for line in final_list:
        if len(line) == 2:
            def_dict[f'{line[0]}'] = int(line[1])
        elif len(line) > 2:
            relation_dict[f'{line[0]}'] = line[1:]

    if fix:
        def_dict['humn'] = 'humn'
        relation_dict['root'][1] = '='

    return final_list, def_dict, relation_dict


def loop(def_dict, relation_dict):
    """
    Old solution...
    """
    while 'root' not in def_dict.keys():
        for key, relation in relation_dict.items():
            try:
                def_dict[key] = int(eval(f'{def_dict[relation[0]]} {relation[1]} {def_dict[relation[2]]}'))
            except KeyError:
                pass

    return def_dict['root']

def getNumber(def_dict, relation_dict, monkey):
    """
    Faster solution from Lafazar which solves the operations with a lambda function on retrieval.
    """
    operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x // y}
    if monkey in def_dict:
        return def_dict[monkey]
    monkey1, operation, monkey2 = relation_dict[monkey]
    return operations[operation](getNumber(def_dict, relation_dict, monkey1), getNumber(def_dict, relation_dict, monkey2))

def getExpression(def_dict, relation_dict, monkey):
    if monkey in def_dict:
        return def_dict[monkey]
    monkey1, operation, monkey2 = relation_dict[monkey]
    return f"({getExpression(def_dict, relation_dict, monkey1)}{operation}{getExpression(def_dict, relation_dict, monkey2)})"

def solve_solution(def_dict, relation_dict):
    # both_sides = [relation_dict[f'{relation_dict["root"][0]}'], relation_dict[f'{relation_dict["root"][2]}']]

    left, right, humn = symbols("left right humn")
    left = eval(getExpression(def_dict, relation_dict, relation_dict['root'][0]))
    right = eval(getExpression(def_dict, relation_dict, relation_dict['root'][2]))
    answer = solve(left - right, humn)

    return int(answer[0])


def main():
    ## Part 1
    # final_dict, def_dict, relation_dict = read_input("Day21_test_input.txt")
    final_dict, def_dict, relation_dict = read_input("Day21_input.txt")

    # answer = loop(def_dict, relation_dict)
    answer = getNumber(def_dict, relation_dict, 'root')
    print(f'\'root\' monkey should yell {answer}.')


def main2():
    # Part 2
    # final_dict, def_dict, relation_dict = read_input("Day21_test_input.txt", fix=True)
    final_dict, def_dict, relation_dict = read_input("Day21_input.txt", fix=True)

    answer = solve_solution(def_dict, relation_dict)

    print(f'\'humn\' not-monkey should yell {answer}.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
