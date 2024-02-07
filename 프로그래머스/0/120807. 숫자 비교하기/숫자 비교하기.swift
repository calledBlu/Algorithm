import Foundation

func solution(_ num1:Int, _ num2:Int) -> Int {
    guard (0 <= num1 && num1 <= 10000) && (0 <= num2 && num2 <= 10000) else { return 0 }
    
    return num1 == num2 ? 1 : -1
}