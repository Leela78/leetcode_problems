class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first=[]
        second=[]
        total=0
        for i in range(m):
            first.append(nums1[i])
        for j in range(n):
            second.append(nums2[j])
        total=first+second
        total.sort()
        nums1[:]=total

          




        