from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dp = []
        cnt = 0

        # we want from nums=[1,1,0,1] create dp=[2,0,1]
        # sum all ones between zeros
        for i in range(len(nums)):
            n = nums[i]
            if n:
                cnt += 1
            else:
                if cnt != 0:
                    dp.append(cnt)
                    cnt = 0
                dp.append(n)

            if i == len(nums) - 1 and cnt != 0:
                dp.append(cnt)


        # corner case where we have all zeros either all
        if len(dp) == 1:
            return 0 if dp[0] == 0 else dp[0] - 1
        
        # slide with window of 3 because we always got dp as [1,0,5,0,1,0,5]
        # or [0, 5, 0]
        # and also we always have at least one zero to delete
        window = sum(dp[:3])    
        longLen = window

        for i in range(len(dp) - 3):
            window = window - dp[i] + dp[3+i]
            longLen = max(longLen, window)
            
        return longLen
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.longestSubarray(nums = [0,1,1,1,0,1,1,0,1]))
    print(sol.longestSubarray(nums = [1,1,0,1]))
    print(sol.longestSubarray(nums = [1,1,1]))
    print(sol.longestSubarray(nums = [1]))
    print(sol.longestSubarray(nums = [0,0]))
