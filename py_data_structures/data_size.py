from sys import getsizeof

data = []
print(f'initial size: {getsizeof(data)} bytes')

for i in range(16):
    data.append(i)
    print(f'i size = {getsizeof(i)}b,  list len = {len(data)},  list size = {getsizeof(data)}b')

print()
data = []

for i in range(16):
    j = str(i) * i * 10
    data.append(j)
    print(f'j size = {getsizeof(j)}b,  list len = {len(data)},  list size = {getsizeof(data)}b')

# print()
# data = {}
# print(f'initial size: {getsizeof(data)} bytes')

# for i in range(16):
#     data[i] = i
#     print(f'i size = {getsizeof(i)}b,  dict len = {len(data)},  list size = {getsizeof(data)}b')