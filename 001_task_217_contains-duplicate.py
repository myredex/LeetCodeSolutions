"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Define empty list
        checked_nums = []

        # Run loop throught the given list
        for num in nums:
            if num in checked_nums:
                return True
            else:
                checked_nums.append(num)

        # If all items checked return False
        return False