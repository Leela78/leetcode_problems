class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit =0
        for i in range(1,len(prices)):
               cost=prices[i]-min_val
               profit=max(profit,cost) 
               min_val=min(prices[i],min_val)
        return profit

        

        
     
        