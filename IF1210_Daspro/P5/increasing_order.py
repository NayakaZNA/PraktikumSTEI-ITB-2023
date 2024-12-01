# FUNGSI geser(arr, n)
def geser(arr, n):
    temp = arr[n-1]
    for i in range(n-1, -1, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

# FUNGSI menaik(arr, n)
def menaik(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

# INPUT
n = int(input())
a = list(map(int, input().strip().split()))

# PROSES
naik = False
count = 0
for i in range(n):
    if menaik(a, n):
        naik = True
        break
    else:
        a = geser(a, n)
        count += 1

print(count if naik else "Tidak") 