#
# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Language: python
# Date: 2026-04-29


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        freq = {}
        low = 0
        res = 0

        for high in range(n):
            freq[s[high]] = freq.get(s[high], 0) + 1

            while len(freq) < (high - low + 1):
                freq[s[low]] -= 1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1

            res = max(res, high - low + 1)

        return res
