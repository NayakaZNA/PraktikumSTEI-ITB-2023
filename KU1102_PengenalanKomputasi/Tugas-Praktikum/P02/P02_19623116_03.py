# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 5 Oktober 2023
# Deskripsi : Program mencetak piramida bilangan
# Panjang   : 18 lines

# KAMUS
# length    : integer; panjang segitiga
# lengthn   : integer; panjang baris (tidak mencakup)
# a         : integer; selisih angka antarbaris
# num       : integer; angka yang dicetak pada baris

# ALGORITMA
## Inisialisasi Awal
length  = 76
lengthn = 1
num     = 1

## Input

### Terus menerima input jika panjang piramida melebihi 75 atau panjangnya genap
while ((length > 75) or (length % 2 == 0)):
    length = int(input("Masukkan panjang piramida: "))

### Input selisih angka antarbaris:
a = int(input("Masukkan selisih: "))

## Proses

### Jika panjangnya genap, dikurangi 1 (instruksi asprak Kak Christina Wijaya)
if length % 2 == 0:
    length -= 1

### While loop; dilakukan hingga baris terbawah hanya berisi angka
while (lengthn <= length):
    ### X kiri
    for i in range((length - lengthn) // 2):
        print("X", end="")
    
    ### Angka
    for i in range(lengthn):
        print(num, end="")

    ### X kanan
    for i in range((length - lengthn) // 2):
        print("X", end="")
    
    ### Newline
    print()

    ### Update nilai variabel
    num = (num + a) % 10    # Ambil digit satuan dari num + a
    lengthn += 2            # Increment panjang baris yang memuat angka sebanyak 2

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
""" 
