# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 10 Oktober 2023
# Deskripsi : Program menentukan stasiun awal agar Tuan Leo bisa kunjungi stasiun sebanyak mungkin

# KAMUS
# duit          : integer
# n             : integer   ; banyaknya stasiun
# harga         : array     ; menampung harga stasiun ke-(i + 1)
# biaya         : integer   ; total biaya kereta Tuan Leo dalam satu perjalanan
# visited       : integer   ; stasiun yang telah dikunjungi
# visits        : integer   ; banyaknya stasiun yang dapat dikunjungi jika mulai dari stasiun ke-(i + 1)
# j             : integer   ; variabel iterator while
# idx_maks      : integer   ; indeks dari nilai maksimum suatu array
# count         : integer   ; jika uang Tuan Leo tidak cukup, bisa = 0

# ALGORITMA

## Input awal
duit    = int(input("Masukkan uang yang dibawa Tuan Leo: "))
n       = int(input("Masukkan jumlah stasiun: "))

## Inisialisasi Awal
harga   = [0 for i in range(n)]
visits  = [0 for i in range(n)]
count   = 0

## Input harga stasiun
for i in range(n):
    harga[i] = int(input(f"Masukkan harga stasiun ke-{i + 1}: "))

## Proses
### Menghitung banyaknya stasiun yang dicapai dimulai dari tiap stasiun
for i in range(n):
    j       = i
    visited = 0
    biaya   = 0
    maks    = 0
    if harga[j] <= duit:
        #### Berjalan ke stasiun selanjutnya selagi uang masih cukup
        while biaya < duit:
            biaya   += harga[j]
            visited += 1
            j       = (j + 1) % n
        #### Mengantisipasi total biaya akhir melebihi uang Tuan Leo
        if biaya > duit:
            visited -= 1
        #### Mengantisipasi `visited` melebihi banyak stasiun yang ada
        if visited > n:
            visited = n
        #### Menyimpan nilai `visited` ke dalam `visits`
        visits[i]   = visited
        #### Increment variabel `bisa`
        count += 1

# Output
if count == 0:
    print("Tuan Leo kekurangan uang.")
else:
### Mencari i sehingga visits[i] maksimum
    for i in range(n, -1, -1):
        idx_maks = i
        for j in range(i + 1, n):
            if visits[idx_maks] < visits[j]:
                idx_maks = j
print(f"Tuan Leo dapat mengunjungi {visits[idx_maks]} stasiun dimulai dari stasiun ke-{idx_maks + 1}.")
