# Day21.py
#
# First attempt at doing Day 21 of Advent of Code 2022

import time
import sympy
from collections.abc import Iterable

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
        del def_dict['humn']
        # if relation_dict['root'][0] in def_dict.keys():
        #     def_dict[relation_dict['root'][2]] = def_dict[relation_dict['root'][0]]
        #     # relation_dict['root'][2] = int(2)
        #     # relation_dict['root'][1] = '*'
        # elif relation_dict['root'][2] in def_dict.keys():
        #     def_dict[relation_dict['root'][0]] = def_dict[relation_dict['root'][2]]
        #     # relation_dict['root'][0] = int(2)
        #     # relation_dict['root'][1] = '*'
        # else:
        #     # relation_dict['root'][0] = int(0)
        #     # relation_dict['root'][1] = '+'
        #     relation_dict['root'][1] = '='
        relation_dict['root'][1] = '='

    print(relation_dict['root'])

    return final_list, def_dict, relation_dict


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x

def loop(def_dict, relation_dict):
    while 'root' not in def_dict.keys():
    # for _ in range(1):
        # print(def_dict)
        for key, relation in relation_dict.items():
            try:
                def_dict[key] = int(eval(f'{def_dict[relation[0]]} {relation[1]} {def_dict[relation[2]]}'))
            except KeyError:
                pass

    return def_dict['root']


def reduce(def_dict, relation_dict):
    # while 'root' not in def_dict.keys():
    for _ in range(50):
        # print(def_dict)
        for key, relation in list(relation_dict.items()):
            try:
                def_dict[key] = int(eval(f'{def_dict[relation[0]]} {relation[1]} {def_dict[relation[2]]}'))
                del relation_dict[key]
            except KeyError:
                pass

    return def_dict, relation_dict


def solve(def_dict, relation_dict):
    # LHS
    both_sides = [relation_dict[f'{relation_dict["root"][0]}'], relation_dict[f'{relation_dict["root"][2]}']]

    for idx, curr_var in enumerate(both_sides):
        print('both sides')
        # print(curr_var)
        for _ in range(50):
        # while 'humn' not in flatten(curr_var):
            both_sides[idx] = list(flatten(curr_var))
            for jdx, val in enumerate(curr_var):
                print(val)
                # print(jdx, val)
                try:
                    curr_var[jdx] = relation_dict[val]
                    # curr_var[jdx] = int(eval(f'{def_dict[val[0]]} {val[1]} {def_dict[val[2]]}'))
                    curr_var = list(flatten(curr_var))
                    print(curr_var)
                    print('success_replacement')
                except (KeyError, TypeError):
                    pass
                try:
                    curr_var[jdx] = def_dict[val]
                    curr_var = list(flatten(curr_var))
                except (KeyError, TypeError):
                    pass
        b = ''
        print(curr_var)
        #both_sides[idx] = [b.join(str(i)) for i in curr_var]

    print(both_sides)
    return both_sides

def solve_system(def_dict, relation_dict):
    variables = set()
    equations = []


    for key, val in def_dict.items():
        variables.add(key)
        equations.append(f'{val} - {key}')
    for key, val in relation_dict.items():
        variables.add(key)
        variables.add(val[2])
        if not isinstance(val[0], int):
            variables.add(val[0])

        equations.append(f'{val[0]} {val[1]} {val[2]} - {key}')

    symbols = dict()
    for j in variables:
        symbols[str(j)] = sympy.Symbol(j)
        #symbols.append(j)
        #print(type(j))

    print(symbols)
    for i in equations:
        print(i)


    solution = sympy.solvers.linsolve([str(f'Eq({i}, 0)') for i in equations], list(symbols.values()))

    return symbols, solution

    # return symbols, 1

def main():
    ## Part 1
    # final_dict, def_dict, relation_dict = read_input("Day21_test_input.txt")
    final_dict, def_dict, relation_dict = read_input("Day21_input.txt")

    answer = loop(def_dict, relation_dict)
    print(f'\'root\' monkey should yell {answer}.')


def main2():
    # Part 2
    final_dict, def_dict, relation_dict = read_input("Day21_test_input.txt", fix=True)
    # final_dict, def_dict, relation_dict = read_input("Day21_input.txt")

    print(def_dict)
    print(relation_dict)
    answer = solve(def_dict, relation_dict)
    # def_dict, relation_dict = reduce(def_dict, relation_dict)
    #
    # symbols, solution = solve_system(def_dict, relation_dict)

    print(answer)
    #print(f'\'root\' monkey should yell {answer}.')


if __name__ == "__main__":
    ## Part 1
    # startTime = time.perf_counter()
    # main()
    # print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
