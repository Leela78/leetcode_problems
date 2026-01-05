class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()          # Step 1: sort the array
        total = 0

        for i in range(0, len(nums), 2):  # Step 2: take every 2nd element
            total += nums[i]              # add the minimum of each pair

        return total
