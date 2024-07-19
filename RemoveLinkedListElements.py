def removeElements(head, val):
    dummy = ListNode(0, head)
    curr = head
    prev = dummy
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next