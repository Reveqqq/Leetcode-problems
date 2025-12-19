from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _listNode2Num(self, l: Optional[ListNode]) -> int:
        num = 0
        l_tmp = l
        i = 1

        while l_tmp is not None:
            num += l_tmp.val * i
            l_tmp = l_tmp.next
            i *= 10

        return num

    def _num2ListNode(self, num: int) -> Optional[ListNode]:
        l = ListNode(num % 10)
        num //= 10
        l_tmp = l

        while num != 0:
            l_tmp.next = ListNode(num % 10)
            l_tmp = l_tmp.next
            num //= 10

        return l

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 == None and l2 == None: 
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
    
        num1 = self._listNode2Num(l1)
        num2 = self._listNode2Num(l2)
        ans = num1 + num2 

        ans_l = self._num2ListNode(ans)

        return ans_l
        


if __name__ == "__main__":
    sol = Solution()
    l1 = sol._num2ListNode(342)
    l2 = sol._num2ListNode(465)
    print(sol.addTwoNumbers(l1, l2))
    