from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True   # checks monotone increasing
        dec = True   # checks monotone decreasing

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                inc = False
            if nums[i] < nums[i + 1]:
                dec = False

        return inc or dec
