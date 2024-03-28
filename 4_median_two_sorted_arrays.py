"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        ind = int(len(nums1) / 2)
        if len(nums1) % 2 == 0:
            return (nums1[ind] + nums1[ind - 1]) / 2
        else:
            return nums1[ind]

