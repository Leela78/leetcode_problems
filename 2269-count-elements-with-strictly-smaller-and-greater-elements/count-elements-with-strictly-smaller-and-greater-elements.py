class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_element =max(nums)
        min_element=min(nums)
        count=0
        for i in range(len(nums)):
            if nums[i] > min_element and nums[i]  < max_element:
                count +=1
        return count        


