def has_cycle(head):
    unique_nodes = set()
    curr = head
    while curr:
        if curr in unique_nodes:
            return True
        unique_nodes.add(curr)
        curr = curr.next
    return False


def has_cycle2(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow and fast:
        if fast == slow:
            return True
        slow = slow.next
        fast = fast.next.next if fast.next else None
    return False
