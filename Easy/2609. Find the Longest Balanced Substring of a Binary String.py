class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        result = ones = zeros = 0

        for char in s:
            if char == '0':
                if ones > 0:
                    zeros = ones = 0
                zeros += 1
            else:
                ones += 1
            result = max(result, min(zeros, ones) * 2)
            
        return result




if __name__ == "__main__":
    sol = Solution()
    # "01000111"
    # "00111"
    # "111"
    # "10"
    # "010"
    # "100000000"
    print(sol.findTheLongestBalancedSubstring(s = "10"))
