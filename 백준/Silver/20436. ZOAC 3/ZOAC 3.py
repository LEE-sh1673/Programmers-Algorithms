from sys import stdin

consonants = 'qwertasdfgzxcv'
vowels = 'yuiophjklbnm'
positions = {
    'q': (0, 0),
    'w': (0, 1),
    'e': (0, 2),
    'r': (0, 3),
    't': (0, 4),
    'a': (1, 0),
    's': (1, 1),
    'd': (1, 2),
    'f': (1, 3),
    'g': (1, 4),
    'z': (2, 0),
    'x': (2, 1),
    'c': (2, 2),
    'v': (2, 3),
    'y': (0, 5),
    'u': (0, 6),
    'i': (0, 7),
    'o': (0, 8),
    'p': (0, 9),
    'h': (1, 5),
    'j': (1, 6),
    'k': (1, 7),
    'l': (1, 8),
    'b': (2, 4),
    'n': (2, 5),
    'm': (2, 6),
}

input = stdin.readline
L, R = input().strip().split()
word = input().strip()
answer = 0

for ch in word:
    x2, y2 = positions[ch]

    # 현재 단어가 자음이라면
    if ch in consonants:
        x1, y1 = positions[L]
        answer += abs(x1 - x2) + abs(y1 - y2) + 1
        L = ch

    # 현재 단어가 모음이라면
    if ch in vowels:
        x1, y1 = positions[R]
        answer += abs(x1 - x2) + abs(y1 - y2) + 1
        R = ch

print(answer)
