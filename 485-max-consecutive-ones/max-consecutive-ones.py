class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count=0
        max_count=0
        for i in nums:
            if i==1:
                one_count+=1
            else:
                max_count=max(one_count,max_count)
                one_count=0
        max_count=max(one_count,max_count)
        return max_count            
                           
