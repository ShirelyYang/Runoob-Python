x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
a = {"x": x, "y": y, "z": z}
for w in sorted(a, key=a.get):
    print(w, a[w])