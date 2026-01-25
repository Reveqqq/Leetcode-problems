class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                content = ''
                number = ''

                while stack[-1] != '[':
                    content = stack.pop() + content
                stack.pop()

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number

                stack.append(int(number) * content)

        return ''.join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString(s = "3[a]2[bc]"))
    print(sol.decodeString(s = "3[a2[c]]"))
    print(sol.decodeString(s = "abc3[cd]xyz"))
    print(sol.decodeString(s = "10[l]"))
