a = [int(i) for i in input("请输入：").split()]
m = len(a)
while m != 1:
    for i in range(m-1):
        if a[i] > a[i+1]:
            x = a[i]
            a[i] = a[i+1]
            a[i+1] = x
    m -= 1
print(a)