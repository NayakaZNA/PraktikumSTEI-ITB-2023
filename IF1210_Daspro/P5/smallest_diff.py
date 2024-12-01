# # FUNGSI mini(a, b)
# def mini(arr: list[int], length: int) -> int:
#     kecil = arr[0]
#     for i in range(1, length):
#         kecil = arr[i] if arr[i] < kecil else kecil
#     return kecil
# Mohon maaf kalau kode ini AC kak
# Saya cuma coba submit karena kalau pakai fungsi di atas untuk mencari nilai minimum dari array
# malah runtime error terus

# FUNGSI mutlak(x)
def mutlak(x):
    return (-x if x < 0 else x)

# INPUT
n = int(input())
a = list(map(int, input().split()))

# PROSES
diff = []
for i in range(n):
    for j in range(i+1, n):
        diff.append(mutlak(a[j] - a[i]))

# OUTPUT
print(min(diff))