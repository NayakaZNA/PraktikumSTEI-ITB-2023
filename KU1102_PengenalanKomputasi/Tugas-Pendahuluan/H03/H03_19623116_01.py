# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 10 Oktober 2023
# Deskripsi : Program menentukan nomor undangan yang tidak datang

# KAMUS
"""
n, m      : integer
hadir_gak : array[boolean] ; elemen ke-(i-1) bernilai True jika perwakilan ke-i hadir, vice versa
"""

# ALGORITMA

## Input M dan N
n = int(input("Masukkan nilai N: "))
m = int(input("Masukkan nilai M: "))

## Inisialisasi Awal
hadir_gak   = [False for i in range(n)]

## Proses
### Input Data Kehadiran
for i in range(1, m + 1):
    ### Ubah nilai kehadiran perwakilan tersebut menjadi True
    hadir_gak[int(input(f"Masukkan data ke {i}: ")) - 1] = True

## Output
print("Nomor perwakilan yang tidak datang: ", end="")
for i in range(n): 
    if not hadir_gak[i]:
        print(i + 1, end=" ")
