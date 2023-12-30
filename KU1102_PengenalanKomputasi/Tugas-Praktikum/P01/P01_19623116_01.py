# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 21 September 2023
# Deskripsi : Program menentukan nominal uang terbesar
# Panjang   : 8 lines

# KAMUS
# peng, kom : float

# ALGORITMA

# Input
peng    = float(input("Banyak uang Peng yang ditawarkan: "))
kom     = float(input("Banyak uang Kom yang ditawarkan: "))
peng   *= float(input("Konversi mata uang Peng ke rupiah: "))
kom    *= float(input("Konversi mata uang Kom ke rupiah: "))

# Proses
if peng > kom:
    print("Adik Tuan Kil memilih uang Peng.")
else: # peng < kom, mengasumsikan peng != kom pasti berlaku
    print("Adik Tuan Kil memilih uang Kom.")
  
"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""