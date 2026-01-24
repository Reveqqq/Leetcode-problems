from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        prev = ListNode(head.val)
        cur = head.next

        while True:
            next = cur.next
            cur.next = prev
            prev = cur
            if next is None:
                break
            cur = next

        return cur
        

def print_list(head: Optional[ListNode]) -> None:
    while n_head is not None:
        print(n_head.val)
        n_head = n_head.next
        
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    tmp = head

    for i in range(1,5):
        tmp.next = ListNode(i + 1)
        tmp = tmp.next

    h = sol.reverseList(head)
    while h is not None:
        print(h.val)
        h = h.next
    
    