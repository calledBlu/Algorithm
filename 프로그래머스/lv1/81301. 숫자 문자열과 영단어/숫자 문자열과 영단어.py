def solution(s):
    new_word = s
    
    # 숫자가 key이고 영단어가 value인 dictionary를 생성
    alpha_dict = {"0": "zero",
                  "1": "one",
                  "2": "two",
                  "3": "three",
                  "4": "four",
                  "5": "five",
                  "6": "six",
                  "7": "seven",
                  "8": "eight",
                  "9": "nine"}
    
    # replace 메서드 활용하기
    for key, value in alpha_dict.items():
        new_word = new_word.replace(value, key)
    
    answer = int(new_word)
    return answer