import Foundation

func solution(_ numer1:Int, _ denom1:Int, _ numer2:Int, _ denom2:Int) -> [Int] {
    var numer3: Int, denom3: Int = 0

    if denom1 == denom2 {
        numer3 = numer1 + numer2
        denom3 = denom1
    } else {
        numer3 = (numer1 * denom2) + (numer2 * denom1)
        denom3 = denom1 * denom2
    }

    let greatestCommonDivison = gcd(numer3, denom3)

    numer3 /= greatestCommonDivison
    denom3 /= greatestCommonDivison

    return [numer3, denom3]
}

func gcd(_ a: Int, _ b: Int) -> Int {
    if b == 0 {
        return a
    } else {
        return gcd(b, a % b)
    }
}
