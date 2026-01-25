from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return nums
        
        i = 0

        for j in range(len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] != 0:
                i += 1
        
    
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)

    print(nums)
    
