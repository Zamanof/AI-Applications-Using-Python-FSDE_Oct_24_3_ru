arr = [2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
       19, 20, 21, 22, 23, 24]

sliced_arr = arr[:5]

print(sliced_arr)

for item in range(len(sliced_arr)):
    sliced_arr[item] = 15

print(sliced_arr)
print(arr)

