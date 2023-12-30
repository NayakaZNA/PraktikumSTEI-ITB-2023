# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 21 September 2023
# Deskripsi : Program menentukan angka spesial
# Panjang   : 12 lines

# KAMUS
# n, d1, d2, d3, d4 : integer

# ALGORITMA

# Input
n = int(input("Masukkan Angka: "))

# Proses
# Mengambil setiap digit dari n
d1  = n // 1000
d2  = n // 100 % 10
d3  = n // 10 % 10
d4  = n % 10

# Menggunakan percabangan untuk menentukan keterbagian d1*d2 oleh (d2+d3)
if (d2 + d3) != 0:                  # mengantisipasi d2 = d3 = 0 -> operasi mod 0 (undefined)
    if (d1 * d4) % (d2 + d3) == 0:  # x kelipatan y -> x habis dibagi y -> x mod y = 0
        print(f"Angka {n} adalah angka spesial.")
    else:   # d1*d4 % (d2+d3) != 0
        print(f"Angka {n} bukan angka spesial.")
else:   # d2 + d3 == 0
    print(f"Angka {n} bukan angka spesial.")

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""