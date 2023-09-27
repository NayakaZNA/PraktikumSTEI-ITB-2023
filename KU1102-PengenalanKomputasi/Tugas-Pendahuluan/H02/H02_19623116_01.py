# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 26 September 2023
# Deskripsi : Program menentukan apakah suatu bilangan merupakan perpangkatan dari bilangan lain

# KAMUS
# n, nn, k : integer

# ALGORITMA

# Input
n = int(input("Masukkan bilangan N: "))
k = int(input("Masukkan nilai k: "))

# Inisialisasi Awal
nn = n

# While loop
# Jika n adalah perpangkatan dari k maka n = k^a untuk sembarang bilangan asli a. Jadi, n habis dibagi k.
# Akibatnya n bisa terus dibagi k (sebanyak a kali) hingga menjadi 1. Loop dihentikan jika n tidak habis dibagi k lagi.
while (nn % k == 0):
    nn /= k
if nn == 1:
    print(f"{n} merupakan perpangkatan {k}.")
else: #nn != 1
    print(f"{n} bukan merupakan perpangkatan {k}.")
