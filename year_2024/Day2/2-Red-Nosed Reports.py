import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import utils
input_array = utils.get_file_lines_as_list("input2.txt")

def main():

    def check_asc(a):
        return (all(a[i] <= a[i + 1] for i in range(len(a) - 1)))

    def check_desc(b):
        return (all(b[i] >= b[i + 1] for i in range(len(b) - 1)))
    
    def min_operations_asc(arr):
        for i,v in enumerate(arr):
            if i!=len(arr)-1:
                if arr[i]>=arr[i+1]:
                    del arr[i+1]
                    break
        if arr == sorted(arr):
            return True
        return False
    
    def min_operations_desc(arr):
        for i,v in enumerate(arr):
            if i!=len(arr)-1:
                if arr[i]<=arr[i+1]:
                    del arr[i+1]
                    break
        if arr == sorted(arr, reverse=True):
            return True
        return False


    
    ### PART 1 ###
    # counter = 0
    # for data in input_array:
    #     data_input = data.split(" ")
    #     data_input = [int(item) for item in data_input]

    #     if check_asc(data_input) or check_desc(data_input):
    #         xdiff = [abs(data_input[n]-data_input[n-1]) for n in range(1,len(data_input))]
    #         if max(xdiff) <= 3 and min(xdiff) >=1:
    #             counter+=1
    # print(counter)
    
    ### PART 2 ###
    counter = 0
    for data in input_array:
        data_input = data.split(" ")
        data_input = [int(item) for item in data_input]

        if min_operations_asc(data_input) or min_operations_desc(data_input):
            for i,v in enumerate(data_input):
                if i!=len(data_input)-1:
                    diff = abs(data_input[i]-data_input[i+1])
                    if diff > 3 or diff <1:
                        del data_input[i]
                        break
            xdiff = [abs(data_input[n]-data_input[n-1]) for n in range(1,len(data_input))]
            if max(xdiff) <= 3 and min(xdiff) >=1:
                counter+=1
    print(counter)

if __name__ == "__main__":
    main()