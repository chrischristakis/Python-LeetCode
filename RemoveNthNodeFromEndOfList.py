def removeNthFromEnd(head, n):

    if not head.next:
        return

    left = head
    right = head

    # Make right n spaces away from left, acts like a stopper.
    for i in range(0, n):
        right = right.next

    # In the case where right exceeds the list, we are trying to
    # remove the head, so we can terminate early here
    if not right:
        return head.next

    # Now, parse list until right.next goes out of bounds. This
    # makes left point to the node to the immediate left of the removed node
    while right.next:
        left = left.next
        right = right.next

    left.next = left.next.next

    return head