def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
max = int(input("input max num:"))
fibs = []
for n in fib(max):
    fibs.append(n)
print(fibs)