import heapq


def last_stone_weight(stones):
    # To make max heap, we multiple all values by -1
    stones = [stone * -1 for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        biggest = heapq.heappop(stones) * -1
        second_biggest = heapq.heappop(stones) * -1
        if biggest == second_biggest:
            continue

        heapq.heappush(stones, (biggest - second_biggest) * -1)

    return stones[0] * -1 if len(stones) == 1 else 0


print(last_stone_weight([2,7,4,1,8,1]))  # 1
print(last_stone_weight([1]))  # 1
