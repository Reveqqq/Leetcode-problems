from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        counter = 0
        for idx in range(len(nums)):
            if nums[idx]:
                counter += 1
                
            max_ones = max(max_ones, counter)

            if not nums[idx]:
                counter = 0

        return max_ones

if __name__ == "__main__":
    sol = Solution()

    print(sol.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
