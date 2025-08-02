"""
https://leetcode.com/problems/longest-consecutive-sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)

        for n in numsSet:
            if (n-1) not in numsSet:
                length = 0
                while (n + length) in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest


nums = [100, 4, 200, 1, 3, 2]

print(Solution().longestConsecutive(nums))