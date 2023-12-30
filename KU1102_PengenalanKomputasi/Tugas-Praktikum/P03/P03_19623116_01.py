# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 19 Oktober 2023
# Deskripsi : Program mencari biaya minimum untuk makan di restoran selama 3 jam tanpa henti
# Panjang   : 20 lines

# KAMUS
# n             : integer
# harga         : array[float]      ; elemen ke-i adalah harga jam ke-(i + 1)
# biaya         : array[float]      ; elemen ke-i adalah total biaya jika mulai makan dari jam ke-(i + 1)
# mini_index    : integer           ; indeks dari elemen terkecil dalam array
# mini          : integer           ; elemen terkecil dalam array

# ALGORITMA
## Input N
n = int(input("Masukkan nilai N: "))

## Inisialisasi Awal
harga = [0 for i in range(n)]
biaya = [0 for i in range(n - 2)]

## Input harga
for i in range(n):
    harga[i] = float(input(f"Masukkan harga jam ke-{i + 1}: "))

## Proses
### Menghitung total biaya yang dikeluarkan jika mulai pada tiap jamnya 
### (tidak bisa mulai dari 2 jam terakhir)
for i in range(n - 2):
    biaya[i] = harga[i] + harga[i + 1] + harga[i + 2]

### Melakukan sorting (dengan selection sort) untuk mengurutkan biaya
for i in range(n - 2):
    mini_index = i
    # Membandingkan elemen ke-i dengan semua elemen di kanannya
    for j in range(i + 1, n - 2):
        if biaya[j] < biaya[mini_index]:
            mini_index = j
        mini = biaya[mini_index]
    
    # Push semua elemen ke kanan dan taruh `mini`` di indeks ke-i
    for k in range(n - 3, i - 1, -1):
        biaya[k] = biaya[k - 1]
    biaya[i] = mini

## Output
### Formatting
if int(biaya[0]) == biaya[0]:   # biaya berupa bilangan bulat
    print(f"Total harga yang harus dibayar adalah {biaya[0]:.0f}.")
else: #int(biaya[0]) != biaya[0], biaya berupa bilangan desimal
    print(f"Total harga yang harus dibayar adalah {biaya[0]}.")


"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""
