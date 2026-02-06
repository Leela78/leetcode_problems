class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x=abs(x) 
        digit=0
        while x > 0:
            rem= x%10
            digit=digit*10 +rem
            x=x//10
        digit *=sign    
        if digit < -2 **31-1 or digit > 2**31-1:
            return 0
        else:
            return digit

 

            
            