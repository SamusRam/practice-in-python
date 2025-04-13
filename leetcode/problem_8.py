class Solution:
    def myAtoi(self, s: str) -> int:
        int_min = -2**31
        int_max = 2**31 - 1
        result = 0
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i == len(s):
            return result

        sign_mult = -1 if s[i] == '-' else 1
        if s[i] in {'+', '-'}:
            i += 1

        while i < len(s) and s[i].isdigit():
            next_digit = int(s[i])
            result *= 10
            result += next_digit
            i += 1
        
        result *= sign_mult

        if result < int_min:
            result = int_min
        elif result > int_max:
            result = int_max
        return result
