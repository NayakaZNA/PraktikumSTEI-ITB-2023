# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 2 November 2023
# Deskripsi : 

# KAMUS
# m             : int       ; panjang sisi papan catur
# peta_catur    : arr[str]  ; peta catur
# skak          : bool      ; bernilai True jika raja terkena skak oleh kuda

# ALGORITMA
## fungsi kuda_gerak
def raja_kena_skak(matrix: list[str], i: int, j: int, m: int) -> bool:
    # Menentukan apakah raja sedang diskak kuda
    mampus = False

    # Maaf ini kurang efisien soalnya saya lagi skill issue

    if matrix[i][j] == 'K':
        # Bisa menyerang ke atas
        if i > 1:
            ## Atas kanan
            if (j < m - 1) and (matrix[i-2][j+1] == 'R'):
                mampus = True
            ## Atas kiri
            if (j > 0) and (matrix[i-2][j-1] == 'R'):
                mampus = True

        # Bisa menyerang ke bawah
        if (m - 1) - i > 1:
            ## Bawah kanan
            if (j < m - 1) and (matrix[i+2][j+1] == 'R'):
                mampus = True
            ## Bawah kiri
            if (j > 0) and (matrix[i+2][j-1] == 'R'):
                mampus = True

        # Bisa menyerang ke kiri
        if j > 1:
            ## Kiri atas
            if (i > 0) and (matrix[i-1][j-2] == 'R'):
                mampus = True
            ## Kiri bawah
            if (i < m - 1) and (matrix[i+1][j-2] == 'R'):
                mampus = True
            
        # Bisa menyerang ke kanan
        if (m - 1) - j > 1:
            ## Kanan atas
            if (i > 0) and (matrix[i-1][j+2] == 'R'):
                mampus = True
            ## Kanan bawah
            if (i < m - 1) and (matrix[i+1][j+2] == 'R'):
                mampus = True
    return mampus

## Input m
m = int(input("Masukkan nilai m: "))

## Inisiasi matriks dan variabel
peta_catur  = [["" for i in range(m)] for i in range(m)]
skak        = False

## Input peta catur
for i in range(m):
    for j in range(m):
        peta_catur[i][j] = input(f"Masukkan elemen matriks ke-{i + 1} {j + 1}: ")

## Proses
### Menggunakan perulangan untuk mengecek apakah kuda bisa menskak raja
for i in range(m):
    for j in range(m):
        if raja_kena_skak(peta_catur, i, j, m):
            skak = True

## Output
if skak:
    print("Raja tidak aman dari serangan kuda.")
else: # not skak
    print("Raja aman dari serangan kuda.")

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""