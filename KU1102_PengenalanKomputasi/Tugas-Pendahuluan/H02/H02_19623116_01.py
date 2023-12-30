# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 26 September 2023
# Deskripsi : Program menentukan apakah suatu bilangan merupakan perpangkatan dari bilangan lain
# Panjang   : 15 lines

# KAMUS
# n, nn, k : integer

# ALGORITMA

# Input
n = int(input("Masukkan bilangan N: "))
k = int(input("Masukkan nilai k: "))

# Inisialisasi Awal
nn = n

# While loop (untuk k > 1)
if k != 1:
    # Jika n adalah perpangkatan dari k maka n = k^a untuk sembarang bilangan asli a. Jadi, n habis dibagi k.
    # Akibatnya n bisa terus dibagi k (sebanyak a kali) hingga menjadi 1. Loop langsung dihentikan jika n tidak habis dibagi k lagi.
    while (nn % k == 0):
        nn /= k
    if nn == 1:
        print(f"{n} merupakan perpangkatan {k}.")
    else: #nn != 1
        print(f"{n} bukan merupakan perpangkatan {k}.")

# Antisipasi corner case k = 1 (infinite loop)
else: # k == 1
    if n == 1:
        nn = 1
    else: # n != 1
        print(f"{n} bukan merupakan perpangkatan {k}.")

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""
