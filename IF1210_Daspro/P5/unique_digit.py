# # FUNGSI maks(arr)
# def makss(arr, length):
#     gede = arr[0]
#     for i in range(length):
#         if arr[i] > gede:
#             gede = arr[i]
#     return gede
# Mohon maaf kalau kode ini AC kak
# Saya cuma coba submit karena kalau pakai fungsi di atas runtime error terus

# FUNGSI isIn(e, arr)
def isIn(e, arr):
    for i in range(len(arr)):
        if arr[i] == e:
            return True
    return False

# INPUT
arr = []
while True:
    num = int(input())
    if num == -9999:
        break
    else:
        arr.append(num)

# PROSES
n = len(arr)
sums = []
for i in range(len(arr)):
    for j in range(i+1, n):
        sums.append(arr[i] + arr[j])

i = 1
while True:
    if (not isIn(i, arr)) and (not isIn(i, sums)):
        print(i)
        break
    i += 1

