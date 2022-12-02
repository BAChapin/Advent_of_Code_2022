import sys
sys.path.append('..')
from helper import get_lines, time_func

# Rock:     A ; 1
# Paper:    B ; 2
# Scissors: C ; 3
# Win:      Z ; 6
# Lose:     X ; 0
# Draw:     Y ; 3

def choice_value(opponent): # return (win, lose, draw)
    if opponent == 'A':
        return (2, 3, 1)
    elif opponent == 'B':
        return (3, 1, 2)
    else:
        return (1,2,3)


def score(round):
    elf_choice = round[0]
    desired_outcome =  round[2]
    elf_check = choice_value(elf_choice)

    if desired_outcome == 'Z':
        return 6 + elf_check[0]
    elif desired_outcome == 'X':
        return 0 + elf_check[1]
    else:
        return 3 + elf_check[2]


def process():
    lines = get_lines()
    mapped_scores = map(score, lines)
    score_list = list(mapped_scores)
    summed_scores = sum(score_list)
    return summed_scores

if __name__ == '__main__':
    time_func(process)