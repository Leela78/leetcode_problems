class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left < right:
            sum =numbers[left] + numbers[right]
            if sum == target:
                return [left+1 ,right+1]
                break
            elif  sum < target:
                left = left +1
            else:
                right = right -1


