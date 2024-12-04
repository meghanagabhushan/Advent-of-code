import sys
import os
import re
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import utils
input_str = utils.get_file_as_str("input1.txt")

def main():

    ##### PART 1 SOLUTION #####
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, input_str)
    print(matches)
    results = []
    for data in matches:
        data = data.replace('mul(','')
        values = data.split(",")
        results.append(int(values[0]) * int(values[1].replace(')','')))
    print(sum(results))

    ##### PART 2 SOLUTION #####
    pattern = r"mul\(\d+,\d+\)"

    

main()


