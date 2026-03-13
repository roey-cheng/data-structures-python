class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = head
            currnext = curr.next
            prev = None
            while curr:
                currnext = curr.next
                curr.next = prev
                prev = curr
                curr = currnext
            return prev
        else:
            return None



        