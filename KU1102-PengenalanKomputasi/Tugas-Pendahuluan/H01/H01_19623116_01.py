# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 14 September 2023
# Deskripsi : Program Menentukan Kelulusan Tuan Kil berdasarkan Nilai Ujian/Rata-Ratanya

# KAMUS
# n_1, n_2, n_3, n_4    : integer
# avg                   : float

# ALGORITMA

# Input
n_1 = int(input("Masukkan nilai ujian 1: "))
n_2 = int(input("Masukkan nilai ujian 2: "))
n_3 = int(input("Masukkan nilai ujian 3: "))
n_4 = int(input("Masukkan nilai ujian 4: "))

# Proses
avg = (n_1 + n_2 + n_3 + n_4)/4 # Menghitung rerata nilai

# Menggunakan percabangan untuk menentukan kelulusan
if ((n_1 < 50) or (n_2 < 50) or (n_3 < 50) or (n_4 < 50) or (avg < 70)):
    print("Tuan Kil tidak lulus kelas Tuan Leo.")
    # Jika ada nilai yang kurang dari 50 atau reratanya kurang dari 70 maka Tuan Kil tidak lulus
else: # Semua nilai >= 50 dan rerata >= 70
    print("Tuan Kil lulus kelas Tuan Leo.")
    # Kalau tidak, maka Tuan Kil lulus
