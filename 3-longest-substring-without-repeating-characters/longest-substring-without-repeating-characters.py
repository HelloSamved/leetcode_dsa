class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            if ch in char_map and char_map[ch] >= left:
                left = char_map[ch]   # move left past the previous occurrence
            char_map[ch] = right + 1  # store next valid start position
            max_len = max(max_len, right - left + 1)
        return max_len