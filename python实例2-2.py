i = int(input("Please enter profit:"))
i /= 10000
obj = {100: 0.01, 60: 0.015, 40: 0.03, 20: 0.05, 10: 0.075, 0: 0.1}
keys = list(obj.keys())
keys.sort()
keys.reverse()
r = 0

for key in keys:
    if i > key:
        r += (i - key) * obj.get(key)
        i = key
print(int(r * 10000))