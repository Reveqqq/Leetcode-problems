from typing import List
from collections import Counter
from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        ans = []
        frequents = Counter(nums)
        priority_queue = PriorityQueue()

        for num, freq in frequents.items():
            priority_queue.put(((-1)*freq, num))
        
        for _ in range(k):
            _, n = priority_queue.get()
            ans.append(n)

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent(nums = [1,1,1,2,2,4], k = 2))
    print(sol.topKFrequent(nums = [1], k = 1))
    print(sol.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))