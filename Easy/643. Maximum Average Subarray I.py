from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_avg = cur_sum / k

        for i in range(len(nums) - k):
            cur_sum = cur_sum - nums[i] + nums[k+i]
            max_avg = max(max_avg, cur_sum / k)

        return max_avg


if __name__ == "__main__":
    sol = Solution()

    print(sol.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
    print(sol.findMaxAverage(nums = [0,1,1,3,3,0], k = 4))