# sum = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if(i != j) and (i != k) and (j != k):
#                 print(i, j, k)
#                 sum += 1
# print(sum)

# 创建一个迭代器
# class MyNumber:
#     def __iter__(self):
#         """
#         返回一个特殊的迭代对象
#         :return:
#         """
#         self.a = 1
#         return self
#     def __next__(self):
#         """
#         返回下一个迭代器对象
#         :return:
#         """
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#         pass
#     pass
# myclass = MyNumber()
# myiter = iter(myclass)
# for i in myiter:
#     print(i)

# 生成器
import sys
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a+b
        counter += 1
        pass
    pass
f = fibonacci(10)
while True:
    try:
        print(next(f), end=" ")
        pass
    except StopIteration:
        sys.exit()
        pass
    pass
