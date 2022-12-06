with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

# print(data)
gamma = b''
epsilon = b''
for i in range(len(data[0])):
    column = []
    for x in data:
        column.append(int(x[i]))
    if sum(column) > len(column) / 2:
        gamma += b'1'
        epsilon += b'0'
    else:
        gamma += b'0'
        epsilon += b'1'

result = int(gamma, 2) * int(epsilon, 2)
print(result)
