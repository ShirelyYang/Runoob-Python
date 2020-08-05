year = int(input("请输入年份：\n"))
month = int(input("请输入月份：\n"))
date = int(input("请输入日期：\n"))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
K = ["Y", "y", "N", "n"]

while True:
    while True:
        if month in range(1, 13):
            sum = months[month-1]
            break
        else:
            print("data error!")
            month = int(input("请输入月份：\n"))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if month > 2:
            sum += 1
        sum += date
        print("这一天是这一年的第", sum, "天")
    else:
        sum += date
        print("这一天是这一年的第", sum, "天")
    print("是否继续计算？Y 继续，N 结束。")
    k = input("")
    if k not in K:
        print("您输入有误，请重新输入！")
        k = input("")
    elif k in K[:2]:
        year = int(input("请输入年份：\n"))
        month = int(input("请输入月份：\n"))
        date = int(input("请输入日期：\n"))
    else:
        break
print("感谢使用，程序结束！")