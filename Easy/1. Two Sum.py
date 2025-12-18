from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for j in range(len(nums)):
            miss = target - nums[j]
            if miss in hashmap and hashmap[miss] != j:
                ans.append(j)
                ans.append(hashmap[miss])
                break
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum(nums = [2,7,11,15], target = 9))
    print(sol.twoSum(nums = [3,2,4], target = 6))
    print(sol.twoSum(nums = [3,3], target = 6))
