class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=nums[0]
        max_product=nums[0]
        min_product=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i] >=0:
                max_product=max(max_product * nums[i],nums[i])
                min_product=min(min_product * nums[i],nums[i]) 
            else:
                temp = max_product
                max_product=max(min_product * nums[i],nums[i])
                min_product =min(temp * nums[i],nums[i])
            result =max(result,max_product)
        return result       