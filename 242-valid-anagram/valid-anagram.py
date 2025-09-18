from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       l=Counter(s)
       n=Counter(t)
       if l == n:
          return True
       else:
          return False