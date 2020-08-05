# 3X4的矩阵列表
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 方法一
# list1 = [[row[i] for row in matrix] for i in range(4)]
# print(list1)

# 方法二
# list2 = []
# for i in range(4):
#     list2.append([row[i] for row in matrix])
#     pass
# print(list2)

# 方法三
list3 = []
for i in range(4):
    list_row = []
    for row in matrix:
        list_row.append(row[i])
        pass
    list3.append(list_row)
    pass
print(list3)