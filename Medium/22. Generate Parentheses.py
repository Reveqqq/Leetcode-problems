from typing import List

class Solution:
    def __init__(self):
        self.brackets = []

    def _find_brackets(self, cur_s: str, open_rem: int, clsd_rem: int):
        if open_rem  == 0 and clsd_rem == 0:
            self.brackets.append(cur_s)

        if open_rem > 0:
            self._find_brackets(cur_s + "(", open_rem - 1, clsd_rem)
        
        if clsd_rem > 0 and (clsd_rem - 1 >= open_rem or open_rem == 0):
            self._find_brackets(cur_s + ")", open_rem, clsd_rem - 1)
        
        return


    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return self.brackets
        
        self._find_brackets("(", n - 1, n)
        
        return self.brackets
    

if __name__ == "__main__":
    sol = Solution()

    print(sol.generateParenthesis(4))
