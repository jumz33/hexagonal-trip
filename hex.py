# f - move forward
# l - rotate left
# r - rotate right
# example: fflffrrf
command_sequence = input('? ')

# x, y
helicopter_pos = [0, 0]
truck_pos = [0, 0]
# rotation
# range from 0 to 5 
helicopter_rt = 0
truck_rt = 0

# 1st face = [-1, 1], 2nd face = [-1, 0] and etc.
faces = [
    [-1, 1], [-1, 0], [0, -1],
    [1, -1], [1, 0], [0, 1]
]

# helicopter
for command in command_sequence:
    # rotate left
    if command == 'l':
        helicopter_rt -= 1
        if helicopter_rt < 0:
            helicopter_rt += 6
    # rotate right
    if command == 'r':
        helicopter_rt += 1
        if helicopter_rt == 6:
            helicopter_rt -= 6
    # move forward
    if command == 'f':
        for axis in range(2):
            helicopter_pos[axis] += faces[helicopter_rt][axis]
print(f'Helicopter position: {helicopter_pos}')

# truck
print('> ', end='')
while truck_pos != helicopter_pos:
    # POSITION
    truck_pos_before = truck_pos[0], truck_pos[1]
    # x axis
    if truck_pos[0] != helicopter_pos[0]:
        x1 = truck_pos[0] + 1
        x2 = truck_pos[0] - 1
        if helicopter_pos[0] > 0:
            if helicopter_pos[0] + x1 > helicopter_pos[0] + x2:
                truck_pos[0] += 1
            else:
                truck_pos[0] -= 1
        if helicopter_pos[0] < 0:
            if helicopter_pos[0] + x1 < helicopter_pos[0] + x2:
                truck_pos[0] += 1
            else:
                truck_pos[0] -= 1
    # y axis
    if truck_pos[1] != helicopter_pos[1]:
        y1 = truck_pos[1] + 1
        y2 = truck_pos[1] - 1
        if helicopter_pos[1] > 0:
            if helicopter_pos[1] + y1 > helicopter_pos[1] + y2:
                truck_pos[1] += 1
            else:
                truck_pos[1] -= 1
        if helicopter_pos[1] < 0:
            if helicopter_pos[1] + y1 < helicopter_pos[1] + y2:
                truck_pos[1] += 1
            else:
                truck_pos[1] -= 1
    # cannot change x and y at the same time
    if truck_pos[1] - truck_pos_before[1] == truck_pos[0] - truck_pos_before[0]:
        # change only x
        try:
            truck_rt_now_1 = truck_rt - faces.index([truck_pos[0], truck_pos_before[1]])
            if truck_rt_now_1 < 0:
                truck_rt_now_1 += 6
            #
            if truck_rt_now_1 == 4:
                truck_rt_now_1 = 2
            if truck_rt_now_1 == 5:
                truck_rt_now_1 = 1
        except ValueError:
            truck_rt_now_1 = 6
        # change only y
        try:
            truck_rt_now_2 = truck_rt - faces.index([truck_pos_before[0], truck_pos[1]])
            if truck_rt_now_2 < 0:
                truck_rt_now_2 += 6
            #
            if truck_rt_now_2 == 4:
                truck_rt_now_2 = 2
            if truck_rt_now_2 == 5:
                truck_rt_now_2 = 1
        except ValueError:
            truck_rt_now_2 = 6
        # make a choice
        if truck_rt_now_1 > truck_rt_now_2:
            truck_pos[0] = truck_pos_before[0]
        else:
            truck_pos[1] = truck_pos_before[1]
    # ROTATION
    truck_pos_changes = [0, 0]
    for i in range(2):
        truck_pos_changes[i] = truck_pos[i] - truck_pos_before[i]
    truck_rt -= faces.index(truck_pos_changes)
    if truck_rt < 0:
        truck_rt += 6
    while truck_rt != 0:
        if truck_rt <= 3:
            truck_rt -= 1
            print('l', end='')
        if 3 < truck_rt:
            truck_rt += 1
            if truck_rt == 6:
                truck_rt = 0
            print('r', end='')
    print('f', end='')
    truck_rt += faces.index(truck_pos_changes)
    if truck_rt > 5:
        truck_rt -= 6
print('.')

