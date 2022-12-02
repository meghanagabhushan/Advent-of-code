from shutil import move

input_file = "input2.txt"

def get_file_lines_as_list(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def get_win_score(win_status,lose_status,draw_status):
    if win_status:
        return 6
    elif draw_status:
        return 3
    elif lose_status:
        return 0

def get_score(val):
    opponent_move = val.split(" ")[0]
    own_move = val.split(" ")[1]
    own_move_simple = own_move.replace("X","A").replace("Y","B").replace("Z","C")
    win_status = False
    lose_status = False
    draw_status = False
    move_status_score = {"A":1,"B":2,"C":3}
    if opponent_move==own_move_simple:
        draw_status = True
    elif opponent_move=='A' and own_move_simple=='B':
        win_status=True
    elif opponent_move=='B' and own_move_simple=='A':
        lose_status=True
    elif opponent_move=='A' and own_move_simple=='C':
        lose_status=True
    elif opponent_move=='C' and own_move_simple=='A':
        win_status=True
    elif opponent_move=='B' and own_move_simple=='C':
        win_status=True
    elif opponent_move=='C' and own_move_simple=='B':
        lose_status=True
    return get_win_score(win_status,lose_status,draw_status) + move_status_score[own_move_simple]

def get_score_part2(val):
    opponent_move = val.split(" ")[0]
    result = val.split(" ")[1]
    win_combo = {"A":"B","B":"C","C":"A"}
    lose_combo = {"A":"C","B":"A","C":"B"}
    draw_combo = {"A":"A","B":"B","C":"C"}
    values = {"A":1,"B":2,"C":3}
    if result=='X':
        return values[lose_combo[opponent_move]]+0
    elif result=='Y':
        return values[draw_combo[opponent_move]]+3
    elif result=='Z':
        return values[win_combo[opponent_move]]+6


def main():
    data = get_file_lines_as_list(input_file)
    print(data)
    total_score = 0
    total_score_part2 = 0
    for line in data:
        print(get_score(line))
        # total_score = total_score + get_score(line)
        total_score_part2 = total_score_part2 + get_score_part2(line)
    # print("total score part 1")
    # print(total_score)
    print("total score part 2")
    print(total_score_part2)

    

if __name__ == "__main__":
    main()
