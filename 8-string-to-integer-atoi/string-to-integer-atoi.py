class Solution:
    def myAtoi(self, s: str) -> int:

        max_num = 2**31 - 1
        min_num = -2**31

        s = s.strip()

        if not s:
            return 0

        sign = 1
        index = 0

        if s[0] == '-':
            sign = -1
            index += 1

        elif s[0] == '+':
            index += 1

        number = ""

        while index < len(s) and s[index].isdigit():
            number += s[index]
            index += 1

        if number == "":
            return 0

        answer = sign * int(number)

        if answer > max_num:
            return max_num

        if answer < min_num:
            return min_num

        return answer