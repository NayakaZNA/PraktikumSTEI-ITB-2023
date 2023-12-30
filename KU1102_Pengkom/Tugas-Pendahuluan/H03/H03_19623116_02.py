# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 10 Oktober 2023
# Deskripsi : Program menentukan bilangan terbesar ke-n dalam array

# KAMUS
# n             : integer
# panjang       : integer       ; panjang array
# values        : array[integer]
# maks          : integer       ; menyimpan maksimum sementara dari subarray
# idx_maks      : integer       ; menyimpan indeks `maks` pada array `values`

# ALGORITMA

## Input M dan N
panjang = int(input("Masukkan banyak data: "))
n       = int(input("Masukkan nilai N: "))

## Inisialisasi Awal
values    = [0 for i in range(panjang)]

## Input masukan arr
for i in range(1, panjang + 1):
    values[i-1]  = int(input(f"Masukkan data ke-{i}: "))

## Proses
### Mengurutkan array (dari yang terbesar) dengan selection sort
for j in range(panjang):
    #### Mencari indeks elemen terbesar dalam subarray
    idx_maks = j
    for k in range(j + 1, panjang):
        if values[k] > values[idx_maks]:
            idx_maks = k
    maks = values[idx_maks]
    
    #### Mendorong semua elemen subarray (j sampai maks)
    for l in range(idx_maks, j - 1, -1):
        values[l] = values[l-1]
    values[j] = maks

## Output
print(f"Nilai terbesar ke-{n} adalah {values[n - 1]}.")

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""