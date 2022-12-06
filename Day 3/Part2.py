import re
with open('input1.txt', 'r') as file:
    data = file.read().strip().split('\n')

print(data)
# gamma = b''
# epsilon = b''

o2_nums = []
co2_nums = []
columns = []
for i in range(len(data[0])):
    column = []
    for x in data:
        column.append(x[i])

    if column.count('0') <= column.count('1'):
        o2_nums.append('1')
        co2_nums.append('0')
    else:
        o2_nums.append('0')
        co2_nums.append('1')
    columns.append(''.join(column))
o2_nums = ''.join(o2_nums)
co2_nums = ''.join(co2_nums)
print(o2_nums,co2_nums)


print()


# for i,k in enumerate(o2_nums):
#     for j,l in enumerate(data):
#         # print(i,k,j,l)
#
#         if l[i] != k:
#             # data.pop(j)
#             data.remove(l)
#             print(data)









