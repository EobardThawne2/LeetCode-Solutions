class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        n_str = str(n)
        x_str = ""
        digit_sum = 0
        for char in n_str:
            if char != '0':
                x_str += char
                digit_sum += int(char)
        if not x_str:
            return 0
        x = int(x_str)
        return x * digit_sum