def get_file_lines_as_list(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def get_file_as_str(filename):
    with open(filename) as file:
        content = file.read()
    return content

def read_file_into_matrix(filename):
    matrix = []
    with open(filename, 'r') as f:
        matrix = [list(line.strip()) for line in f]
    return matrix
