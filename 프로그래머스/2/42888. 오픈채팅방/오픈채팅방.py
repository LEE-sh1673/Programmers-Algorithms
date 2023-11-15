def solution(record):
    msg_info = []
    uid_info = {}
    
    for command_info in record:
        splitted_info = command_info.split(" ")
        
        if splitted_info[0] == 'Enter':
            op, uid, name = splitted_info
            uid_info[uid] = name
            msg_info.append(('님이 들어왔습니다.', uid))
        
        if splitted_info[0] == 'Leave':
            op, uid = splitted_info
            msg_info.append(('님이 나갔습니다.', uid))
        
        if splitted_info[0] == 'Change':
            op, uid, name = splitted_info
            uid_info[uid] = name
    
    answer = []
    for msg, uid in msg_info:
        answer.append(uid_info[uid] + msg)
        
    return answer
        
        