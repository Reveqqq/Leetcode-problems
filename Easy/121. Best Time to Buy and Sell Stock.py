from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        a = prices[0]

        for i in range(1, len(prices)):
            b = prices[i]

            if b < a:
                a = b
            else:
                max_profit = max(max_profit, b - a)

        return max_profit
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(prices = [7,1,5,3,6,4]))
    print(sol.maxProfit(prices = [7,6,4,3,1]))