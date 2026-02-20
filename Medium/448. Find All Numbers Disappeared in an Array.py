from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # let's say that nums are [1,1,3,4], but ideal nums should by [1,2,3,4]
        # and we want to mark 1 as already seen
        # we do it by idx = abs(nums[i]) - 1
        # abs(nums[0]) - 1 = 1 - 1 = 0
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] *= -1

        res = []
        # after transform we got nums like this:
        # [-1, 1, -3, -4]
        # there we see, that on idx = 1, there was no num = 2
        # so if nums[i] > 0 we easily add (i+1) as missing number
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)

        return res
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))