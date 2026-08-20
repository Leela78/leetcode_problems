class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        rotate=[[0]*n for _ in range(n)]
        for i in range(n):
           for j in range(n):
                rotate[j][(n-1)-i]= matrix[i][j]
        matrix[:]=rotate    