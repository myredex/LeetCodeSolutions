"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:

    @staticmethod
    def string_map(string: str):
        """
        Build hashmap of the string
        :param string: Some text
        :return: Dictionary with symbols counted
        """

        char_count = {}

        # Go through the string
        for letter in string:
            # Count letters
            char_count[letter] = char_count.get(letter, 0) + 1

        return char_count

    def isAnagram(self, s: str, t: str) -> bool:

        # Get and compare hashmaps
        s_map = self.string_map(s)
        t_map = self.string_map(t)

        return s_map == t_map