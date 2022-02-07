class Solution:
    _symbolsList: str = [
        ['M', 1000],
        ['D', 500],
        ['C', 100],
        ['L', 50],
        ['X', 10],
        ['V', 5],
        ['I', 1],
    ]

    def intToRoman(self, num: int) -> str:
        result = ''
        
        if num >= 1000:
            countM = num // 1000
            result += "M" * countM
            num -= 1000 * countM

        if num >= 500:
            if num >= 900:
                result += "CM"
                num -= 900
            else:
                countD = num // 500
                result += "D" * countD
                num -= 500 * countD

        if num >= 100:
            if num >= 400:
                result += "CD"
                num -= 400
            else:
                countC = num // 100
                result += "C" * countC
                num -= 100 * countC

        if num >= 50:
            if num >= 90:
                result += "XC"
                num -= 90
            else:
                countL = num // 50
                result += "L" * countL
                num -= 50 * countL
        
        if num >= 10:
            if num >= 40:
                result += "XL"
                num -= 40
            else:
                countX = num // 10
                result += "X" * countX
                num -= 10 * countX
        
        
        if num >= 5:
            if num == 9:
                result += "IX"
                num -= 9
            else:
                countV = num // 5
                result += "V" * countV
                num -= 5 * countV
        
        
        if num >= 1:
            if num == 4:
                result += "IV"
                num -= 4
            else:
                countI = num
                result += "I" * countI

        return result

      


solution = Solution()

res1 = solution.intToRoman(3)
ans1 = "III"
print("{}: {}".format(res1 == ans1, res1))

res2 = solution.intToRoman(58)
ans2 = "LVIII"
print("{}: {}".format(res2 == ans2, res2))

res3 = solution.intToRoman(1994)
ans3 = "MCMXCIV"
print("{}: {}".format(res3 == ans3, res3))

res4 = solution.intToRoman(3999)
ans4 = "MMMCMXCIX"
print("{}: {}".format(res4 == ans4, res4))
