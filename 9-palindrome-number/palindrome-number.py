class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit=0
        m=x
        rem=0
        digit=0
        while(x > 0):
            rem=x%10
            digit = digit*10 + rem
            x =x//10
        if digit == m:
            return True
        else:
            return False    