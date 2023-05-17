def solution(id_list, report, k):
    # 이용자 ID 배열만큼의 인접 리스트를 생성하기 위한 count 선언
    count = len(id_list) - 1

    # id_list_padding = id_list
    # id_list_padding.insert(0, 0)

    # 총 신고 결과를 가지고 있을 visited dictionary 생성
    result = {}

    # 인접 리스트 틀 생성
    my_list = [[0] * (count + 1) for _ in range(count + 1)]

    # 인접 리스트에 값을 할당하는 과정
    for i in report:
        # 신고자, 피신고자를 start, end에 각각 할당
        start, end = map(str, i.split(" "))
        # id_list 중 신고자, 피신고자의 index 파악
        start_index = id_list.index(start)
        end_index = id_list.index(end)
        # 인접 리스트에 신고 여부를 할당
        # 상호 신고한 것이 아닌 한 쪽만 신고한 것이므로 역으로 할당은 안 해줌
        my_list[start_index][end_index] = 1

    # 인접리스트의 크기만큼 반복
    for j in range(len(id_list)):
        # 피신고자 index를 고정하여 신고당한 횟수를 count
        total = 0
        for h in range(len(id_list)):
            # 신고당한 횟수를 더해줌
            total += my_list[h][j]
        # 다 카운트했다면 그 수를 dictionary에 넣어줌
        result[j] = result.get(j, 0) + total

    print("result", result)
    # k번 이상 신고받은 사람들과 신고 횟수
    danger = []

    for key, value in result.items():
        if value >= k:
            danger.append(key)

    print("danger", danger)

    mail = [0] * len(my_list)
    # danger에 있는 사람들을 신고한 사람들을 찾기
    for y in danger:
        for q in range(len(my_list)):
            if my_list[q][y] == 1:
                mail[q] += 1

    answer = mail

    return answer