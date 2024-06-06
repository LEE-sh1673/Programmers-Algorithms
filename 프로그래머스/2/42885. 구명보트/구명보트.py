def solution(people, limit):
    people.sort()
    nums_people = len(people)
    nums_pair = 0

    start = 0
    end = nums_people - 1

    while start < end:
        if people[start] + people[end] <= limit:
            nums_pair += 1
            start += 1
        end -= 1

    return nums_people - nums_pair
