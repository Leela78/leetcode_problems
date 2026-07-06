class Solution:
    def reverse(self, x: int) -> int:
        r=0
        num=x
        neg=False
        if x<0:
            x=abs(x)
            neg=True
        while x>0:
            rem=x%10
            r=r*10+rem
            x=x//10
        if neg:
            r= -r 
        if r < -(2**31) or r>(2**31):
            return 0
        else:
            return r    
              
        