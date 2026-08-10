from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        for key,cou in count.items():
            if cou==1:
                return key
                


     