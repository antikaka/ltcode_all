
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        ...


num = 9

check = [1000, 500, 100, 50, 10, 5, 1]
check_f = [1, 3, 5]
romenai = []
romenai_num = ["M", "D", "C", "L", "X", "V", "I"]

answer = ""
for i, numcheck in enumerate(check):
    print(str(num)[0])
    if i in check_f and num // (check[i + 1]) == 9:
        romenai.append("dev")
        if len(str(num)) <= 1:
            num = 0
        else:
            num = int(str(num)[1:])
    else:
        romenai.append(num // numcheck)
        num -= romenai[i] * numcheck
    print(i, romenai)
    if i not in check_f and romenai[i] == 4:
        answer += romenai_num[i] + romenai_num[i - 1]
        print("if", 4, answer)
    elif i in check_f and romenai[i] == "dev":
        answer += romenai_num[i + 1] + romenai_num[i - 1]
        print("if", 9, answer)
    else:
        answer += romenai[i] * romenai_num[i]

print(romenai, answer)