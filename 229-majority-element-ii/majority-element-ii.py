class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dic={}
        result=[]
        count=n//3
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]=dic.get(nums[i],0)+1
        for num in dic:
            if dic[num]> count:
                result.append(num)
        return result
