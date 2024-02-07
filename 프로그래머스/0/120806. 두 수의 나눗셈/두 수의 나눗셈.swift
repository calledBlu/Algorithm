import Foundation

func solution(_ num1:Int, _ num2:Int) -> Int {
    guard (0 < num1 && num1 <= 100) && (0 < num2 && num2 <= 100) else { return -1 }
    
    return Int(Double(num1) / Double(num2) * 1000)
}