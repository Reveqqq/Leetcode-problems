from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next

        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next

        return dummy.next



        
if __name__ == "__main__":
    sol = Solution()

    head = ListNode(1)
    tmp = head

    for i in range(1,5):
        tmp.next = ListNode(i + 1)
        tmp = tmp.next

    h = sol.reverseBetween(head,2,4)

    head = ListNode(3)
    head.next = ListNode(5)

    h = sol.reverseBetween(head, 1, 2)
