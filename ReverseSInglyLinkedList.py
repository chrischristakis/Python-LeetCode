from DataStructures.LinkedList import LinkedList


def reverse_linked_list(linked_list):
    prev = None
    curr = linked_list.head
    while curr is not None:
        next_node = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = next_node

    linked_list.head = prev


linked = LinkedList()
linked.append(0)
linked.append(1)
linked.append(3)
linked.append(5)
linked.append(8)
linked.append(11)

print(linked)

reverse_linked_list(linked)

print(linked)
