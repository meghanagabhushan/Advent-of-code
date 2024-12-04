import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import utils
input_array = utils.get_file_lines_as_list("input1.txt")

def main():
    left_array, right_array = [], []
    for data in input_array:
        left_array.append(int(data.split("   ")[0]))
        right_array.append(int(data.split("   ")[1]))
    

    ##### PART 1 #####
    left_array.sort()
    right_array.sort()
    
    result_array = []
    for i,v in enumerate(left_array):
         result_array.append(abs(left_array[i] - right_array[i]))
    print(sum(result_array))

    ##### PART 2 #####
    result_array = []
    for i,v in enumerate(left_array):
        result_array.append(v*right_array.count(v))
    print(sum(result_array))


if __name__ == "__main__":
    main()