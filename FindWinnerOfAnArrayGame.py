from collections import deque


def get_winner(arr, k):
    if len(arr) <= 1:
        return arr

    highest_num = 0
    win_count = {}
    for i in arr:
        highest_num = max(highest_num, i)
        win_count[i] = 0

    linked = deque(arr)
    head = linked.popleft()
    while win_count[head] < k and head != highest_num:
        next = linked.popleft()
        if head > next:
            linked.append(next)
        else:
            linked.append(head)
            head = next
        win_count[head] += 1
    return head


def get_winner2(arr, k):
    highest_num = max(arr)
    win_count = 0
    winner = arr[0]
    for num in arr[1::]:
        if win_count >= k or winner == highest_num:
            break
        if winner > num:
            win_count += 1
        else:
            win_count = 1
            winner = num
    return winner


print(get_winner2([2,1,3,5,4,6,7], 2))
print(get_winner2([1,11,22,33,44,55,66,77,88,99], 1000000000))
