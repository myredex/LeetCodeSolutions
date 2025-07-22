"""
https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
import heapq
from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Counting
        count = {} # num: freq
        for n in nums:
            # Count elements in nums
            count[n] = count.get(n, 0) + 1

        print(count)

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res



nums = [1,1,1,2,2,3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))