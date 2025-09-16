class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash:
                return [hash[complement], i]
            
            hash[nums[i]] = i

     