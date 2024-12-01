# FUNGSI mini(a, b)
def mini(arr: list[int], length: int) -> int:
    kecil = arr[0]
    for i in range(1, length):
        kecil = arr[i] if arr[i] < kecil else kecil
    return kecil

# INPUT
n = int(input())
a = list(map(int, input().strip().split()))

# PROSES
# Mengisi dictionary of frequency
freq = {}
for i in range(n):
    freq[a[i]] = 0

# Menambah dictionary of frequency berdasarkan kemunculan elemen
for i in range(n):
    freq[a[i]] += 1

# Mencari frekuensi terbesar
k = a[0]
for i in freq:
    if freq[i] > freq[k]:
        k = i

# MEncari nilai terkecil jika elemen dengan frekuensi terbesar ada lebih dari satu
soln = []
for i in freq:
    if freq[i] == freq[k]:
        soln.append(i)

# OUTPUT
print(mini(soln, len(soln)))
