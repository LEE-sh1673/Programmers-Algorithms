"""
- 재생 시간과 제공된 악보를 직접 보면서 비교
- [음악 제목, 재생이 시작되고 끝난 시각, 악보]를 제공한다.
- 악보에 사용되는 음은 [C, C#, D, D#, E, F, F#, G, G#, A, A#, B]
- 각 음은 1분에 1개씩 재생된다. 
- 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 
- 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
- 음악이 00:00를 넘겨서까지 재생되는 일은 없다.
- 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
- 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
- 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.

[입력]
- 네오가 기억한 멜로디를 담은 문자열 m
-  방송된 곡의 정보를 담고 있는 배열 musicinfos
    -  [음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보]
    - 시각은 24시간 HH:MM 형식

[출력]
- 조건과 일치하는 음악 제목


1. 방송된 곡 정보에 대해 전처리를 수행한다.
    1. 총 재생 시간 (= 음악 끝난 시간 - 음악 시작 시간)을 구한다.
    2. 총 재생 시간에 따라 [악보 정보]를 반복한다.
    
2. 멜로디 [m]에 대해 수정된 [악보 정보]와 다음 연산을 수행한다.
    1. [악보 정보]에서 [m]이 존재하는 [악보 정보]를 구한다.

3. <2>에서 나온 [악보 정보]에 따라 다음을 진행한다.

    3.A 조건에 일치하는 [악보 정보]가 없다면: "(None)"
    3.B 조건에 일치하는 [악보 정보]가 여러 개라면:
        1. 총 재생 시간이 제일 긴 [악보 정보]의 [제목]을 반환한다.
        
        3.B.A 총 재생 시간도 같다면:
            1. 먼져 입력된 [악보 정보]의 [제목]을 반환한다.
"""
def solution(m, musicinfos):
    repeated_musics = []
    m = encode_melody(m)
    
    for info in musicinfos:
        s_time, e_time, title, melody = info.split(',')
        times = time_diff(s_time, e_time)
        melody = repeat_melody(encode_melody(melody), times)        
        repeated_musics.append((title, times, melody))
        
    matched_musics = [music for music in repeated_musics if m in music[-1]]
    
    if not matched_musics:
        return '(None)'
    
    answer = matched_musics[0][0]

    if len(matched_musics) > 1:
        answer = max(matched_musics, key=lambda music : music[1])[0]
    
    return answer


def encode_melody(melody):
    return melody\
        .replace('A#', 'a')\
        .replace('C#', 'c')\
        .replace('D#', 'd')\
        .replace('F#', 'f')\
        .replace('G#', 'g')


def time_diff(start, end):
    s_hours, s_minutes = map(int, start.split(':'))
    e_hours, e_minutes = map(int, end.split(':'))    
    return (e_hours - s_hours) * 60 + (e_minutes - s_minutes)


def repeat_melody(melody, times):
    a, b = divmod(times, len(melody))
    return encode_melody(melody * a + melody[:b])
