def solution(routes):
    answer = 0
    routes.sort()
    camera = routes[0]
    
    for route in routes[1:]:
        if route[0] > camera[1]:
            answer += 1
            camera = route
        else:
            camera = [route[0], min(camera[1], route[1])]
    
    return answer + 1