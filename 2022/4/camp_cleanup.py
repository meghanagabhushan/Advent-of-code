from operator import eq
input_file = "input2.txt"

def get_file_lines_as_list(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def main():
    data = get_file_lines_as_list(input_file)
    total_count = 0
    common_pairs = 0
    for line in data:
        data1 = line.split(",")[0]
        data2 = line.split(",")[1]
        l1 = list(range(int(data1.split("-")[0]),int(data1.split("-")[1])+1))
        l2 = list(range(int(data2.split("-")[0]),int(data2.split("-")[1])+1))
        if set(l1).issubset(set(l2)) or set(l2).issubset(set(l1)):
           total_count = total_count +1
        res = len(set(l1) & set(l2))
        if res>0:
            common_pairs = common_pairs + 1
    print("Solution 1")
    print(total_count)
    print("Solution 2")
    print(common_pairs)

if __name__ == "__main__":
    main()