class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        max_jump=0
        jump=0
        curr=0
        for i in range(n-1):
           max_jump=max(max_jump,nums[i]+i) 
           if i==curr:
            jump+=1
            curr =max_jump
        return jump     

