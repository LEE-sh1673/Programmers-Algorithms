def solution(dirs):
    answer = 0
    
    # 현재 방향 값을 읽는다.
    # 기존에 지나왔던 길인지 확인한다.
    # 현재 방향 값으로 갈 수 있는지 여부를 확인한다.
    # 갈 수 있다면, 해당 방향만큼 거리를 증가시키고, 지나왔던 길로 체크한다.
    # 위 과정을 반복한다.
    
    visited = []
    dir_map = { "U": (1,0), "L": (0,-1), "R": (0,1), "D": (-1,0)}
    curr_x, curr_y = 0, 0
    
    for dir in dirs:
        x, y = dir_map[dir]
            
        next_x = curr_x + x
        next_y = curr_y + y
        
        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5:
            continue

        is_visited = False
        
        for mark, prev_x, prev_y in visited:
            off_x, off_y = dir_map[mark]
            
            if (prev_x + off_x, prev_y + off_y) == (curr_x, curr_y) and (prev_x, prev_y) == (next_x, next_y):
                is_visited = True
                break
                
            if (prev_x + off_x, prev_y + off_y) == (next_x, next_y) and (prev_x, prev_y) == (curr_x, curr_y):
                is_visited = True
                break
            
        if not is_visited:
            visited.append((dir, curr_x, curr_y))
        
        curr_x = next_x
        curr_y = next_y
    
    return len(visited)
