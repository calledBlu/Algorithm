import Foundation

func solution(_ array:[Int]) -> Int {
    guard array.count != 1 else { return array[0] }

    var dic: [Int: Int] = [:]

    for num in array {
        let count = dic[num] ?? 0
        dic[num] = count + 1
    }

    guard dic.count != 1 else { return array[0] }

    let sortedDic = dic.sorted(by: { $0.1 > $1.1 })

    return sortedDic[0].value == sortedDic[1].value ? -1 : sortedDic[0].key
}