class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        l = 0
        for r in range(len(s)):
            char = s[r]

            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                max_len = max(max_len, r - l + 1)
            seen[char] = r

        return max_len




if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s = "abcabcbb"))
