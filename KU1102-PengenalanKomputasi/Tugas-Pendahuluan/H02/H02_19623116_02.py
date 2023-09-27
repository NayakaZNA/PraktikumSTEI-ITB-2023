# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 26 September 2023
# Deskripsi : Program membuat segitiga angka

# KAMUS
# h     : integer
# num   : integer;  variabel untuk keep track angka pada segitiga

# ALGORITMA

# Input
h = int(input("Masukkan nilai H: "))

# Proses
num = 1
"""
Inkubasi
Jika H ganjil, baris tengah pada segitiga tidak punya kembaran.
Untuk mengantisipasi tersebut, kita perlu cetak satu baris lagi jika H ganjil.
Perhatikan jika H genap : (h + 1) // 2 = h / 2; 
           jika H ganjil: (h + 1) // 2 = (h + 1) / 2
"""

# Membuat segitiga bagian atas
for i in range((h + 1) // 2):
    # Mencetak tiap baris pada segitiga
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    # Memberi newline antarbaris
    print()

# Membuat segitiga bagian bawah
for i in range(h//2, 0, -1):
    # Mencetak tiap baris pada segitiga
    for j in range(i + 1, 1, -1):
        print(num, end=" ")
        num += 1
    # Memberi newline antarbaris
    print()
