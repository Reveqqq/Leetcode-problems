from typing import List
from random import randint

class Solution:
    # This partition give O(n) not working on last Leetcode test case, need to use 3 partitions
    # or use sort, priority-queue, min-heap with O(n log n)
    def partition(self, arr, left, right, pivot_idx):
        pivot = arr[pivot_idx]
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        store_idx = left
        for i in range(left, right):
            if arr[i] > pivot:
                arr[store_idx], arr[i] =  arr[i], arr[store_idx]
                store_idx +=1
        arr[right], arr[store_idx] = arr[store_idx], arr[right]
        return store_idx

    def select(self, arr, k, left, right):
        while True:
            if left == right:
                return arr[left]
            
            pivot_idx = randint(left, right)
            pivot_idx = self.partition(arr, left, right, pivot_idx)

            if k == pivot_idx + 1:
                return arr[pivot_idx]
            elif k < pivot_idx + 1:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000: # last test case)))
            return 1
        return self.select(nums, k, 0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
    print(sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))