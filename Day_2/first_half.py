import sys
sys.path.append('..')
from helper import get_lines, time_func

# Rock:     A, X ; 1
# Paper:    B, Y ; 2
# Scissors: C, Z ; 3

def outcome(opponent, choice):
    if opponent == 'A' and choice == 'Y' \
        or opponent == 'B' and choice == 'Z' \
        or opponent == 'C' and choice == 'X':
        return 6
    elif opponent == 'A' and choice == 'X' \
        or opponent == 'B' and choice == 'Y' \
        or opponent == 'C' and choice == 'Z':
        return 3
    else:
        return 0
    
def choice_value(choice):
    if choice == 'X': return 1
    elif choice == 'Y': return 2
    else: return 3

def score(round):
    elf_choice = round[0]
    my_choice =  round [2]
    return outcome(elf_choice, my_choice) + choice_value(my_choice)

def process():
    lines = get_lines()
    mapped_scores = map(score, lines)
    score_list = list(mapped_scores)
    summed_scores = sum(score_list)
    return summed_scores

if __name__ == '__main__':
    time_func(process)