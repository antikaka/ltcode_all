
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

from typing import List


from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        countmax = 0
        lettercount = 0
        wordcount = 0
        longestword = len(max(strs, key=len))
        strs_count = len(strs)

        if len(min(strs, key=len)) == 0:
            return ""
        if longestword <= 0:
            return ""

        for num, string in enumerate(strs):
            count = 0
            for num2, string2 in enumerate(strs):
                if string2.startswith(string[0]):
                    count += 1
                else:
                    return ""
            if count >= countmax:
                countmax = count
            else:
                strs.pop(num)

        print(strs_count, len(strs))
        if strs_count > len(strs):
            return ""

        if len(strs) == 1:
            return strs[0]
        if countmax <= 1:
            return ""

        longestword = len(max(strs, key=len))

        for num, string in enumerate(strs):                             #per string
            for ilgis in range(1, longestword + 1):                          #imi tiek raidziu
                commcount = 0
                for num2, string2 in enumerate(strs):                   #tikrini string2
                    if string2.startswith(string[0:ilgis]):
                        commcount += 1
                if commcount >= countmax:
                    lettercount = ilgis
                    wordcount = num
        return strs[wordcount][0:lettercount]

