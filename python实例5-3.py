a = [1, 3, 5, 2, 4, 5, 7]
n = len(a)
for i in range(n):
    for j in range(i, n):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
print(a)