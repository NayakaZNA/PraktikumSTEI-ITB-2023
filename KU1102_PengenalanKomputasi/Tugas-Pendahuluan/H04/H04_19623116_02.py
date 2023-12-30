# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 24 Oktober 2023
# Deskripsi : Program menentukan banyak bakteri (semula n) pada detik ke-k

# KAMUS
# n, k  : integer

# ALGORITMA

## INKUBASI
"""
detik | bakteri
———————————————————————————————————————
0     | n
1     | n + 2n
2     | n + 2n + 4n
k     | n + (2^1 + 2^2 + ... + 2^k) * n = n + n * sum_(i=1)^(k) 2^i
"""

## Fungsi BerapaBacter
def BerapaBacter(n, k):
    ### Menghitung jumlah Pengkombacter dengan jumlah awal n pada detik ke-k
    #### Jumlah awal
    banyak = n
    #### Menambah Pengkombacter
    for i in range(1, k + 1):
        banyak += n * 2 ** i
    return banyak

## Input
n   = int(input("Masukkan N: "))
k   = int(input("Masukkan K: "))

## Output
print(f"Terdapat {BerapaBacter(n, k)} Bakteri Pengkombacter.")

"""
Sebenarnya nilai deret geometri tersebut adalah S_n = n * (2 ** (k + 1) - 1) jadi
kita bisa saja definisikan
def BerapaBacter(n, k):
    return n * (2 ** (k + 1) - 1)

Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""