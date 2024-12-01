def mutlak(x):
    return x if x >= 0 else -x

n = int(input())
x = int(input())
a = list(map(int, input("").split()))

ada = False

minn, makss, sama = a[0], a[0], 0
for i in range(n):
    if x == a[i]:
        ada = True
        sama = a[i]
    elif mutlak(x - a[i]) > mutlak(x - makss):
        makss = a[i]
    elif mutlak(x - a[i]) < mutlak(x - minn):
        minn = a[i]

print("TIDAK ADA" if not ada else sama)
print(minn)
print(makss)
