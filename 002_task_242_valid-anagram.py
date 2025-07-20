"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:

    def string_map(self, string: str):
        """
        Build hashmap of the string
        :param string: Some text
        :return: Dictionary with symbols counted
        """

        map = {}

        # Go through the string
        for letter in list(string):
            # Count letters
            map[letter] = map.get(letter, 0) + 1

        return map

    def isAnagram(self, s: str, t: str) -> bool:

        # Get and compare hashmaps
        s_map = self.string_map(s)
        t_map = self.string_map(t)

        return s_map == t_map