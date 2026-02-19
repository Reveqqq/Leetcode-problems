from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_miss = defaultdict()
        prefix_miss[0] = 1

        prefix = 0
        cnt = 0

        for n in nums:
            prefix += n
            miss = prefix % k

            if miss in prefix_miss:
                cnt += prefix_miss[miss]
            
            if miss in prefix_miss:
                prefix_miss[miss] += 1
            else:
                prefix_miss[miss] = 1
        
        return cnt
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))