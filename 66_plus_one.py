
"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""
        temp2 = []
        for char in digits:
            temp += str(char)
        temp = list(str(int(temp) + 1))
        for char in temp:
            temp2.append(int(char))
        return temp2

solution = Solution()
print(solution.plusOne([1,2,3]))
