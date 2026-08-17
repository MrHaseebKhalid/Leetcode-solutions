class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        nums = set(nums)
        while left <= right:
            if left not in nums:
                return left
            elif right not in nums:
                return right
            left += 1
            right -= 1
        


