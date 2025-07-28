"""
https://leetcode.com/problems/encode-and-decode-strings/
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""
from typing import List

input_str = ["neet","code","love","you"]

output_str = ["neet","code","love","you"]

def encode(strs: List[str]) -> str:
    res = ''.join(f"{len(s)}#{s}" for s in strs)
    return res

def decode(strs: str) -> List[str]:
    res, i = [], 0
    while i < len(strs):
        j = i
        while strs[j] != "#":
            j += 1
        length = int(strs[i:j])
        i = j + 1 + length
        res.append(strs[j+1 : i])
    return res

x = encode(input_str)
print(decode(x))