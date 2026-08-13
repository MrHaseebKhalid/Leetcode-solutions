class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for x in range(n):
            nums1[m+x] = nums2[x]

        nums1.sort()
