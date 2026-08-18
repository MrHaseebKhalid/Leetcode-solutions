class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        index = 0
        shift = 0
        while shift != n:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
            shift += 1
