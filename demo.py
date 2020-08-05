people = {}
for x in range(1, 31):
    people[x] = 1
    pass
print(people)
i = 1
j = 0
check = 0
while i <= 31:
    if i == 31:
        i = 1
        pass
    elif j == 15:
        break
        pass
    else:
        if people[i] == 0:
            i += 1
            continue
            pass
        else:
            check += 1
            if check == 9:
                people[i] = 0
                check = 0
                print("%d 下船了" % i)
                j += 1
                pass
            else:
                i += 1
                pass
            pass
        pass
    pass
