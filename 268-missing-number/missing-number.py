class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=sorted(nums)
        for i in range(0,len(nums)):
            if i!=k[i]:
                return i
        return len(nums)        