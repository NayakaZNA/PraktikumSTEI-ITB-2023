# Import library Tkinter dan datetime
import tkinter as tk
from datetime import datetime

# Membuat jendela utama
window = tk.Tk()
window.title("Sistem Parkir Mall")

# Membuat label dan kolom masukan untuk jenis kendaraan dan nomor plat
label_jenis = tk.Label(window, text="Jenis Kendaraan (misalnya, Mobil, Motor):")
label_jenis.pack()

input_jenis = tk.Entry(window)
input_jenis.pack()

label_plat = tk.Label(window, text="Nomor Plat:")
label_plat.pack()

input_plat = tk.Entry(window)
input_plat.pack()

# Membuat label dan kolom masukan untuk ruang parkir (baris dan kolom)
label_baris = tk.Label(window, text="Ruang Parkir (Baris):")
label_baris.pack()
input_baris = tk.Entry(window)
input_baris.pack()

label_kolom = tk.Label(window, text="Ruang Parkir (Kolom):")
label_kolom.pack()

input_kolom = tk.Entry(window)
input_kolom.pack()

# Membuat tombol parkir
def parkir_kendaraan():
    # Mengambil input dari pengguna
    jenis_kendaraan = input_jenis.get()
    nomor_plat = input_plat.get()
    baris_parkir = input_baris.get()
    kolom_parkir = input_kolom.get()
    
    # Memeriksa ketersediaan tempat parkir (pengecekan disederhanakan)
    if jenis_kendaraan.lower() == "mobil":
        tempat_kosong = 50
    elif jenis_kendaraan.lower() == "motor":
        tempat_kosong = 20
    else:
        tempat_kosong = 0

    if tempat_kosong > 0:
        # Memeriksa apakah input baris dan kolom adalah angka yang valid
        if baris_parkir.isdigit() and kolom_parkir.isdigit():
            baris_parkir = int(baris_parkir)
            kolom_parkir = int(kolom_parkir)
            
            # Memeriksa apakah baris dan kolom berada dalam rentang yang valid
            if 1 <= baris_parkir <= num_baris and 1 <= kolom_parkir <= num_kolom:
                if ruang_parkir[baris_parkir - 1][kolom_parkir - 1]["text"] == "Kosong":
                    # Parkir kendaraan di ruang yang dipilih
                    pesan = f"Kendaraan {jenis_kendaraan} dengan nomor plat {nomor_plat} parkir di ruang {baris_parkir}, {kolom_parkir}."
                    tempat_kosong -= 1#tempat kosong dikurangi 1
                    waktu_masuk = datetime.now() #mencatat waktu masuk
                    ruang_parkir[baris_parkir - 1][kolom_parkir - 1].config(text=nomor_plat) #teks "kosong" diubah menjadi nomor plat kendaraan
                    kendaraan_terparkir[baris_parkir - 1][kolom_parkir - 1] = {
                        "jenis_kendaraan": jenis_kendaraan,
                        "nomor_plat": nomor_plat,
                        "waktu_masuk": waktu_masuk,
                    } #dictionary untuk dipakai untuk fungsi yang memperlihatkan biaya parkir dan identitias kendaraan(di akhir)
                else:
                    pesan = f"Tempat parkir {baris_parkir}, {kolom_parkir} sudah terisi."
            else:
                pesan = "Nomor baris atau kolom tidak valid."
        else:
            pesan = "Baris dan kolom harus berisi angka."
    else:
        pesan = f"Tidak ada tempat parkir tersedia untuk {jenis_kendaraan} dengan nomor plat {nomor_plat}."

    label_hasil.config(text=pesan)
tombol_parkir = tk.Button(window, text="Parkir Kendaraan", command=parkir_kendaraan)
tombol_parkir.pack()

# Membuat label untuk menampilkan hasil
label_hasil = tk.Label(window, text="")
label_hasil.pack()

# Membuat layout parkir dengan matriks
matriks_parkir = tk.Frame(window)
matriks_parkir.pack()

# Membuat tempat parkir dalam matriks
ruang_parkir = [] # Daftar label untuk mewakili tempat parkir
kendaraan_terparkir = [] # Daftar kendaraan yang terparkir
num_baris = 5 # Jumlah baris tempat parkir
num_kolom = 10 # Jumlah kolom tempat parkir

# Mengisi matriks parkir dengan label "Kosong"
for i in range(num_baris):
    baris = [] # Daftar label untuk satu baris
    kendaraan_baris = [] # Daftar kendaraan terparkir di satu baris
    for j in range(num_kolom):
        tempat_parkir = tk.Label(matriks_parkir, text="Kosong", borderwidth=1, relief="solid", width=8)
        tempat_parkir.grid(row=i, column=j, padx=2, pady=2)
        baris.append(tempat_parkir)
        kendaraan_baris.append(None)
    ruang_parkir.append(baris)
    kendaraan_terparkir.append(kendaraan_baris)

# Fungsi untuk mengeluarkan kendaraan dari tempat parkir
def keluar_kendaraan(baris, kolom):
    if kendaraan_terparkir[baris][kolom] is not None:
        kendaraan = kendaraan_terparkir[baris][kolom]
        waktu_keluar = datetime.now() #mencatat waktu keluar kenndaraan
        durasi = waktu_keluar - kendaraan["waktu_masuk"]
        durasi_jam = durasi.total_seconds() / 3600 #mengkonversi detik menjadi jam
        jenis_kendaraan = kendaraan["jenis_kendaraan"] 
        nomor_plat = kendaraan["nomor_plat"] 
        biaya_parkir = hitung_biaya_parkir(jenis_kendaraan, durasi_jam)
        
        pesan = f"Jenis Kendaraan: {jenis_kendaraan}\nNomor Plat: {nomor_plat}\nWaktu Masuk: {kendaraan['waktu_masuk']}\nWaktu Keluar: {waktu_keluar}\nDurasi (jam): {durasi_jam:.2f}\nBiaya Parkir: Rp {biaya_parkir:.2f}"
        #menampilkan kembali jenis kendaraan, plat nomor kendaraan, waktu masuk, waktu keluar, durasi dan biaya parkir
        ruang_parkir[baris][kolom].config(text="Kosong") #ruang parkir yang diisi teksnya diubah menjadi kosong kembali
        kendaraan_terparkir[baris][kolom] = None #kendaraan tidak diparkirkan lagi
        label_hasil.config(text=pesan)
    else:
        label_hasil.config(text="Tidak ada kendaraan terparkir di tempat ini.")

# Mengikat aksi keluar ke tempat parkir
for baris in range(num_baris):
    for kolom in range(num_kolom):
        ruang_parkir[baris][kolom].bind("<Button-1>", lambda event, r=baris, c=kolom: keluar_kendaraan(r, c))

# Fungsi untuk menghitung biaya parkir
def hitung_biaya_parkir(jenis_kendaraan, durasi_jam):
    if jenis_kendaraan.lower() == "mobil":
        tarif = 5000  # Tarif per jam untuk mobil
    elif jenis_kendaraan.lower() == "motor":
        tarif = 2000  # Tarif per jam untuk motor
    else:
        tarif = 0
    
    biaya_parkir = tarif * durasi_jam
    return biaya_parkir

# Menjalankan perulangan utama
window.mainloop()