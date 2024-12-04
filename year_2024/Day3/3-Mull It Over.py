import sys
import os
import re
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import utils
input_str = utils.get_file_as_str("input2.txt")

def main():

    ##### PART 1 SOLUTION #####
    # pattern = r"mul\(\d+,\d+\)"
    # matches = re.findall(pattern, input_str)
    # print(matches)
    # results = []
    # for data in matches:
    #     data = data.replace('mul(','')
    #     values = data.split(",")
    #     results.append(int(values[0]) * int(values[1].replace(')','')))
    # print(sum(results))

    ##### PART 2 SOLUTION #####

    # Initialize state
    mul_enabled = True  # Initially mul is enabled
    total_sum = 0

    # Define pattern to match the do(), don't(), and mul(int, int) instructions
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_pattern = r"mul\((\d+),(\d+)\)"

    # Process the input string
    index = 0
    while index < len(input_str):
        # Check for do() instruction
        if re.match(do_pattern, input_str[index:]):
            mul_enabled = True
            index += len("do()")
        # Check for don't() instruction
        elif re.match(dont_pattern, input_str[index:]):
            mul_enabled = False
            index += len("don't()")
        # Check for mul(int, int) instruction
        elif re.match(mul_pattern, input_str[index:]):
            match = re.match(mul_pattern, input_str[index:])
            num1, num2 = map(int, match.groups())
            
            # If mul is enabled, calculate the result and add to the total
            if mul_enabled:
                total_sum += num1 * num2
            index += len(match.group(0))  # Move past the mul() instruction
        else:
            # Skip any non-matching characters
            index += 1

    print(total_sum)

    

main()


