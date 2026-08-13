class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        max_sum=0
        summ=0
        for j in range(i+1,len(prices)):
            if prices[j]<prices[i]:
                i=j
            else:    
                summ = prices[j]-prices[i]
                if summ > max_sum:
                    max_sum=summ
        return max_sum        
