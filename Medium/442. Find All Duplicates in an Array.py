from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # as in problem 448 we marked nums with negatives positions what we already senn
        # and if we already see that negative just add it to res
        res = []

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] *= -1
            elif nums[idx] < 0:
                res.append(idx + 1)
            

        return res
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicates(nums = [4,3,2,7,8,2,3,1]))