class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""

        for i in range(len(s)):

            # odd and even centers
            for l, r in [(i, i), (i, i + 1)]:

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1

                # palindrome length = r - l - 1
                if r - l - 1 > len(palindrome):
                    palindrome = s[l + 1:r]

        return palindrome