class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        curr = self.next
        res = [str(self.val)]
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return ' -> '.join(res)


def reorder_list(head):
    if not head.next:
        return

    # store nodes in a stack for easy back-to-front access
    stack = []
    front = head
    while front:
        stack.append(front)
        front = front.next

    front = head
    # While our front has a next, and also our front's next node is not equal to the back of the stack (finished)
    while front.next and front.next != stack[-1]:
        temp = front.next
        back = stack.pop()
        stack[-1].next = None  # Back of the stack now points to None instead of the newly arranged element.
        front.next = back
        back.next = temp
        front = temp


def reorder_list2(head):
    if not head.next:
        return

    # Find middle element of list
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split second half of list from the middle 1 -> 2 -> 3 -> 4 -> 5 -> 6 : 1 -> 2 -> 3   4 -> 5 -> 6
    front_first_half = head
    front_second_half = slow.next
    slow.next = None  # this decouples them

    # Reverse second half of list
    curr = front_second_half
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    front_second_half = prev

    # Now, while we have something in the second half to insert, insert that in between the first half elements
    while front_second_half:
        first_half_temp = front_first_half.next
        front_first_half.next = front_second_half
        second_half_temp = front_second_half.next
        front_second_half.next = first_half_temp

        front_second_half = second_half_temp
        front_first_half = first_half_temp


# initialize list
start = ListNode()
inp = [1,2,3,4]
c = start
for e in inp:
    c.next = ListNode(e)
    c = c.next
# ---------------

func = reorder_list2
print(start.next)
func(start.next)
print(start.next)
