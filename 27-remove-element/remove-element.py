class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        k=0
        for i in range(n):
            if val != nums[i]:
                nums[k]=nums[i]
                k += 1
        return  k   
               
        