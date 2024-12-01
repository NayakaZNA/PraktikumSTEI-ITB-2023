# Fungsi jumlahDijit(n)
def jumlahDijit(n):
    # Menghitung jumlah dari seluruh digit n
    jumlah = 0
    while n > 0:
        jumlah += n % 10
        n //= 10
    return jumlah


# Input
n = int(input())
a = list(map(int, input("").split()))

# Proses
count = 0
for i in range(n):
    while a[i] >= 10:
        a[i] = jumlahDijit(a[i])
        count += 1

# Output
print(count)