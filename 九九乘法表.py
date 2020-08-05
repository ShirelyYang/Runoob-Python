i, j = 1, 1
while i <= 9:
    while j <= 9-i+1:
        print("%d*%d=%d" % (i, j, i*j), end="")
        j += 1
        pass
    print()
    j = 1
    i += 1
    pass