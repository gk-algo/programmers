from collections import defaultdict


CHOICE_ELEMENT = {
    'no': [1, 2, 3],
    'none': [4],
    'yes': [5, 6, 7]
}


PERSONALITY_TYPE = [('R', 'T'), ('F', 'C'), ('M', 'J'), ('A', 'N')]


def _get_score(choice):
    return abs(4-choice)


def solution(survey, choices):
    answer = defaultdict(int)
    for i, q_type in enumerate(survey):
        choice = choices[i]
        if choice in CHOICE_ELEMENT['no']:
            answer[q_type[0]] += _get_score(choice)
        elif choice in CHOICE_ELEMENT['yes']:
            answer[q_type[1]] += _get_score(choice)

    result = ''
    for _type in PERSONALITY_TYPE:
        if answer[_type[0]] == answer[_type[1]]:
            result += sorted([_type[0], _type[1]])[0]
        else:
            result += _type[0] if answer[_type[0]] > answer[_type[1]] else _type[1]

    return result
