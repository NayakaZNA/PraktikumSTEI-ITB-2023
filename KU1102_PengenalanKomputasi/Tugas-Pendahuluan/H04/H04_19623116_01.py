# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 24 Oktober 2023
# Deskripsi : Program menentukan jumlah maksimum submatriks 2x2 yang memuat elemen ganjil
# (18 lines)

# KAMUS
# m, n            : integer             ; dimensi matriks
# row_matriks     : string              ; menyimpan input tiap baris matriks
# matriks         : list[list[integer]] ; matriks yang diproses
# ganteng         : integer             ; total jumlah maksimum submatriks 2x2 yang memuat bilangan ganjil


# ALGORITMA

## Input M dan N
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

## Inisialisasi Awal
matriks         = [[0 for j in range(n)] for i in range(m)]
ganteng         = 0

## Input Elemen matriks
print("Masukkan elemen matriks: ")
for i in range(m):
    row_matriks = input()
    ### Pecah string dalam `row_matriks` menjadi tiap elemen lalu masukkan ke `matriks`
    for j in range(n):
        matriks[i][j] = int(row_matriks.split()[j])

## Proses
### For loop
for i in range(m-1):
    for j in range(1, n):
        ### Cari submatriks 2x2 yang punya elemen ganjil
        if matriks[i][j] % 2 == 1 or matriks[i][j-1] % 2 == 1:
            ### Jumlahkan semua elemen submatriks tersebut, bandingkan dengan jumlah sebelumnya
            if ganteng < matriks[i][j] + matriks[i][j-1] + matriks[i+1][j] + matriks[i+1][j-1]:
                ### Jika jumlahnya lebih besar, update nilai `ganteng` dengan jumlah tersebut
                ganteng = matriks[i][j] + matriks[i][j-1] + matriks[i+1][j] + matriks[i+1][j-1]

## Output
if ganteng == 0:
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")
else:   # ganteng > 0
    print(f"Jumlah maksimum dari submatriks 2x2 yang memiliki elemen ganjil adalah {ganteng}")

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""
