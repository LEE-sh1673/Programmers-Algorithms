def solution(dirs):
    visited = set()
    dir_map = { "U": (1,0), "L": (0,-1), "R": (0,1), "D": (-1,0)}
    curr_x, curr_y = 0, 0
    
    for dir in dirs:
        x, y = dir_map[dir]
        next_x = curr_x + x
        next_y = curr_y + y
        
        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5:
            continue
            
        visited.add((next_x, next_y, curr_x, curr_y))
        visited.add((curr_x, curr_y, next_x, next_y)) 
        curr_x, curr_y = next_x, next_y
    
    return len(visited) // 2
