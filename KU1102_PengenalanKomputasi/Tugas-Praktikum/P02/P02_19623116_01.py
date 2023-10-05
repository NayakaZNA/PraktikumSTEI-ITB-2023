# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 5 Oktober 2023
# Deskripsi : Program Menentukan Banyaknya Kegiatan di Gedung A dan B

# KAMUS
# n             : integer; kapasitas peserta per kegiatan di gedung A
# psrta         : integer; banyaknya peserta pada kegiatan ke-i
# keg_a, keg_b  : integer; banyaknya kegiatan pada tiap gedung
# i             : integer; urutan kegiatan

# ALGORITMA

## Inisialisasi Awal
keg_a   = 0
keg_b   = 0
i       = 1
## Input
n = int(input("Masukkan nilai N: "))

## Proses

### While loop; dilakukan selagi kegiatan di gedung B kurang belum mencapai 3
while (keg_b < 3):
    ### Terus menerima input jumlah peserta per kegiatan
    psrta = int(input(f"Masukkan peserta kegiatan ke-{i}: "))

    """
    Jika peserta kurang dari n dan kapasitas kegiatan gedung A belum dilampaui,
    masukkan ke gedung A dulu---kalau sudah tidak cukup, masukkan ke gedung B.
    """
    if (psrta < n):
        if keg_a < 5:
            keg_a += 1
        else: # keg_a = 5 (keg_a > 5 mustahil)
            keg_b += 1
    else:
        keg_b += 1
    i += 1

## Output
print(f"Terdapat {keg_a} kegiatan di gedung A dan {keg_b} kegiatan di gedung B.")

"""
Mudah-mudahan AC :D 
Semangat ngoreksinya, Kak!
- Nayaka
"""  