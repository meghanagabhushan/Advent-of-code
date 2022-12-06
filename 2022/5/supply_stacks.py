import csv
input_file = "input2.txt"
operations_file = "operations2.txt"
# n=3
n=9
total_len = (n*4)-1
indices_of_elements = []
i=1
while (i<total_len):
    indices_of_elements.append(i)
    i+=4

with open(operations_file) as file:
    operations = file.readlines()
    operations = [line.rstrip() for line in operations]

def get_file_lines_as_list(filename):
    with open(filename) as file:
        lines = file.readlines()
        # print(lines)
        # lines = [line.rstrip() for line in lines]
    return lines

def get_columns(filename): 
    with open(filename) as inf:
        reader = csv.reader(inf, delimiter=" ")
        second_col = list(zip(*reader))[1]

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

def perform_operations(all_stacks):
    for op in operations:
        num = int(op.split(" ")[1])
        source_ind = int(op.split(" ")[3])-1
        dest_ind = int(op.split(" ")[5])-1
        i=1
        while(i<=num):
            pop_element = ''
            for idx,elem in enumerate(all_stacks[source_ind]):
                break_flag = False
                print(idx,elem)
                if elem!=' ':
                    pop_element = elem
                    all_stacks[source_ind][idx] = ' '
                    break_flag = True
                    break
                else:
                    continue
            # print("pop element - "+pop_element)
            dest_indices = find_indices(all_stacks[dest_ind], ' ')
            if dest_indices:
                idx2 = max(dest_indices)
                all_stacks[dest_ind][idx2] = pop_element
            else:
                all_stacks[dest_ind].insert(0,pop_element)
            # print(all_stacks)
            i+=1
    return all_stacks

def perform_operations2(all_stacks):
    for s in all_stacks:
        if ' ' in s:
            s.remove(" ")
    print(all_stacks)
    for op in operations:
        num = int(op.split(" ")[1])
        source_ind = int(op.split(" ")[3])-1
        dest_ind = int(op.split(" ")[5])-1
        i=1
        elements_to_be_popped = all_stacks[source_ind][:num]
        print(elements_to_be_popped)        
        for e in elements_to_be_popped:
            all_stacks[source_ind].remove(e)
            # all_stacks[source_ind] = list(map(lambda x: x.replace(e, ' '), all_stacks[source_ind]))
        elements_to_be_popped = list(reversed(elements_to_be_popped))
        for e in elements_to_be_popped:
            all_stacks[dest_ind].insert(0,e)
        print(all_stacks)
    return all_stacks

def get_first_element(res):
    res_str = ''
    for stack_col in res:
        for element in stack_col:
            if element!=' ':
                res_str = res_str + element
                break
            else:
                continue
    return res_str
    



def main():
    data = get_file_lines_as_list(input_file)
    all_stacks = []
    for indices in indices_of_elements:
        column_stack = []
        for line in data:
            column_stack.append(line[indices])
        all_stacks.append(column_stack)
    print(all_stacks)
    res = perform_operations(all_stacks)
    print(all_stacks)
    solution1 = get_first_element(res)
    print("solution 1")
    print(solution1)
    print("solution 2")
    res2 = perform_operations2(all_stacks)
    solution2 = get_first_element(res2)
    print(solution2)


if __name__ == "__main__":
    main()

