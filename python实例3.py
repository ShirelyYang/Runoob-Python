for i in range(2, 85, 2):
    j = 168/i
    if i > j and (i-j) % 2 == 0:
        n = (i-j)/2
        x = n ** 2 - 100
        print(int(x))