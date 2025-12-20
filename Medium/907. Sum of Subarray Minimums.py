from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1] if stack else -1
            res[i] = res[j] + (i - j) * arr[i]

            stack.append(i)
        
        return sum(res) % (10**9 + 7)


if __name__ == "__main__":
    sol = Solution()

    print(sol.sumSubarrayMins(arr = [3,1,2,4]))
    print(sol.sumSubarrayMins(arr = [11,81,94,43,3]))
    
    