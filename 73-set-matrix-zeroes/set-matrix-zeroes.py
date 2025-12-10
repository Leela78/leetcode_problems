from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Uses O(m + n) extra space.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])

        rows_to_zero = [False] * m
        cols_to_zero = [False] * n

        # First pass: record rows and cols that must be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero[i] = True
                    cols_to_zero[j] = True

        # Second pass: apply zeros
        for i in range(m):
            for j in range(n):
                if rows_to_zero[i] or cols_to_zero[j]:
                    matrix[i][j] = 0
