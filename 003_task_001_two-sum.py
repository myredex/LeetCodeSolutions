"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen: dict[int, int] = {}

        for index, n in enumerate(nums):

            # Count residual
            residual = target - n

            # If residual in seen already return the answer
            if residual in seen:
                return [seen[residual], index]

            # If not in seen save in hashmap
            seen[n] = index
