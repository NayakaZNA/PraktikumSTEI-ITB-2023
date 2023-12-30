# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 2 November 2023
# Deskripsi : Program menghitung nilai tugas praktikum berdasarkan bobotnya (dan menentukan kevalidan bobot)

# KAMUS
# a, b, c                   : float ; bobot nilai tiap soal
# score1, score2, score3    : int   ; nilai tiap soal

# ALGORITMA
## Inisialisasi Fungsi
### Fungsi cek_valid
def cek_valid(a: int, b: int, c: int) -> bool:
    # Menentukan apakah bobot yang diberikan valid
    if (a + b + c == 1) and (0 <= a <= 1) and (0 <= b <= 1) and (0 <= c <= 1):
        valid_gak = True
    else: # not(a + b + c == 1) or not(0 <= a <= 1) or not(0 <= b <= 1) or not(0 <= c <= 1)
        valid_gak = False
    return valid_gak

### Prosedur hitung
def hitung(a: int, b: int, c: int, x1: int, x2: int, x3: int) -> float:
    # Menghitung nilai tugas praktikum jika bobotnya valid
    if cek_valid(a, b, c):
        print(f"Nilai tugas praktikum adalah {a*x1 + b*x2 + c*x3:.2f}")
    else: #not cek_valid(a, b, c)
        print("bobot tidak valid")
    return

## Input
a       = float(input("Masukkan nilai a: "))
b       = float(input("Masukkan nilai b: "))
c       = float(input("Masukkan nilai c: "))
score1  = int(input("Masukkan nilai soal 1: "))
score2  = int(input("Masukkan nilai soal 2: "))
score3  = int(input("Masukkan nilai soal 3: "))

## Proses & Output
hitung(a, b, c, score1, score2, score3)


"""
NB: soal menyatakan a, b, c bilangan bulat tetapi test case menunjukkan
bahwa a, b, c bisa sembarang bilangan desimal sehingga saya pilih tipe
datanya sebagai float.

Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""