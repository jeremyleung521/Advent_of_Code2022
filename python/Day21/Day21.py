# Day21.py
#
# First attempt at doing Day 21 of Advent of Code 2022

import time


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
        def_dict['root'][1] = '='
        del def_dict['humn']

    return final_list, def_dict, relation_dict


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


def main():
    ## Part 1
    # final_dict, def_dict, relation_dict = read_input("Day21_test_input.txt")
    final_dict, def_dict, relation_dict = read_input("Day21_input.txt")

    answer = loop(def_dict, relation_dict)
    print(f'\'root\' monkey should yell {answer}.')


def main2():
    # Part 2
    # a = read_input("Day21_test_input.txt")
    a = read_input("Day21_input.txt")
    answer2 = return_top3(a)
    print(f'Elves {answer2[1] + 1} have {answer2[0]} calories worth of food.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    # startTime = time.perf_counter()
    # main2()
    # print(f'{time.perf_counter() - startTime} sec.')
