# Day1.py
#
# First attempt at doing Day 1 of Advent of Code 2022

import numpy

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    # Create an array that assume each "elf" only carried one food item
    final_count = numpy.zeros(int(len(read_list)/2 + 1))
    counter = 0
    for entry in read_list:
        if entry != '':
            final_count[counter] += int(entry)
        elif entry == '':
            counter += 1

    final_count = numpy.trim_zeros(final_count, trim='b')

    return final_count

def return_max(input_list):
   max_cal = numpy.max(input_list)
   where = numpy.where(input_list == max_cal)[0][0]

   return [int(max_cal), where]

def return_top3(input_list):
    sorted_list = sorted(input_list, key=lambda x:-x)
    cal_sum = sum(sorted_list[0:3])
    where_three = numpy.where(input_list > sorted_list[3])[0]

    return [int(cal_sum), where_three]

if __name__ == "__main__":
    ## Part 1
    #b = read_input("Day1_test_input.txt")
    b = read_input("Day1_input.txt")
    answer = return_max(b)
    print(f'Elf {answer[1]+1} has {answer[0]} calories worth of food.')


    ## Part 2
    #a = read_input("Day1_test_input.txt")
    a = read_input("Day1_input.txt")
    answer2 = return_top3(a)
    print(f'Elves {answer2[1]+1} have {answer2[0]} calories worth of food.')
