class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in {'(','[','{'}:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                if stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                else:
                    return False
            
        if stack:
            return False
        else:
            return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(s = "["))
    print(sol.isValid(s = "]"))
    print(sol.isValid(s = "()"))
    print(sol.isValid(s = "()[]{}"))
    print(sol.isValid(s = "(]"))
    print(sol.isValid(s = "()[]{}"))
    print(sol.isValid(s = "()[]{}"))

