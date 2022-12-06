import re
from itertools import groupby
input_file = "input2.txt"

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

def get_file_lines_as_list(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def main():
    data = get_file_lines_as_list(input_file)
    count_max = 0
    ind = find_indices(data, '')
    sum_sublist = []
    start_counter = 0
    for i in ind:
        end_counter = i
        sub_list = data[start_counter:end_counter]
        sub_list = [eval(i) for i in sub_list]
        print(sum(sub_list))
        sum_sublist.append(sum(sub_list))
        start_counter = end_counter+1
    print("Solution 1")
    print(max(sum_sublist))
    print("Solution 2")
    sum_sublist.sort(reverse = True)
    print(sum(sum_sublist[0:3]))

if __name__ == "__main__":
    main()