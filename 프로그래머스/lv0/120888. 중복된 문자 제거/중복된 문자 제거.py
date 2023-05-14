def solution(my_string):
    answer = ''
    # key로 문자열을, 값으로 횟수를 저장할 딕셔너리를 생성한다.
    my_dict = {}
    
    # 문자열을 한번씩 돌면서 문자가 존재하는 경우 1을 더하도록, 존재하지 않는 경우 0을 할당 후 1을 더하도록 한다.
    for i in my_string:
        my_dict[i] = my_dict.get(i, 0) + 1
        
    # key값에 해당하는 것들만 answer에 더한다.
    for key in my_dict.keys():
        answer += key
        
    return answer