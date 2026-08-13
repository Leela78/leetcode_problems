class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        positive=0
        negitive=1
        for i in nums:
            if i>0:
                arr[positive]=i
                positive+=2
            else:
                arr[negitive]=i
                negitive+=2
        return arr                   