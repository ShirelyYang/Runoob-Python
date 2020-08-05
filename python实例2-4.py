a = [100, 60, 40, 20, 10, 0]
b = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
def f(x):
    for i in range(len(a)):
        if n > a[i]:
            c = (a[j] - a[j+1] for j in range(i, len(a)-1))
            break
    r = sum(map(lambda x, y: x*y, b[i:], ([n-a[i]]+list(c))))
    yield int(r*10000)

k = 1
while k:
    n = int(input("请输入净利润，单位为（万元）：\n"))
    print("应发奖金为：", next(f(n)), "元")
    k = int(input("是否继续计算奖金？是：1，否：0\n"))
    if k not in range(2):
        print("输入有误，请重新输入！")
        k = int(input("是否继续计算奖金？是：1，否：0\n"))
print("感谢使用，程序结束！")