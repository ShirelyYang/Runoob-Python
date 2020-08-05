import sys
print("命令行参数如下：")
for i in sys.argv:
    print(i)
    pass
print("python 路径为：")
for num in range(len(sys.path)):
    print(sys.path[num], end=";")
    if num % 2 == 0:
        print("\n")
        pass