# The array-form of an integer num is an array representing its digits in left to right order.

# For example, for num = 1321, the array form is [1,3,2,1].

# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1

        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
            
            last_digit = k % 10
            res.append(last_digit)
            k = k // 10

            i -= 1
        
        res.reverse()

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.addToArrayForm(num = [1,2,0,0], k = 34))
    print(sol.addToArrayForm(num = [2,7,4], k = 181))
    print(sol.addToArrayForm(num = [2,1,5], k = 806))
