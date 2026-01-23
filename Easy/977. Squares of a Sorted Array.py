from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [x**2 for x in nums]
        
        ans = []
        i = 0 # right pointer
        
        while nums[i] < 0 and i + 1 < len(nums):
            i += 1
        
        j = i - 1 # left pointer
        nums = [x**2 for x in nums]

        while j >= 0 and i < len(nums):
            if nums[j] < nums[i]:
                ans.append(nums[j])
                j -= 1
            else:
                ans.append(nums[i])
                i += 1
        
        while j >= 0:
            ans.append(nums[j])
            j -= 1

        while i < len(nums):
            ans.append(nums[i])
            i += 1
        
        return ans

        


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedSquares(nums = [-5,-3,-2,-1]))
    print(sol.sortedSquares(nums = [-1]))
    print(sol.sortedSquares(nums = [1, 2]))
    print(sol.sortedSquares(nums = [-2, 10]))
    print(sol.sortedSquares(nums = [-4,-1,0,3,10]))
    print(sol.sortedSquares(nums = [-7,-3,2,3,11]))