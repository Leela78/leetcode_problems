class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]
        for i in range(n+1):
            ans=bin(i).count('1')
            arr.append(ans)
        return arr    


