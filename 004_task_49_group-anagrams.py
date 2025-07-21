"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

class Solution:

    def groupAnagrams(self, strs):

        seen = {}

        for str in strs:

            # Sort each string it'll bee key of seen
            sorted_str = "".join(sorted(str))

            # Save string in hashmap
            seen.setdefault(sorted_str, []).append(str)

        # Return values of the hashmap as list of lists
        return list(seen.values())
