"""
https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        # Count items and save in list of lists
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Get result from the list of lists
        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
            if len(result) >= k:
                return result[:k]

nums = [1,1,1,2,2,3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))