class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) == len(set(nums)):
            return False

        seen = set()
        
        for index,item in enumerate(nums):
            if item in seen:
                return True

            seen.add(item)

            if len(seen) > k:
                seen.remove(nums[index-k])

        return False
