class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return str(self.val)
        return str(self.val) + " -> " + str(self.next)


def merge_lists(list1, list2):
    head = curr = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    if list1:
        curr.next = list1
    if list2:
        curr.next = list2

    return head.next


list_1 = ListNode(1)
ListNode2 = ListNode(2)
ListNode3 = ListNode(4)
list_1.next = ListNode2
ListNode2.next = ListNode3

list_2 = ListNode(1)
ListNode4 = ListNode(3)
ListNode5 = ListNode(4)
list_2.next = ListNode4
ListNode4.next = ListNode5

print(merge_lists(list_1, list_2))  # 1 -> 1 -> 2 -> 3 -> 4 -> 4
