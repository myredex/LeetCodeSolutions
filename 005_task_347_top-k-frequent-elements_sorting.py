"""
https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for n in nums:
            # Count elements in nums
            seen[n] = seen.get(n, 0) + 1

        sorted_seen = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_seen.keys())[:k]


nums = [1,1,1,2,2,3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))