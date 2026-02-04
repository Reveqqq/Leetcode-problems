from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return nums
        
        prefix_freq = defaultdict()
        prefix = 0
        cnt = 0

        for i in range(len(nums)):
            prefix += nums[i]
            if prefix == k:
                cnt += 1

            miss = prefix - k
            if miss in prefix_freq:
                cnt += prefix_freq[miss] 

            if prefix in prefix_freq:
                prefix_freq[prefix] += 1
            else:
                prefix_freq[prefix] = 1
        
        return cnt



if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum(nums=[-1,-1,1], k=0))
    print(sol.subarraySum(nums=[1,2], k=2))
    print(sol.subarraySum(nums=[0,2], k=2))
    print(sol.subarraySum(nums=[1], k=0))
    print(sol.subarraySum(nums=[1,1,1], k=2))
    print(sol.subarraySum(nums=[1,2,3], k=3))
    print(sol.subarraySum(nums=[3,4,7,-2,2,1,4,2], k=7))
    