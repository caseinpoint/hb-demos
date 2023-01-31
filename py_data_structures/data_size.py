from sys import getsizeof

data = []
print(f'initial size: {getsizeof(data)} bytes')

for i in range(16):
    data.append(i)
    print(f'size i: {getsizeof(i)}b, len: {len(data)}, size: {getsizeof(data)}b')

print()
data = []

for i in range(16):
    j = str(i) + '0'
    data.append(j)
    print(f'size j: {getsizeof(j)}b, len: {len(data)}, size: {getsizeof(data)}b')

# data = {}
# print(f'initial size: {getsizeof(data)} bytes')

# for i in range(16):
#     data[i] = i
#     print(f'size i: {getsizeof(i)}b, len: {len(data)}, size: {getsizeof(data)}b')