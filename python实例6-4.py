lis = []
a = 1
lis.append(a)
b = 1
lis.append(b)
for i in range(1, 20):
    c = lis[i-1] + lis[i]
    lis.append(c)
