import re

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')
cmds = []
for row in data:
    a, b = re.split(r' ', row)
    cmds.append([a, int(b)])

horizontal = 0
depth = 0
for cmd in cmds:
    direction = cmd[0]
    move = cmd[1]
    if direction == 'forward':
        horizontal += move
    elif direction == 'down':
        depth += move
    elif direction == 'up':
        depth -= move
    else:
        pass

print(horizontal * depth)
