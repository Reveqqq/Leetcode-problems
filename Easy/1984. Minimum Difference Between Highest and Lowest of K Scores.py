from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:    
        nums.sort(reverse=True)
        minDiff = nums[0] - nums[k-1]

        for i in range(len(nums) - k + 1):
            minDiff = min(minDiff, nums[i] - nums[k - 1 + i])
        
        return minDiff
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumDifference(nums = [9,2,10,1,10,4,8,9,7,6,8,10,8,6,5,4,3,4,2,10], k = 7))