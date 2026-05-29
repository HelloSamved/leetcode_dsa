class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = min(strs), max(strs)
        for i, c in enumerate(s[0]):
            if c != s[1][i]:
                return s[0][:i]
        return s[0]