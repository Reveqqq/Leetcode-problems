from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = None
        l = None
        n = len(nums)
        for i in range(n - 1):
            if nums[i] < nums[i+1]:
                k = i
        
        # nums contains the last permutation
        if k is None:            
            nums[:] = nums[::-1]
            return

        for i in range(k,n):
            if nums[k] < nums[i]:
                l = i

        nums[l], nums[k] = nums[k], nums[l]

        nums[k+1:n] = nums[k+1:n][::-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(nums)

    for _ in range(6):
        sol.nextPermutation(nums = nums)
        print(nums)
    
    