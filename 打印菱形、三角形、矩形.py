rows = int(input("请输入列数："))
# i控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
i, j, k = 1, 1, 1
# 等腰直角三角形1
# print("等腰直角三角形1：")
# while i <= rows:
#     while j <= rows-i+1:
#         print("*", end=" ")
#         j += 1
#         pass
#     print()
#     j = 1
#     i += 1
#     pass

# i = rows
# while i > 0:
#     while j <= rows-i+1:
#         print("*", end=" ")
#         j += 1
#         pass
#     print()
#     j = 1
#     i -= 1
#     pass

# print("等腰三角形：")
# while i <= rows:
#     while j <= rows-i+1:
#         print(" ", end=" ")
#         j += 1
#         pass
#     while k <= 2*i-1:
#         print("*", end=" ")
#         k += 1
#         pass
#     k = 1
#     j = 1
#     print()
#     i += 1
#     pass


# print("实心等边三角形：")
# while i <= rows:
#     j, k = 1, 1
#     while j <= rows-i:
#         print(" ", end=" ")
#         j += 1
#         pass
#     while k <= i:
#         print(" * ", end=" ")
#         k += 1
#         pass
#     print()
#     i += 1
#     pass

print("空心等边三角形：")
while i <= rows:
    j, k = 1, 1
    while j <= rows-i:
        print(" ", end="")
        j += 1
        pass
    while k <= 2*i:
        # print("*", end=" ")
        if k == 1 or k == 2*i-1 or i == rows:
            if i == rows:
                if k % 2 != 0:
                    print("*", end="")
                    pass
                else:
                    print(" ", end="")
                    pass
                pass
            else:
                print("*", end="")
                pass
        else:
            print(" ", end="")
        k += 1
        pass
    print()
    i += 1
    pass
