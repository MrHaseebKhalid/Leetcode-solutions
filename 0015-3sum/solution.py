class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i, x in enumerate(nums):

            if i == n - 2:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = x + nums[left] + nums[right]
                
                if current_sum == 0:
                    triplet = [x, nums[left], nums[right]]
                    ans.append(triplet)
                    
                    left += 1
                    right -= 1
                    

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    

                elif current_sum < 0:
                    left += 1
                    
                else:
                    right -= 1

        return ans

