from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        l = 0
        for r in range(len(t)):
            if s[l] == t[r]:
                l += 1
            if l == len(s):
                return True
            
        return False

    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.isSubsequence(s = "abc", t = "ahbgdc"))
    # print(sol.isSubsequence(s = "axc", t = "ahbgdc"))
    print(sol.isSubsequence(s = "axc", t = "axc"))