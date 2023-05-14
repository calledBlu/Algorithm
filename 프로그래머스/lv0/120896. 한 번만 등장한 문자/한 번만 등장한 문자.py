def solution(s):
    answer = ''
    # dictionary, set를 통한 접근방법
    # 문자열을 set으로 변환한 후 list 사용하여 정렬하고 문자열 내에 존재하는 값을 ticket 형태로 사용한다.
    ticket = list(set(s))
    ticket.sort()
    # 빈 dictionary를 생성한다.
    my_dictionary = {}
    
    # s 문자열을 하나씩 꺼내서 확인한다.
    for char in s:
        
        # 문자열이 딕셔너리의 키값에 존재하는 경우 +1
        # 문자열이 딕셔너리의 키값에 존재하지 않는 경우 0으로 하고 +1
        my_dictionary[char] = my_dictionary.get(char, 0) + 1
    
    # ticket에 있는 요소들을 하나씩 꺼내서 dictionary의 key로 사용해서 호출한다.
    for key in ticket:
        # value가 1인 것들만 answer 변수에 더한다.
        if my_dictionary[key] == 1:
            answer += str(key)
        else:
            continue
        
    return answer