class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Sign handling
        positive = (dividend >= 0) == (divisor >= 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Double divisor until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return quotient if positive else -quotient