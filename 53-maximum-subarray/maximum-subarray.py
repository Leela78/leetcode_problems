class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        sum=0
        n=len(nums)
        for j in range(n):
                sum  +=nums[j]
                max_sum=max(max_sum,sum)
                if sum < 0:
                    sum=0
        return max_sum        