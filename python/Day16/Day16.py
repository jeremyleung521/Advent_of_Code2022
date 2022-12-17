# Day16.py
#
# First attempt at doing Day 16 of Advent of Code 2022
#
# With help from https://github.com/mebeim/aoc/blob/master/2022/README.md#day-16---proboscidea-volcanium


import sys
sys.path.append("..")

from perf import calc_perf
from random import choice
from tqdm.auto import tqdm, trange
from copy import deepcopy
from collections import deque, defaultdict
from itertools import combinations


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

    flow_mod_dict = deepcopy(flow_dict)

    for key, val in flow_dict.items():
        # print(key,val)
        if val == 0 and key != 'AA':
            flow_mod_dict.pop(key)

    return flow_dict, tunnel_dict, flow_mod_dict


def bfs_optimize(adj_array, start, end):
    parent = {start: None}
    d = {start: 0}
    visited = []

    queue = deque()
    queue.append(start)
    #print(end)
    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.append(u)
        for n in adj_array[u]:
            # print(n)
            # if u in end:
            #     print(f'Shortest path between {start} and {end} is {d[u]} steps.')
            #     return parent, d
            if n not in d:
                if n not in parent:
                    parent[n] = []
                parent[n].append(u)
                d[n] = d[u] + 1
                queue.append(n)
    return parent, d

def distance_matrix(flow_dict, tunnel_dict, skip_dict):
    seen = []
    parent = []
    dist = []
    order = []
    for key in skip_dict.keys():
        order.append(key)
        parent_out, dist_out = bfs_optimize(tunnel_dict, key, 0)
        parent.append(parent_out)
        dist.append(dist_out)
        seen.append([key])

    # Remove valves with 0 rates
    for valve in flow_dict:
        if valve not in skip_dict:
            for dict in dist:
                dict.pop(valve)

    #
    seen_dict = {}
    choices = []
    for idx, val in enumerate(seen):
        seen_dict[val[0]] = dist[idx]
        choices.append(val[0])

    choices.remove('AA')

    return parent, seen_dict, choices

def score(rates, chosen_valves):
    total = 0
    for valve, time_left in chosen_valves.items():
        total += rates[valve] * time_left
    return total

def choices(distance, rates, valves, time=30, cur='AA', chosen={}):
    for nxt in valves:
        new_time = time - (distance[cur][nxt] + 1)

        if new_time < 2:
            continue

        new_chosen = chosen | {nxt: new_time}
        yield from choices(distance, rates, valves - {nxt}, new_time, nxt, new_chosen)

    yield chosen


def main():
    ## Part 1
    # flow, path, skip = read_input("Day16_test_input.txt")
    flow, path, skip = read_input("Day16_input.txt")

    parent, dist, seen = distance_matrix(flow, path, skip)

    best = max(score(flow, c) for c in choices(dist, flow, set(seen)))

    print(f'Best path has with {best} of pressure released.')

def main2():
    # Part 2
    # flow, path, skip = read_input("Day16_test_input.txt")
    flow, path, skip = read_input("Day16_input.txt")

    parent, dist, seen = distance_matrix(flow, path, skip)

    maxscore = defaultdict(int)

    for solution in choices(dist, flow, set(seen), 26):
        k = frozenset(solution)
        s = score(flow, solution)

        if s > maxscore[k]:
            maxscore[k] = s

    best = max(sa + sb for (a, sa), (b, sb) in combinations(maxscore.items(), 2) if not a & b)

    print(f'Best path has with {best} of pressure released.')

if __name__ == "__main__":
    ## Part 1
    # calc_perf(main())

    ## Part 2
    calc_perf(main2())
