# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 5 Oktober 2023
# Deskripsi : Program Mencetak Barisan Unik (Naik Turun)

# KAMUS
# x, y  : integer
# count : integer; untuk keep track panjang barisan
# yi    : integer; menyimpan nilai awal y

# ALGORITMA
## Input
x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))

## Inisialisasi
count   = 0
yi      = y

## Proses
### While loop; dilakukan selagi panjang barisan belum melebihi x
while count < x:
    i = 1
    #### Barisan Naik
    while (i < y and count < x):
        print(i, end=" ")
        i += 1
        count += 1
    # Setelah loop ini berakhir, i mencapai y
    
    #### Barisan Turun
    y += yi
    while (i > 1 and count < x):
        print(i, end=" ")
        i -= 1
        count += 1

"""
Mudah-mudahan AC :D 
Semangat ngoreksinya, Kak!
- Nayaka
"""  