# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 5 Oktober 2023
# Deskripsi : Program Mencetak Piramida Bilangan

# KAMUS
# length    : integer; panjang segitiga
# lengthn   : integer; panjang baris (tidak mencakup)
# a         : integer; selisih angka antarbaris
# num       : integer; angka yang dicetak pada baris
# line      : integer; keep track banyaknya baris yang tercetak

# ALGORITMA
## Inisialisasi Awal
length  = 76
lengthn = 1
num     = 1

## Input

### Memastikan panjang piramida tidak melebihi 75
"""
(Tidak diinstruksikan apa yang harus dilakukan jika demikian
jadi saya tetap terima inputnya hingga valid)
"""
while (length > 75):
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
Mudah-mudahan AC :D 
Semangat ngoreksinya, Kak!
- Nayaka
"""  