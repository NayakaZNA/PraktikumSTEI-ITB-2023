# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 2 November 2023
# Deskripsi : Program membuat matriks baru yang tiap elemennya merupakan jumlah elemen adjacent pada matriks semula
# Panjang   : 14 lines

# KAMUS
# m, n      : int       ; dimensi matriks
# matriks1  : arr[int]  ; matriks lama
# matriks2  : arr[int]  ; matriks baru

# ALGORITMA
## Input m dan n
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

## Inisiasi matriks
matriks1 = [[0 for j in range(n+2)] for i in range(m+2)]
matriks2 = [[0 for j in range(n)] for i in range(m)]

## Input elemen matriks
for i in range(m):
    for j in range(n):
        matriks1[i+1][j+1] = int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))

## Proses
for i in range(m):
    for j in range(n):
        matriks2[i][j] = matriks1[i+1][j] + matriks1[i+1][j+2] + matriks1[i][j+1] + matriks1[i+2][j+1]

## Output
        if j == n - 1:
            print(matriks2[i][j])
        else: # 0 <= j < n - 1
            print(matriks2[i][j], end=" ")

"""
Penjelasan:
Ambil contoh test case 1. Agar kode tidak terlalu panjang karena pembagian kasus yang banyak, 
kita atur sehingga `matriks1` yang seharusnya berbentuk
2 3 4
2 2 3
2 9 7

menjadi

0 0 0 0 0
0 2 3 4 0
0 2 2 3 0
0 2 9 7 0
0 0 0 0 0

Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""
