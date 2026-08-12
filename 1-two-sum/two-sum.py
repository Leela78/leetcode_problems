class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        n=len(nums)
        for i in range(n):
            compliment =target-nums[i]
            if compliment in hash:
                return [hash[compliment],i]
            hash[nums[i]]=i
                

