class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
    
        sum=0
        n=len(nums)
        for i in nums:
            sum +=i
            arr.append(sum)
        return arr    