class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
            if dict[i] >= 2:
                return i
            