# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 2 November 2023
# Deskripsi : Program membuat matriks baru yang tiap elemennya merupakan jumlah elemen adjacent pada matriks semula

# KAMUS
# m, n      : int       ; dimensi matriks
# matriks1  : arr[int]  ; matriks lama
# matriks2  : arr[int]  ; matriks baru

# ALGORITMA
## Input m dan n
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

## Inisiasi matriks
matriks1 = [[0 for i in range(n)] for i in range(m)]
matriks2 = [[0 for i in range(n)] for i in range(m)]

## Input elemen matriks
for i in range(m):
    for j in range(n):
        matriks1[i][j] = int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))

## Proses
for i in range(m):
    for j in range(n):
        ### Baris paling atas
        if i == 0:
            ### Pojok kiri atas
            if j == 0:
                matriks2[i][j] = matriks1[i][j+1] + matriks1[i+1][j]
            ### Pojok kanan atas
            elif j == n - 1:
                matriks2[i][j] = matriks1[i][j-1] + matriks1[i+1][j]
            ### Elemen lainnya
            else: # 0 < j < n - 1
                matriks2[i][j] = matriks1[i][j-1] + matriks1[i][j+1] + matriks1[i+1][j]
        
        ### Baris paling bawah
        elif i == m - 1:
            ### Pojok kiri bawah
            if j == 0:
                matriks2[i][j] = matriks1[i][j+1] + matriks1[i-1][j]
            ### Pojok kanan bawah
            elif j == n - 1:
                matriks2[i][j] = matriks1[i][j-1] + matriks1[i-1][j]
            ### Elemen lainnya
            else: # 0 < j < n - 1
                matriks2[i][j] = matriks1[i][j-1] + matriks1[i][j+1] + matriks1[i-1][j]
        
        ### Kolom paling kiri (0 < i < m - 1, kasus i = 0 atau i = m - 1 sudah dicek di percabangan sebelumnya)
        elif j == 0:
            matriks2[i][j] = matriks1[i][j+1] + matriks1[i+1][j] + matriks1[i-1][j]
        
        ### Kolom paling kanan (0 < i < m - 1, kasus i=0 atau i=m-1 sudah dicek di percabangan sebelumnya)
        elif j == n - 1:
            matriks2[i][j] = matriks1[i][j-1] + matriks1[i+1][j] + matriks1[i-1][j]
        
        ### Elemen sisanya
        else: # (0 < i < m - 1) and (0 < j < n - 1)
            matriks2[i][j] = matriks1[i][j-1] + matriks1[i][j+1] + matriks1[i-1][j] + matriks1[i+1][j]

## Output
        if j == n - 1:
            print(matriks2[i][j])
        else: # 0 <= j < n - 1
            print(matriks2[i][j], end=" ")
            

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""