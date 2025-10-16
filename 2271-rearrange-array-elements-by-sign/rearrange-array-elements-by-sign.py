class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negitive = 1
        n=len(nums)
        arr = [0] * n
        for i in range(n):
            if nums[i] < 0:
                arr[negitive] =nums[i]
                negitive +=2
            else:
                arr[positive] = nums[i]
                positive +=2
        return arr
                