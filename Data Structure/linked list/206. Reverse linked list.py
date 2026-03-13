num_list = []
while head:
    num_list.append(head)
    head = head.next
num_list.reverse()
gummy = ListNode(0)
if num_list != []:
    gummy.next = num_list[0]
    a_head = gummy.next
    for i in range(1,len(num_list)):
        a_head.next = num_list[i]
        a_head = a_head.next
    a_head.next = None
    return gummy.next
else:
    return None