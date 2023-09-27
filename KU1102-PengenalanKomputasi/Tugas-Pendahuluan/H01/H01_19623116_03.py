# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 14 September 2023
# Deskripsi : Program Menentukan Harga Kursi Pesawat

# KAMUS
# n, harga  : int
# p, type   : str 

# ALGORITMA

# Input
n = int(input("Tentukan Nomor Kursi: "))
p = input("Tentukan Posisi Kursi: ")

# Proses
# Hot Seat
if ((1 <= n <= 20) or (51 <= n <= 60)):
    type = "Hot Seat"
    if (p == "A" or p == "F"):
        harga = 1_600_000
    elif (p == "B" or p == "E"):
        harga = 1_550_000
    else: # p == C or p == D
        harga = 1_500_000

# Regular
else: # (21 <= n <= 50) or (61 <= n <= 100)
    type = "Regular"
    if (p == "A" or p == "F"):
        harga = 1_000_000
    elif (p == "B" or p == "E"):
        harga = 950_000
    else: # p == C or p == D
        harga = 900_000

# Output
print(f"Tuan Kil memilih kursi {type} dengan harga {harga}.")
