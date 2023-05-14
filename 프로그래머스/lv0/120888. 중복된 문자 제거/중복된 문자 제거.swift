import Foundation


func solution(_ my_string:String) -> String {
    // 문자를 저장할 배열을 선언한다.
    var my_array: [String] = []
    
    // 문자 시작점부터 끝까지 한 개씩 뽑아서 비교한다.
    for i in my_string {
        // 문자열에서 한 글자를 뽑아오면 Character이므로 String타입으로 변환한다
        let charString = String(i)
        
        // 뽑아온 문자가 새로 선언한 배열에 있는 경우
        if my_array.contains(charString) {
            // 다른 액션을 취하지 않고 지나간다
            continue
            // 새로 선언한 배열에 없는 경우
        } else {
            // 배열에 추가해 준다
            my_array.append(charString)
        }
    }
    // 전체 반복문 반복 후 배열에 저장된 요소를 붙여서 반환시켜준다.
    var result = my_array.joined()

    return result
}