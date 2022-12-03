from shutil import move
import string

input_file = "input2.txt"

lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

lower_dict = {}
upper_dict = {}

lower_count = 1
upper_count = 27
for x in lower_alphabet:
    lower_dict[x] = lower_count
    lower_count = lower_count+1

for x in upper_alphabet:
    upper_dict[x] = upper_count
    upper_count = upper_count+1

def get_file_lines_as_list(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def get_str(line):
    return line[0:len(line)//2],line[len(line)//2:]

def get_common_score(str1,str2):
    common_char = set(str1) & set(str2)
    if list(common_char)[0] in lower_dict:
        return lower_dict[list(common_char)[0]]
    else:
        return upper_dict[list(common_char)[0]]

def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def get_common_score2(lists):
    common_char = set(lists[0]) & set(lists[1]) & set(lists[2])
    if list(common_char)[0] in lower_dict:
        return lower_dict[list(common_char)[0]]
    else:
        return upper_dict[list(common_char)[0]]

def main():
    data = get_file_lines_as_list(input_file)
    total_count = 0
    for line in data:
        str1,str2 = get_str(line)
        score = get_common_score(str1,str2)
        total_count = total_count +score
    print("solution1")
    print(total_count)
    total_count2 =0
    input_data2 = list(divide_chunks(data, 3))
    for lists in input_data2:
        score = get_common_score2(lists)
        total_count2 = total_count2 +score
    print("solution2")
    print(total_count2)


if __name__ == "__main__":
    main()
