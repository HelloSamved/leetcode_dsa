class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        res = ""
        cycle = 2 * (numRows - 1)

        for row in range(numRows):

            for j in range(row, len(s), cycle):

                res += s[j]

                # middle rows get one extra character
                diag = j + cycle - 2 * row

                if 0 < row < numRows - 1 and diag < len(s):
                    res += s[diag]

        return res