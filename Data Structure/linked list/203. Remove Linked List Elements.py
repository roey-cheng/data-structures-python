from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(1474743) #这里就是瞎造一个dummy node,里面的数字是啥都无所谓
        dummy.next = head #连接dummy和真正的head,有dummy 的好处就是即使head在动，只要dummy还在，就能找到整个linklist
        prev = dummy # 对于initial head 来说， 它的prev就是dummy
        while head:
            if head.val == val:
                prev.next = head.next #这里就是删中间一条的意思，让prev跳过一条走
            else:
                prev = head #正常让prev往下走
            head = head.next
        return dummy.next
