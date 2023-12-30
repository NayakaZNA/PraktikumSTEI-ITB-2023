# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 19 Oktober 2023
# Deskripsi : Program menentukan ketepatan kata yang ditulis Komi
# Panjang   : 19 lines

# KAMUS
# orlen, wrlen      : integer   ; panjang kata asli dan yang ditulis
# orword, wrword    : string    ; kata asli dan yang ditulis
# word              : string    ; kata yang seharusnya ditulis

# ALGORITMA
## Inisialisasi Awal
word    = ""

## Input
orlen   = int(input("Masukkan panjang kata asli: ") )
orword  = input("Masukkan kata asli: ")
wrlen   = int(input("Masukkan panjang kata yang ditulis: "))
wrword  = input("Masukkan kata yang ditulis: ")

## Proses
### Menentukan kata yang seharusnya ditulis Komi
i = 0
while i < orlen:
    j = 0
    while j < (i + 1):
        word = f"{word}{orword[j]}"
        j += 1
        # Break ketika panjang kata sudah sesuai
        if len(word) == wrlen:
            i = orlen
            j = i + 1
    i += 1
### Mengecek apakah kata yang Komi tulis sudah benar
if wrword == word:
    print("Tulisan Komi sudah benar.")
else: #wrword != word
    print("Tulisan Komi masih salah.")

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""