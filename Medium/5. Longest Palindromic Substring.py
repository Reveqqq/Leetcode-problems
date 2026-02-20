class Solution:
    def longestPalindrome(self, s: str) -> str:
        # main idea is transform s from 'bb' to '@#b#b#$
        # 1 char is palindrome
        # if we add 2 equals chars from left and right it's also will be a palindrome
        # without tranform we need to check odd and even cases
        # with transofrm we easily can check just odd cases
        # for example in 'bb' we will check 'b#b' - is palindrome
        # and in ans we just remove # symbols
        sTransformded = '@#'
        for char in s:
            sTransformded += char + '#'
        sTransformded += '#$'


        ans = s[0]
        maxLen = 1
        
        for i in range(1, len(sTransformded)-1):
            curLen = 1
            l = i - 1
            r = i + 1
            while sTransformded[l] != '@' and sTransformded[r] != '$':
                if sTransformded[l] == sTransformded[r]:
                    curLen += 1
                    l -= 1
                    r += 1
                else:
                    break
            
            if curLen > maxLen:
                maxLen = curLen
                ans = sTransformded[l+1:r-1]
        
        return ans.replace('#','')

if __name__ == "__main__":
    sol = Solution()

    print(sol.longestPalindrome(s = "babad"))
    print(sol.longestPalindrome(s = "cbbd"))
    print(sol.longestPalindrome(s = "bb"))
    