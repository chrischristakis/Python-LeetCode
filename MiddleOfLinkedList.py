class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head) -> ListNode:
    slow = head
    fast = head.next

    while fast:
        slow = slow.next
        fast = fast.next.next if fast.next else None

    return slow


# initialize list
start = ListNode()
inp = [1, 2, 3, 4, 5, 6, 7]
c = start
for e in inp:
    c.next = ListNode(e)
    c = c.next
# ---------------

print(middle_node(start.next).val)
