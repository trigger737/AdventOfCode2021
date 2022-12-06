with open('input.txt', 'r') as file:
    data = file.read().split()
    data = list(map(int, data))

# print(data)
last_value = 0
value = 0
counter = 0
buff = []
for number in data:
    buff.append(number)
    if len(buff) >= 3:
        value = sum(buff)
        buff.pop(0)
    if value > last_value:
        counter += 1
    last_value = value

print(counter - 1)
