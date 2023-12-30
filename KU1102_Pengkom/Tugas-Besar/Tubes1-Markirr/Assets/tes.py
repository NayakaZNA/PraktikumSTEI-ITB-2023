import time
import numpy as np
from tabulate import tabulate
from datetime import datetime

# Inisialisasi variabel parkir
parking_space = {
    'motor': 10,  # Jumlah space parkir untuk motor
    'mobil': 5,   # Jumlah space parkir untuk mobil
}

# Inisialisasi biaya parkir per jam
biaya_parkir = {
    'motor': 2000,  # Biaya parkir per jam untuk motor
    'mobil': 5000   # Biaya parkir per jam untuk mobil
}

# Inisialisasi data parkir
data_parkir = {
    'motor': {},
    'mobil': {}
}

# Inisialisasi daftar space VIP
space_vip = {
    'motor': [],
    'mobil': []
}

# Inisialisasi matriks space parkir
matrix_motor = np.zeros((1, parking_space['motor']), dtype=int)
matrix_mobil = np.zeros((1, parking_space['mobil']), dtype=int)

def identifikasi_jenis_kendaraan():
    while True:
        jenis_kendaraan = input("Jenis kendaraan (motor/mobil): ").lower()
        if jenis_kendaraan in parking_space:
            return jenis_kendaraan
        else:
            print("Jenis kendaraan tidak valid. Silakan masukkan 'motor' atau 'mobil'.")

def identifikasi_tipe_parkir():
    while True:
        tipe_parkir = input("Tipe parkir (VIP/reguler): ").lower()
        if tipe_parkir in ['vip', 'reguler']:
            return tipe_parkir
        else:
            print("Tipe parkir tidak valid. Silakan masukkan 'VIP' atau 'reguler'.")

def cek_parkir(jenis_kendaraan):
    if len(data_parkir[jenis_kendaraan]) < parking_space[jenis_kendaraan]*2:
        return True
    return False

def cari_parkir_kosong(jenis_kendaraan):
    if jenis_kendaraan == 'motor':
        matrix = matrix_motor
    else:
        matrix = matrix_mobil
    counter_shape=0
    for i in range(matrix.shape[counter_shape]):
        for j in range(matrix.shape[counter_shape+1]):
            if matrix[i, j] == 0:
                return i, j
    counter_shape+=1
    return None

def hitung_durasi_parkir(masuk, keluar):
    durasi = keluar - masuk
    durasi_jam = durasi.days * 24 + durasi.seconds / 3600  # Menghitung durasi dalam jam
    return durasi_jam  # Menghitung durasi dalam jam

def hitung_biaya_parkir(jenis_kendaraan, durasi, tipe_parkir):
    if tipe_parkir == 'vip':
        return durasi * biaya_parkir[jenis_kendaraan] * 1.5
    else:
        return durasi * biaya_parkir[jenis_kendaraan]

def print_parking_matrix():
    header = [str(i + 1) for i in range(parking_space['motor'])]
    table_motor = tabulate(matrix_motor, headers=header, tablefmt="pretty")
    table_mobil = tabulate(matrix_mobil, headers=header, tablefmt="pretty")

    print("\n=== Matriks Space Parkir Motor ===")
    print(table_motor)

    print("\n=== Matriks Space Parkir Mobil ===")
    print(table_mobil)

while True:
    print_parking_matrix()

    print("\n=== Sistem Parkir Mall ===")
    jenis_kendaraan = identifikasi_jenis_kendaraan()
    tipe_parkir = identifikasi_tipe_parkir()

    if cek_parkir(jenis_kendaraan):
        i, j = cari_parkir_kosong(jenis_kendaraan)
        if (i, j) is not None:
            print(f"Parkir kendaraan {jenis_kendaraan} di space {i + 1}, baris {j + 1}.")
            masuk = datetime.fromtimestamp(time.time())
            input("Tekan Enter saat kendaraan keluar.")
            keluar = datetime.fromtimestamp(time.time())
            durasi = hitung_durasi_parkir(masuk, keluar)
            biaya = hitung_biaya_parkir(jenis_kendaraan, durasi, tipe_parkir)
            print(f"Kendaraan telah parkir selama {durasi:.2f} jam.")
            print(f"Biaya parkir ({tipe_parkir}): Rp {biaya:.2f}")
            data_parkir[jenis_kendaraan][(i + 1, j + 1)] = keluar
            if tipe_parkir == 'vip':
                space_vip[jenis_kendaraan].append((i + 1, j + 1))
            if jenis_kendaraan == 'motor':
                matrix_motor[i, j] = 1
            else:
                matrix_mobil[i, j] = 1
        
        else:
            print("Maaf, semua space parkir sudah terisi.")
    else:
        print("Maaf, tidak ada space parkir untuk kendaraan jenis ini. Silakan parkir di luar mall.")