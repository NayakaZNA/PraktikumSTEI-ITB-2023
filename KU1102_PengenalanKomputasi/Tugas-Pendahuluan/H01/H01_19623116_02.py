# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 14 September 2023
# Deskripsi : Program menghitung gradien garis
# Panjang   : 11 lines

# KAMUS
# x1, y1, x2, y2    : integer
# m                 : float

# ALGORITMA

# Input
x1 = int(input("Masukkan x1: "))
y1 = int(input("Masukkan y1: "))
x2 = int(input("Masukkan x2: "))
y2 = int(input("Masukkan y2: "))

# Proses
if (y1 == y2):
    print("Garis tersebut merupakan garis horizontal.") # Tiap titik pada garis horizontal ordinatnya sama
elif (x1 == x2):
    print("Garis tersebut merupakan garis vertikal.") # Tiap titik pada garis vertikal absisnya sama
else:   # Garis dengan gradien tertentu
    m = (y2 - y1)/(x2 - x1) # baru dilakukan untuk menghindari pembagian dengan nol jika garisnya vertikal
    print(f"Garis tersebut memiliki gradien {m}.")

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""