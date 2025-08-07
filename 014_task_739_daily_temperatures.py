"""
https://leetcode.com/problems/daily-temperatures
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # index, temp
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((i, t))
        return res

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))