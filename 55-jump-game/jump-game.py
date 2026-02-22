class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump=0
        n=len(nums)
        for i in range(n):
            if i > max_jump:
                return False
            max_jump=max(max_jump,nums[i]+i)
            if  max_jump >= n-1:
                return True
        return False        

               