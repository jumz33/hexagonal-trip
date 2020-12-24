'''
    "Hexagonal trip"
    Author: Zakhar "Jummiuzz33"
'''

# f - move forward
# l - rotate left
# r - rotate right
commands = input('What to do?\n> ')

# [x, y, z]
helicopter_pos = [0, 0, 0]
truck_pos = [0, 0, 0]
# rotation
# 0 - 5 by faces
helicopter_rt = 0
truck_rt = 0

# helicopter
for i in commands:
    # rotate left
    if i == 'l':
        helicopter_rt -= 1
        if helicopter_rt < 0:
            helicopter_rt += 6
    # rotate right
    if i == 'r':
        helicopter_rt += 1
        if helicopter_rt == 6:
            helicopter_rt -= 6
    # move forward
    if i == 'f':
        def change_pos(x, y, z):
            helicopter_pos[0] += x
            helicopter_pos[1] += y
            helicopter_pos[2] += z
        if helicopter_rt == 0:
            change_pos(-1, 1, 0)
        if helicopter_rt == 1:
            change_pos(-1, 0, -1)
        if helicopter_rt == 2:
            change_pos(0, -1, -1)
        if helicopter_rt == 3:
            change_pos(1, -1, 0)
        if helicopter_rt == 4:
            change_pos(1, 0, 1)
        if helicopter_rt == 5:
            change_pos(0, 1, 1)
print(f'Helicopter position: {helicopter_pos}')

# truck
while truck_pos != helicopter_pos:
    # change position
    pos_before = truck_pos[0], truck_pos[1], truck_pos[2]
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
    # can't do x +- 1 and y +- 1 at the same time
    if truck_pos[1] - pos_before[1] == truck_pos[0] - pos_before[0]:
        truck_pos[1] = pos_before[1]
    # z axis
    # z = x + y
    truck_pos[2] = truck_pos[0] + truck_pos[1]

    print(f'go to -> {truck_pos}')

