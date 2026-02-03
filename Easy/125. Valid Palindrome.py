class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l].isalnum() and s[r].isalnum() and s[l] == s[r]:
                l += 1
                r -= 1
                continue
                
            elif s[l].isalnum() and s[r].isalnum() and s[l] != s[r]:
                return False
            
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1

        return True


if __name__ == "__main__":
    sol = Solution()

    print(sol.isPalindrome(s = "A man, a plan, a canal: Panama"))
