# Advent of Code 2022
# --- Day 16: Proboscidea Volcanium ---
# Copied from https://topaz.github.io/paste/#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

import sys
import re
import math
import pprint
import collections
import copy
import queue
import itertools
import functools

DEBUG = False


def sign(a):
    if a == 0:
        return 0
    if a > 0:
        return 1
    return -1


# --- Part One ---
with open('Day16_input.txt','r') as f:
    lines = [line for line in f.read().splitlines()]

flow = {}
next = {}
for line in lines:
    v_id = re.findall("Valve ([A-Z]+) ", line)[0]
    v_flow = re.findall("rate=([0-9]+);", line)[0]
    next_str = re.findall("to valves? (.+)$", line)[0]
    v_next = [a.strip(",") for a in next_str.split()]
    # print(v_id, v_flow, v_next)
    flow[v_id] = int(v_flow)
    next[v_id] = v_next

# print(flow)
# print(next)
all_valves = set(flow.keys())


# print(all_valves)

# use dfs with caching and pruning for 30 steps
#
# path is (v0, v1, v2, .., v_last) of valves leading to v_last  (v<n> may repeat)
#
# - when v<n> repeats indicates a stay to open a valve
# - length of a path may be 30 or shorter if all valves are open, and so
# - all doubles in sequence are unique and equal to the number of valves
#
# open_valves = sorted tuple of set of all open valves at end of path

# get pressure from path for the duration of the path steps
def p_from_path(path):
    open_valves = ()
    path_p = 0
    step_p = 0
    prev_id = None
    for v_id in path:
        path_p += step_p
        # a valve opens
        if prev_id and prev_id == v_id:
            open_valves += (v_id,)
            step_p += flow[v_id]
        prev_id = v_id

    return (path_p, tuple(sorted(open_valves)))


# cache of (v_id, open_valves, next_depth) -> best pressure
# for correct caching, open_valves tuple must be sorted
cached = {}


# path, open_valves  are tuples
def bb(path, open_valves, next_depth):
    ##print("bb:", next_depth, path, open_valves)

    v_id = path[-1]

    # if all valves open, stop moving, a solution
    if not (all_valves - set(open_valves)) or next_depth <= 1:
        cached[(v_id, open_valves, next_depth)] = (0, tuple())
        ##print(next_depth, path, open_valves, ">>", 0)
        return (0, tuple())

    max_n_p = -1
    max_n_tail_path = None

    # move to next valves
    for next_id in next[v_id]:
        cached_key = (next_id, open_valves, next_depth - 1)
        if cached_key in cached:
            n_p, n_tail_path = cached[cached_key]
        else:
            n_path = path + (next_id,)  # tuple(*path, next_id)
            n_p, n_tail_path = bb(n_path, open_valves, next_depth - 1)
        n_tail_path = (v_id,) + n_tail_path
        if n_p > max_n_p:
            max_n_p = n_p
            max_n_tail_path = n_tail_path

    # open last valve ?
    # open only if there is flow !!  how much time lost.. with this check finishes in a few seconds
    if v_id not in open_valves and flow[v_id] > 0:
        n_valves = tuple(sorted(open_valves + (v_id,)))
        cached_key = (v_id, n_valves, next_depth - 1)
        if cached_key in cached:
            n_p, n_tail_path = cached[cached_key]
        else:
            n_path = path + (v_id,)  # tuple(*path, v_id)
            n_p, n_tail_path = bb(n_path, n_valves, next_depth - 1)
            n_p += flow[v_id] * (next_depth - 1)
        n_tail_path = (v_id,) + n_tail_path
        if n_p > max_n_p:
            max_n_p = n_p
            max_n_tail_path = n_tail_path

    cached[(v_id, open_valves, next_depth)] = (max_n_p, max_n_tail_path)
    ##print(next_depth, path, open_valves, ">>", this_p)
    return (max_n_p, max_n_tail_path)


max_depth = 30
print("max_depth = ", max_depth)

best_p, best_path = bb(("AA",), tuple(), max_depth)
print("cache", len(cached))

print(best_path)
print(best_p)
padded_path = (best_path + max_depth * ('',))[:max_depth + 1]
# assertion check, this should be same as above
p, open_valves = p_from_path(padded_path)
print(p)
print(open_valves)

# result in 4.7 sec

# --- Part Two ---

# cache of (v_id, open_valves, next_depth, player) -> best pressure
# for correct caching, open_valves tuple must be sorted
cached = {}


# path, open_valves  are tuples
def bb2(path, open_valves, next_depth, n_player):
    ##print("bb2:", next_depth, path, open_valves)

    v_id = path[-1]

    if n_player == 0:
        return 0

    if next_depth <= 1:
        return bb2(("AA",), open_valves, max_depth, n_player - 1)

    # if all valves open, stop moving, a solution
    if not (all_valves - set(open_valves)):
        cached[(v_id, open_valves, next_depth, n_player)] = 0
        ##print(next_depth, path, open_valves, ">>", 0)
        return 0

    max_n_p = -1

    # move to next valves
    for next_id in next[v_id]:
        cached_key = (next_id, open_valves, next_depth - 1, n_player)
        if cached_key in cached:
            n_p = cached[cached_key]
        else:
            n_path = path + (next_id,)  # tuple(*path, next_id)
            n_p = bb2(n_path, open_valves, next_depth - 1, n_player)
        if n_p > max_n_p:
            max_n_p = n_p

    # open last valve ?
    # open only if there is flow !!  how much time lost.. with this check finishes in a few seconds
    if v_id not in open_valves and flow[v_id] > 0:
        n_valves = tuple(sorted(open_valves + (v_id,)))
        cached_key = (v_id, n_valves, next_depth - 1, n_player)
        if cached_key in cached:
            n_p = cached[cached_key]
        else:
            n_path = path + (v_id,)  # tuple(*path, v_id)
            n_p = bb2(n_path, n_valves, next_depth - 1, n_player)
            n_p += flow[v_id] * (next_depth - 1)
        if n_p > max_n_p:
            max_n_p = n_p

    cached[(v_id, open_valves, next_depth, n_player)] = max_n_p
    ##print(next_depth, path, open_valves, ">>", this_p)
    return max_n_p


max_depth = 26
print("max_depth = ", max_depth)

best_p = bb2(("AA",), tuple(), max_depth, 2)
print("cache", len(cached))

print(best_p)