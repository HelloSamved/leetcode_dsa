class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        curRow = 0
        direction = 1

        for char in s:

            rows[curRow] += char

            # Change direction
            if curRow == 0:
                direction = 1
            elif curRow == numRows - 1:
                direction = -1

            curRow += direction

        return "".join(rows)