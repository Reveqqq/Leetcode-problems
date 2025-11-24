# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
from typing import List

# Solution 1
# Time complexity: O(m+n)
# Space complexity: O(m+n)
class Solution_1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        res = [0] * len(nums1)
        r = 0
        i = 0
        j = 0

        while i < m and j < n:
            d1 = nums1[i]
            d2 = nums2[j]
            if d1 <= d2:
                res[r] = d1
                i += 1
                r += 1
            else: 
                res[r] = d2
                j += 1
                r += 1

        while i < m:
            res[r] = nums1[i]
            i += 1
            r += 1

        while j < n:
            res[r] = nums2[j]
            j += 1
            r += 1

        for k in range(len(res)):
            nums1[k] = res[k]

# Solution 2 in-place
# Time complexity: O(m+n)
# Space complexity: O(1)
class Solution_2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1 
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1  
            k -= 1
        
        print(nums1)

# Solution 3 in-place with sort
# Time complexity: O(m+n)
# Space complexity: O(1)
class Solution_3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()


if __name__ == "__main__":
    sol = Solution_2()
    sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
    sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
    sol.merge(nums1 = [1,2,9,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    sol.merge(nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3)

