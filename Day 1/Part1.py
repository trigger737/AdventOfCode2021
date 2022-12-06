with open('input.txt', 'r') as file:
    data = file.read().split()
    data = list(map(int, data))

# print(data)
last_value = 0
counter = 0
for number in data:
    if number > last_value:
        counter += 1
    last_value = number
print(counter - 1)
