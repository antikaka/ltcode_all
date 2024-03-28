
"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ...

# s = "abcadcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "ckilbkd"
# s = " "
s = "dvdf"
# s = "au"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_test = []
        s_longest = []
        if len(s) == 1:
            return 1
        for num, char in enumerate(s):
            for num2, char2 in enumerate(s):
                if num >= num2:
                    continue
                if len(s_test) > 94 or len(s_longest) > 94:
                    return 95
                if len(s_test) < 1:
                    s_test.append(char)
                if char2 in s_test:
                    if len(s_test) > len(s_longest):
                        s_longest = s_test
                    s_test = []
                    break
                else:
                    s_test.append(char2)
        if len(s_test) > len(s_longest):
            s_longest = s_test
        return len(s_longest)

# seen = {}
# start = result = 0
# for num, char in enumerate(s):
#     if seen.get(char, -1) >= start:
#         start = seen[char] + 1
#     result = max(result, num - start + 1)
#     seen[char] = num


# print(seen)
# print(result)