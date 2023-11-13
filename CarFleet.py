def car_fleet(target, position, speed):
    # Combine both position and speed into a list of tuples
    pos_and_speed = list(map(lambda pos, sp: (pos, sp), position, speed))

    # sort it based off position
    pos_and_speed.sort(key=lambda tupl: tupl[0], reverse=True)

    stack = []
    for pos, sp in pos_and_speed:
        time = (target - pos) / float(sp)
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)


print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(car_fleet(10, [0, 4, 2], [2,1,3]))
