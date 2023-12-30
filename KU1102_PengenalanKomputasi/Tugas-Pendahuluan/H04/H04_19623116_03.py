# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 10 Oktober 2023
# Deskripsi : Program menentukan banyaknya kapal (deretan '1' horizontal/vertikal) dalam peta 
# KAMUS
# n, m          : integer               ; dimensi peta
# row_peta      : string                ; baris pada peta
# katakan_peta  : array[array[integer]] ; petanya
# count         : integer               ; banyaknya kapal perang dalam peta

# ALGORITMA
## Input N dan M
n = int(input("Masukkan nilai N: "))
m = int(input("Masukkan nilai M: "))

## Inisialisasi Awal
katakan_peta    = [[0 for j in range(m)] for i in range(n)]
katakan_kapal   = 0

## Input Peta
print("Masukkan peta: ")
for i in range(n):
    row_peta = input()
    ### Pecah string dalam `row_peta` menjadi tiap elemen lalu masukkan ke `katakan_peta`
    for j in range(m):
        katakan_peta[i][j]   = int(row_peta[j])

## Proses
### Mengecek banyaknya kapal
for i in range(n):
    for j in range(m):
        if (katakan_peta[i][j] == 1) and (j == 0 or katakan_peta[i][j-1] == 0) and (i == 0 or katakan_peta[i-1][j] == 0): 
            katakan_kapal += 1

## Output
if katakan_kapal == 0:
    print("Tidak terdapat kapal musuh pada peta")
else: # katakan_kapal > 0
    print(f"Terdapat {katakan_kapal} kapal musuh pada peta")


"""
Penjelasan:
Cek saja apakah tetangga atas dan kiri adalah 0. Jika iya, elemen tersebut dihitung sebagai kapal.
Artinya kita tidak menghitung elemen 1a yang seperti ini sebagai kapal:
0  0  0  0 
0  0  0  1 
1  1a 0  1a
0  0  0  1a
Ini lebih efisien ketimbang mengecek lalu mengubah elemen yang sudah dicek menjadi 0.

Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""