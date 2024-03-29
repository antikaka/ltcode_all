
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for string in strs:
            string_check = "".join(sorted(string))
            if string_check in check.keys():
                check[string_check].append(string)
            else:
                check[string_check] = [string]
        answer = []
        for key, value in check.items():
            answer.append(value)
        return answer



strs = ["eat","tea","tan","ate","nat","bat"]
check = {}
for string in strs:
    string_check = "".join(sorted(string))
    if string_check in check.keys():
        check[string_check].append(string)
    else:
        check[string_check] = [string]
answer = []
for key, value in check.items():
    answer.append(value)

print(answer)