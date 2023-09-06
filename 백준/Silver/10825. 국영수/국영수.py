from sys import stdin


def map_to_name_and_grades(student: str) -> tuple:
    name, kor, eng, math = student.split(' ')
    return -int(kor), int(eng), -int(math), name


scores = list(map(map_to_name_and_grades, stdin.readlines()[1:]))
print(*map(lambda score: score[3], sorted(scores)), sep='\n')
