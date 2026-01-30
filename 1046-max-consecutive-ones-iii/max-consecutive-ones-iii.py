class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count=0
        zero_count=0
        left=0
        n=len(nums)
        for i in range(n):
            if nums[i] == 0:
                zero_count +=1
            while zero_count> k:
                if nums[left]==0:
                    zero_count -=1
                left +=1
            max_count=max(max_count,i-left+1)
        return max_count               