## Names Scores

## example: COLIN = 3+15+12+9+14 = 53
## and he is the 938th person on the list
## so his score is 938 * 15 = 49714

## What is the total of ALL the name scores in the file?

names = '/Users/aaronestes/projects/project_euler/22/names.txt'
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
from time import perf_counter

def create_alphabet_dict():
    return {letter: idx+1 for idx, letter in enumerate(alphabet)}

def structure_file_contents() -> list:
    all_names = []
    with open(names) as f:
        all_names.append(f.read())
    
    all_names_2 = [str(n).split(",") for n in all_names]
    return [sorted([str(a).replace("\"", "") for a in i]) for i in all_names_2]

def reset_vals():
    return [], 0

def calc_name_score_each_name(sorted_names: list, ad: dict) -> dict:
    sorted_names_score = {}
    curr_name = []
    curr_name_score = 0
    for name in sorted_names[0]:
        curr_name.append(str(name))
        for n in curr_name[-1]:
            curr_name_score += ad[str(n)]
        sorted_names_score[str(curr_name[0])] = curr_name_score
        curr_name, curr_name_score = reset_vals()
    return sorted_names_score

def calc_name_score_each_name_with_idx(name_score_each_name: dict) -> dict:
    return {str(val):(idx+1) * name_score_each_name[str(val)] for idx, val in enumerate(name_score_each_name)}

def solve():
    sorted_names = structure_file_contents()
    ad = create_alphabet_dict()
    name_score_each_name = calc_name_score_each_name(sorted_names, ad)
    name_score_each_name_with_index = calc_name_score_each_name_with_idx(name_score_each_name)
    return sum(name_score_each_name_with_index.values())

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} seconds to execute!')