arr = [1, 0, 2, 0, 1, 0]
k = 0
temp = 0
arrlen = len(arr)

for i in range(arrlen):
    if arr[i] == 0:
        temp = arr[k]
        arr[k] = arr[i]
        arr[i] = temp
        k += 1

print(arr)

#optput = [0, 0, 0, 1, 1, 2]
