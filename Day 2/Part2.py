import re

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')
cmds = []
for row in data:
    a, b = re.split(r' ', row)
    cmds.append([a, int(b)])

horizontal = 0
depth = 0
aim = 0
for cmd in cmds:
    direction = cmd[0]
    move = cmd[1]
    if direction == 'forward':
        horizontal += move
        depth += aim * move
    elif direction == 'down':
        aim += move
    elif direction == 'up':
        aim -= move
    else:
        pass

print(horizontal * depth)
