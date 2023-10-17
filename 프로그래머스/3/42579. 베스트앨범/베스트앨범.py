def solution(genres, plays):
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    
    genreSort = sorted(list(d.keys()), key= lambda genre: sum(map(lambda song_info: song_info[0], d[genre])), reverse = True)
    answer = []
    for genre in genreSort:
        sorted_info = [song_info[1] for song_info in sorted(d[genre], key= lambda song: (song[0], -song[1]), reverse = True)]
        answer += sorted_info[:min(len(sorted_info), 2)]
    return answer