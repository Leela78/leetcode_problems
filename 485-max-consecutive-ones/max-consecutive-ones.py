class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count=0
        max_count=0
        for i in range(len(nums)):
            if nums[i]==0:
                one_count =0
            else:
               one_count +=1
               max_count =max(max_count,one_count)
        return max_count            
