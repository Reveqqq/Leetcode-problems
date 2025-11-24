# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
# You must also not convert the inputs to integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0

        while i >= 0 or j >= 0 or carry > 0:
            digit1= int(num1[i] if i >= 0 else 0)
            digit2= int(num2[j] if j >= 0 else 0)

            digitSum = digit1 + digit2 + carry

            carry = digitSum // 10
            digitSum %= 10

            res.append(str(digitSum))

            i -= 1
            j -= 1

        while len(res) > 1 and res[-1] == '0':
            res.pop()

        return ''.join(res[::-1])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.addStrings("11", "123"))
    print(sol.addStrings("456", "77"))
    print(sol.addStrings("0", "0"))
    print(sol.addStrings("1", "99999999999999999999999999999999999999999999999999999"))

