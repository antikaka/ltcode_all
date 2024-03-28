

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if (target - value) == value2 and index != index2:
                    return [index, index2]






list1 = [2,7,11,15]
target1 = 9
list2 = [3,2,4]
target2 = 6
list3 = [3,3]
target3 = 6

solution = Solution()
print(solution.twoSum(list3, target3))