def solution(survey, choices):

    score = [0,0,0,0]
    answer = ''

    for i in range(len(survey)):
        if survey[i][0] == 'R':
            score[0] += -(choices[i] - 4)
        elif survey[i][0] == 'T':
            score[0] -= -(choices[i] - 4)
        elif survey[i][0] == 'C':
            score[1] += -(choices[i] - 4)
        elif survey[i][0] == 'F':
            score[1] -= -(choices[i] - 4)
        elif survey[i][0] == 'J':
            score[2] += -(choices[i] - 4)
        elif survey[i][0] =='M':
            score[2] -= -(choices[i] - 4)
        elif survey[i][0] == 'A':
            score[3] += -(choices[i] - 4)
        elif survey[i][0] == 'N':
            score[3] -= -(choices[i] - 4)

    if score[0] >= 0:
        answer += 'R'
    else:
        answer += 'T'

    if score[1] >= 0:
        answer += 'C'
    else:
        answer += 'F'

    if score[2] >= 0:
        answer += 'J'
    else:
        answer += 'M'

    if score[3] >= 0:
        answer += 'A'
    else:
        answer += 'N'


    return answer