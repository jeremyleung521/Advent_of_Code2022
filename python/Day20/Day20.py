# Day20.py
#
# First attempt at doing Day 20 of Advent of Code 2022
# With help from here:
# https://topaz.github.io/paste/#XQAAAQArBQAAAAAAAAARiEJHiiMzw3cPM/1Vl+2nx/DqKkM2yi+HVdpp+qLiqZwdO8DftYzG7xETHPj1qjypxh5M1TcPUMscdwJ9eMao1h4KjZSFqvUVGgRO1B0UY9xy1ppiz5MCls8P3jkcK0nuQ0xyqjMGO1zjudp0iPknFmDdndniTzqJ7bQyJOivVMdvFt6PZvBFRLBJlJt+W2OfKFao4pmwqJQ3tYnoeqoxaZBRq6SnzFKevZL5mczBvlhZ4Z7pOYZWJod3DUZB62OVqwdbVuZ1Gf/YtwiEH73ZCQkNYCTDsmM7Q+7KoPCx1BL7vC8nnymRszz7wQoPgnExffEtXCUA5BrwGtgN+iC7bkvBbLKdGgBlxLpXCxv9tDHXSTAAlW0cfwiiOBGFGYvptqGAEjKFqKzBPe2V7Krsp5rrGFg6b0y5oV3Dzm1Z9SNgK1GRxvQQxGPgcmcSUk3isUQm5j4aqcghwu3d7GkrKCT7kX1dW2YUymL8viTMxauPyqK6xrBIU81Uw0ArXN9KS90ssoDvQ+9X610H8rOxseIchLFxlqY2ldEL8mH6eXvAO6QgiP3cwrN84XRq/v/TJTRFAORAP1r1O3xF19rHw4BxW5jSEbNsnIMVqn3/F/8Vro5zSdIKib6VyuKjofLB/JRqD+5qt2TQi5xqyUOFeWDZeMcDj4Xoc95wKxdPOa1H1wdVL6bIWJDXNJ6R+FBxNpU1rsX7PZv7YxWWeIqICaArC51izABqc0jQLjKIqCIkG0TUQSX1WCENuzO2CZcZKp7fN4YmIWBN//fit2w=

import time
import numpy
from copy import deepcopy
from collections import deque


def read_input(file_name, key=1):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_list = [(idx, int(i)*key) for idx, i in enumerate(read_list)]

    return deque(final_list)


def find_character(final_list, n):
    while final_list[0][1] != 0:
        final_list.rotate(-1)

    mod = len(final_list)
    answer = []
    for i in n:
        answer.append(final_list[i % mod][1])

    # print(answer)
    return answer, sum(answer)

def decrypt_nums(nums):
    # print(nums)
    mod = len(nums)
    for idx in range(mod):
        while idx != nums[0][0]:
            nums.rotate(-1)

        i, n = nums.popleft()
        nums.rotate(-n)
        nums.appendleft((i, n))
        nums.rotate(n)


def basic_decrypt_sum(nums):
    decrypt_nums(nums)
    answer, answer2 = find_character(nums, [1000,2000,3000])
    return answer, answer2


def main():
    ## Part 1
    # b = read_input("Day20_test_input.txt")
    b = read_input("Day20_input.txt")
    answer, answer2 = basic_decrypt_sum(b)
    # print(sorted(b, key=lambda x:x[0]))
    # answer, sum_answer = find_character(answer, [1000, 2000, 3000])
    print(f'Sum of {answer} is {answer2}.')


def main2():
    # Part 2
    # a = read_input("Day20_test_input.txt", 811589153)
    a = read_input("Day20_input.txt", 811589153)

    # Loop through 10 times
    for _ in range(10):
        answer, answer2 = basic_decrypt_sum(a)

    print(f'Sum of {answer} is {answer2}.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
