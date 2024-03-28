"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        num = []
        for ilgis in range(len(x_str)):
            num.append(x_str[ilgis])
        num_back = num[::-1]
        test_num = "".join(num_back)
        if test_num == x_str:
            return True
        else:
            return False

        # return str(x) == str(x)[::-1]