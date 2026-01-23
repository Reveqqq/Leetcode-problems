from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        mon_inc_flg = True
        mon_dec_flg = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                mon_inc_flg = False

            if nums[i] < nums[i+1]:
                mon_dec_flg = False
            
        return mon_inc_flg or mon_dec_flg
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMonotonic(nums = []))
    print(sol.isMonotonic(nums = [1]))
    print(sol.isMonotonic(nums = [1,3]))
    print(sol.isMonotonic(nums = [3,1]))
    print(sol.isMonotonic(nums = [1,2,2,3]))
    print(sol.isMonotonic(nums = [6,5,4,4]))
    print(sol.isMonotonic(nums = [1,3,2]))
