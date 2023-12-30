# Program Markirr
# Perangkat lunak sistem manajemen parkir cerdas otomatis oleh
# William Anthony               [16523109]; Lead Presenter
# Muhammad Jafar Fadli          [16523137]; Backend
# Zulfaqqar Nayaka Athadiansyah [19623116]; Software Engineer and GUI Designer
# Abdullah Farhan               [19623305]; Lead Analyst

# KAMUS
## Daftar Variabel
# plat_nomor            :    arr[str]        ; daftar kode wilayah TNKB di Indonesia
# blokk                 :    dict            ; konversi blok parkir (alfabetik) ke indeks array (numerik)
# slot_id               :    arr[str, int]   ; menampung sementara blok dan nomor slot parkir
# vehicle_data          :    arr[dict]       ; menampung data kendaraan
# terisi                :    arr[str]        ; daftar slot parkir yang telah terisi
# slot_buttons          :    arr[tk.Button]  ; menampung button slot parkir
# tersedia_motor        :    int             ; banyak slot parkir mobil yang tersedia
# tersedia_mobil        :    int             ; banyak slot parkir motor yang tersedia
# Variabel-variabel dengan akhiran `img` adalah gambar yang diimport dari folder `Assets`


## Daftar Fungsi/Prosedur 
# isNumeric(str)        -> bool ; mengecek apakah suatu string tersusun sepenuhnya atas angka
# isAlphabetic(str)     -> bool ; mengecek apakah suatu string tersusun sepenuhnya atas huruf
# entry_caps                    ; memaksa entri menjadi uppercase
# entry_limitn                  ; membatasi panjang entri menjadi n dan membatasi jenisnya
# keluar                        ; menyimpan perintah-perintah yang dieksekusi saat kendaraaan keluar
# create_slot                   ; membuat button slot parkir
# create_home                   ; membuat button home
# create_label                  ; mencetak label Tkinter bergambar
# slot_clicked                  ; menyimpan perintah-perintah yang dieksekusi ketika button `slot` diklik
# ok1_clicked                   ; menyimpan perintah-perintah yang dieksekusi ketika button `ok1` diklik
# ok2_clicked                   ; menyimpan perintah-perintah yang dieksekusi ketika button `ok2` diklik
# exit_clicked                  ; menyimpan perintah-perintah yang dieksekusi ketika button `exit` diklik

# ALGORITMA

import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os
from datetime import datetime


# Inisialisasi Awal
## Database
### Kode Wilayah
plat_nomor      = ["A","AA","AB","AD","AE","AG","B","BA","BB","BD","BE","BG","BH","BK","BL","BM","BN",
                   "BP","BR","D","DA","DB","DC","DD","DE","DG","DH","DK","DL","DM","DN","DP","DR","DT","DW",
                   "E","EA","EB","ED","F","G","H","K","KB","KH","KT","KU","L","M","N","P","PA","PB","S","T",
                   "W","Z"]
### Dictionary Blok Parkir
blokk = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

### Variabel Penampung Data
slot_id         = ["", 0]
vehicle_data    = [[0 for j in range(5)] for i in range(4)]     +   [[0 for i in range(10)] for i in range(4)]
terisi          = []
slot_buttons    = []
tersedia_mobil  = 20
tersedia_motor  = 36

# Konfigurasi Window
window  = tk.Tk()
window.geometry("760x570")
window.resizable(False, False)
window.title("Markirr™")

# Import Assets
def gambar(namafile: str) -> str:
    #
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "./Assets/") + namafile

header_img  = ImageTk.PhotoImage(Image.open(gambar("header.png")))
markirrw_img= ImageTk.PhotoImage(Image.open(gambar("markirr-white.png")))
markirrl_img= ImageTk.PhotoImage(Image.open(gambar("markirr_black.png")))
border_img  = ImageTk.PhotoImage(Image.open(gambar("parking_border.png")))
home_img    = ImageTk.PhotoImage(Image.open(gambar("home.png")))
text1_img   = ImageTk.PhotoImage(Image.open(gambar("text1.png")))
text2_img   = ImageTk.PhotoImage(Image.open(gambar("text2.png")))
text3_img   = ImageTk.PhotoImage(Image.open(gambar("text3.png")))
mobil_img   = ImageTk.PhotoImage(Image.open(gambar("mobil.png")))
motor_img   = ImageTk.PhotoImage(Image.open(gambar("motor.png")))
exit_img    = ImageTk.PhotoImage(Image.open(gambar("exit.png")))
durasi_img  = ImageTk.PhotoImage(Image.open(gambar("durasi.png")))
biaya_img   = ImageTk.PhotoImage(Image.open(gambar("biaya.png")))

# Fungsi dan Prosedur
## Fungsi isNumeric
def isNumeric(x: str) -> bool:
    # Menentukan apakah suatu string sepenuhnya tersusun atas angka
    yes = True
    for i in range(len(x)):
        if not ('0' <= x[i] <= '9'):
            yes = False
            i = len(x)
    return yes

# Fungsi isAlphabetic
def isAlphabetic(x: str) -> bool:
    # Menentukan apakah suatu string sepenuhnya tersusun atas huruf
    yes = True
    for i in range(len(x)):
        if not ('a' <= x[i] <= 'z' or 'A' <= x[i] <= 'Z'):
            yes = False
            i = len(x)
    return yes

## Prosedur entry_caps
def entry_caps(*args):
   # Memaksa entri menjadi uppercase
   seri_wilayah.set(seri_wilayah.get().upper())
   return

## Prosedur entry_limitn
def entry_limitn(n: int, entri: tk.StringVar, input_type: str):
    # Membatasi panjang entri menjadi n karakter dan membatasi jenis input
    masukan = entri.get()
    if len(masukan) > n-1:
        entri.set(masukan[:n])
    if input_type == 'alphabetic':
        if not isAlphabetic(masukan):
            entri.set(masukan[:len(masukan) - 1])
    elif input_type == 'numeric':
        if not isNumeric(masukan):
            entri.set(masukan[:len(masukan) - 1])
    return


## Prosedur keluar
def keluar():
    global tersedia_mobil, tersedia_motor
    # Menyimpan perintah-perintah yang dieksekusi saat kendaraaan keluar
    ## Menampilkan tombol home
    create_home(p4)

    ## Mengakses indeks data kendaraan dalam `vehicle_data`
    blok    = blokk[slot_terisi.get()[0]]
    nomor   = int(slot_terisi.get()[1]) - 1

    # Menghitung waktu keluar (disesuaikan dengan simulasi: 4 detik == 1 jam)
    waktu = (datetime.now() - vehicle_data[blok][nomor]["waktu_masuk"]).total_seconds()/4
    durasi_l = tk.Label(p4, text=f"{waktu:.2f} jam", font='Garamond 15', background='#1F93C5',fg='#D5DCEE')
    durasi_l.place(
        x = 147,
        y = 319
    )

    # Menghitung biaya
    if vehicle_data[blok][nomor]["jenis_kendaraan"] == "mobil":
        biaya = 5000 * int(waktu)
        # Enable slot parkir
        slot_buttons[blok * 5 + nomor].configure(state='normal', bg="#1F93C5", fg="#D5DCEE")
        ## Update counter ketersediaan slot parkir
        tersedia_mobil += 1
    else: #vehicle_data[blok][nomor]["jenis_kendaraan"] == "motor"
        biaya = 2000 * int(waktu)
        # Enable slot parkir
        slot_buttons[20 + (blok - 4) * 10 + nomor].configure(state='normal', bg="#1F93C5", fg="#D5DCEE")
        ## Update counter ketersediaan slot parkir
        tersedia_motor += 1

    biaya_nominal = tk.Label(p4, text=biaya, font='Garamond 15', background='#1F93C5',fg='#D5DCEE')
    biaya_nominal.place(
        x = 560,
        y = 319
    )

    # Menghapus data kendaraan dalam `vehicle data` dan `slot_terisi`
    vehicle_data[blok][nomor]["jenis_kendaraan"] = ""
    vehicle_data[blok][nomor]["plat_nomor"]      = ""
    vehicle_data[blok][nomor]["waktu_masuk"]     = ""
    terisi.remove(slot_terisi.get())

    return



## Prosedur create_slot
def create_slot(x: float, y: float, blok: str, num: int, page: tk.Frame, disabled: bool = False):
    # Membuat button slot parkir
    slot_l   = tk.Button(
    page,
    text= f"{blok}{num}",
    bg="#1F93C5",
    fg="#D5DCEE",
    )
    slot_l.place(
        x       = x,
        y       = y,
        width   = 34,
        height  = 51
    )
    if page == p2_mobil:
        tipe = 'mobil'
    else: #page == p2_motor
        tipe = 'motor'
    slot_l.configure(borderwidth=0, 
                     highlightthickness=0, 
                     activebackground="#D5DCEE",
                     command= lambda: slot_clicked(slot_l, blok, num, type=tipe))
    slot_buttons.append(slot_l)
    return


## Prosedur home
def create_home(page: tk.Frame, last_page='False'):
    
    # Membuat button home
    home_l     = tk.Button(
        page, image = home_img, 
        command = lambda: [p1.tkraise(), home_l.place_forget()])
    home_l.place(
        x       = 701,
        y       = 229,
        width   = 89,
        height  = 79
    )
    home_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")
    if '-' not in terisi:
        ## Memunculkan tombol `exit`
        exit_l     = tk.Button(
            p1, image = exit_img, 
            command = lambda: [exit_clicked(), exit_l.place_forget()]
            )
        exit_l.place(
            x       = 309, 
            y       = 513,
            width   = 141,
            height  = 39
        )
        exit_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")
    return

## Prosedur create_label
def create_label(label_img: tk.PhotoImage, page: tk.Frame, x: float, y: float, width: float, height: float):
    # Mencetak label Tkinter bergambar
    label_l    = tk.Label(page, image = label_img)
    label_l.place(
        x       = x,
        y       = y,
        width   = width,
        height  = height
    )
    return

## Prosedur slot_clicked
def slot_clicked(slot: tk.Button, blok: str, num: int, type: str, slot_id = slot_id):
    # Menyimpan perintah-perintah yang dieksekusi ketika button `slot` diklik
    global tersedia_mobil, tersedia_motor
    # Simpan data blok dan nomor parkir secara sementara
    terisi.append(f"{blok}{num}")
    if '-' in terisi:
        terisi.remove('-')

    ## Jenis Kendaraan
    if 'A' <= blok <= 'D':
        jenis_kendaraan = 'mobil'
    elif 'E' <= blok <= 'H':
        jenis_kendaraan = 'motor'

    # Waktu Masuk
    waktu_masuk = datetime.now()

    ## Dictionary Data Kendaraan
    slot_id[0]  = blokk[blok]
    slot_id[1]  = num-1
    
    # Menyimpan data
    vehicle_data[slot_id[0]][slot_id[1]] = {
        "jenis_kendaraan"   : jenis_kendaraan,
        "plat_nomor"        : "",
        "waktu_masuk"       : waktu_masuk,
    }

    # Counter ketersediaan slot parkir
    if type == 'mobil':
        tersedia_mobil -= 1
        tersedia_mobil_l['text'] = tersedia_mobil
        gktersedia_mobil_l['text'] = 20 - tersedia_mobil
    else: # type == 'motor'
        tersedia_motor -= 1
        tersedia_motor_l['text'] = tersedia_motor
        gktersedia_motor_l['text'] = 36 - tersedia_motor

    # Reset kondisi entri dan dropdown
    kode_wilayah_menu['state']  = 'normal'
    nopol_menu['state']         = 'normal'
    seri_wilayah_menu['state']  = 'normal'
    ok1['state']                = 'normal'
    nopol_menu.delete(0, 4)
    seri_wilayah_menu.delete(0, 4)
    kode_wilayah.set(plat_nomor[0])

    # Menuju p3
    p3.tkraise()
    slot.config(state='disabled', background="#A7B8C8")
    return 

## Prosedur ok1_clicked
def ok1_clicked():
    # Menjalankan sejumlah proses setelah button `ok1` ditekan
    ## Mengambil nopol dan seri wilayah
    nopol_value = nopol.get()
    seri_wilayah_value = seri_wilayah.get()
    ## Percabangan: aksi dilakukan jika kolom entri sudah diisi
    if nopol_value.strip() and seri_wilayah_value.strip():
        # Update data TNKB
        vehicle_data[slot_id[0]][slot_id[1]]["plat_nomor"] = f"{kode_wilayah.get()} {nopol.get()} {seri_wilayah.get()}"
        terisi[-1] += ": " + vehicle_data[slot_id[0]][slot_id[1]]["plat_nomor"]
        # Disable button
        kode_wilayah_menu['state']  = 'disabled'
        nopol_menu['state']         = 'disabled'
        seri_wilayah_menu['state']  = 'disabled'
        ok1['state']                = 'disabled'
        # Munculkan tombol home di halaman tersebut
        create_home(p3)
    else: # Entri nopol atau seri wilayah belum diisi
        print("Kolom Nopol dan Seri Wilayah tidak boleh kosong.")
    return

## prosedur ok2_clicked
def ok2_clicked():
    ## Mengakses indeks data kendaraan dalam `vehicle_data`
    blok    = blokk[slot_terisi.get()[0]]
    nomor   = int(slot_terisi.get()[1]) - 1

    ## Mengakses tipe kendaraan, plat nomor, waktu masuk, dan waktu keluar
    tipe        = vehicle_data[blok][nomor]['jenis_kendaraan']
    plat        = vehicle_data[blok][nomor]['plat_nomor']
    waktu_masuk = vehicle_data[blok][nomor]['waktu_masuk']
    waktu_keluar= datetime.now()

    teks_info = f"Jenis kendaraan: {tipe} \n Nomor TNKB: {plat} \n Waktu masuk: {waktu_masuk} \n Waktu keluar: {waktu_keluar}"
    vehicle_info = tk.Label(p4, text=teks_info, font='Garamond 15', justify="center", background='#243447',fg='#D5DCEE')
    vehicle_info.place(
        x       = 200,
        y       = 450
    )
    return

## Prosedur exit_clicked
slot_terisi        = tk.StringVar()
def exit_clicked():
    p4.tkraise()
    
    def create_slot_terisi_dropdown():
        if len(terisi) != 0:
            slot_terisi.set(terisi[0])
            terisi.sort()
        else: #len(terisi) == 0
            terisi.append("-")
        slot_terisi_menu   = tk.OptionMenu(p4, slot_terisi, *terisi)
        slot_terisi_menu.place(
        x       = 255,
        y       = 224,
        width   = 250,
        height  = 27
        )
        return
    create_slot_terisi_dropdown()
    
    def terisisi():
        if '-' in terisi:
            ok2.configure(state='disabled')
        else: #len(terisi) == 0
            ok2.configure(state='normal')

    biaya_nominal = tk.Label(p4, text="         ", font='Garamond 15', background='#1F93C5',fg='#D5DCEE')
    biaya_nominal.place(
        x = 560,
        y = 319
    )    

    durasi_l = tk.Label(p4, text="             ", font='Garamond 15', background='#1F93C5',fg='#D5DCEE')
    durasi_l.place(
        x = 147,
        y = 319
    )

    teks_info = ("                    "*4 + '\n')*5
    vehicle_info = tk.Label(p4, text=teks_info, font='Garamond 15', justify="center", background='#243447',fg='#D5DCEE')
    vehicle_info.place(
        x       = 200,
        y       = 450
    )    

    ok2 = tk.Button(p4, text="OK", command= lambda: [
        ok2_clicked(),
        keluar(),
        create_slot_terisi_dropdown(),
        terisisi()])
    ok2.place(
    x       = 520,
    y       = 224,
    width   = 25,
    height  = 25
)
    return

## Prosedur mobil_clicked
def mobil_clicked():
    ### Counter Ketersediaan Slot Parkir
    tersedia_mobil_l = tk.Label(p2_mobil, text=str(tersedia_mobil), font='Garamond 15', background='#243447',fg='#D5DCEE')
    tersedia_mobil_l.place(
        x       = 630,
        y       = 407
    )

    gktersedia_mobil_l = tk.Label(p2_mobil, text=str(20 - tersedia_mobil), font='Garamond 15', background='#243447',fg='#D5DCEE')
    gktersedia_mobil_l.place(
        x       = 630,
        y       = 458
    )

    create_home(p2_mobil)
    p2_mobil.tkraise()
    return

## Prosedur motor_clicked
def motor_clicked():
    ### Counter Ketersediaan Slot Parkir
    tersedia_motor_l = tk.Label(p2_motor, text=str(tersedia_motor), font='Garamond 15', background='#243447',fg='#D5DCEE')
    tersedia_motor_l.place(
        x       = 630,
        y       = 407
    )

    gktersedia_motor_l = tk.Label(p2_motor, text=str(36 - tersedia_motor), font='Garamond 15', background='#243447',fg='#D5DCEE')
    gktersedia_motor_l.place(
        x       = 630,
        y       = 459
    )
    create_home(p2_motor)
    p2_motor.tkraise()
    return

# Halaman-Halaman
p1          = tk.Frame(window, width=760, height=570)
p2_motor    = tk.Frame(window, width=760, height=570)
p2_mobil    = tk.Frame(window, width=760, height=570)
p3          = tk.Frame(window, width=760, height=570)
p4          = tk.Frame(window, width=760, height=570)

for frame in (p1, p2_mobil, p2_motor, p3, p4):
    frame.grid(row=0, column=0, sticky='news')

# Halaman Utama
p1.configure(bg="#243447")
p1.place(anchor='center', relx=0.5, rely=0.5)

## Header
create_label(header_img, p1, 0, -32, 760, 231)

## Logo & Slogan
create_label(markirrw_img, p1, 264, 42, 257, 98)

## Instruksi
create_label(text1_img, p1, 208, 231, 343, 22)

## Mobil

mobil_l     = tk.Button(
    p1, image = mobil_img, 
    command = lambda: mobil_clicked())
mobil_l.place(
    x       = 116, 
    y       = 296,
    width   = 199,
    height  = 205
)
mobil_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")

## Motor

motor_l     = tk.Button(
    p1, image = motor_img, 
    command = lambda: motor_clicked()
    )
motor_l.place(
    x       = 444, 
    y       = 296,
    width   = 199,
    height  = 197
)
motor_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")

# Halaman 2 (Mobil)
p2_mobil.configure(bg="#243447")
p2_mobil.place(anchor='center', relx=0.5, rely=0.5)

## Layout Parkir
### Border
create_label(border_img, p2_mobil, 70, 85, 593, 342)

### Tersedia?
create_label(text2_img, p2_mobil, 486, 404, 144, 83)

### Markirr Logo
create_label(markirrl_img, p2_mobil, 26, 506, 125, 42)

### Button Parkir
#### Blok A


create_slot(117, 98, 'A', 1, p2_mobil)
create_slot(159, 98, 'A', 2, p2_mobil)
create_slot(201, 98, 'A', 3, p2_mobil)
create_slot(243, 98, 'A', 4, p2_mobil)
create_slot(285, 98, 'A', 5, p2_mobil)

### Blok B
create_slot(404, 98, 'B', 1, p2_mobil)
create_slot(446, 98, 'B', 2, p2_mobil)
create_slot(488, 98, 'B', 3, p2_mobil)
create_slot(530, 98, 'B', 4, p2_mobil)
create_slot(572, 98, 'B', 5, p2_mobil)

### Blok C
create_slot(160, 234, 'C', 1, p2_mobil)
create_slot(230, 234, 'C', 2, p2_mobil)
create_slot(300, 234, 'C', 3, p2_mobil)
create_slot(370, 234, 'C', 4, p2_mobil)
create_slot(440, 234, 'C', 5, p2_mobil)

#### Blok D
create_slot(117, 363, 'D', 1, p2_mobil)
create_slot(159, 363, 'D', 2, p2_mobil)
create_slot(201, 363, 'D', 3, p2_mobil)
create_slot(243, 363, 'D', 4, p2_mobil)
create_slot(285, 363, 'D', 5, p2_mobil)

### Counter Ketersediaan Slot Parkir
tersedia_mobil_l = tk.Label(p2_mobil, text=str(tersedia_mobil), font='Garamond 15', background='#243447',fg='#D5DCEE')
tersedia_mobil_l.place(
    x       = 630,
    y       = 407
)
gktersedia_mobil_l = tk.Label(p2_mobil, text=str(20 - tersedia_mobil), font='Garamond 15', background='#243447',fg='#D5DCEE')
gktersedia_mobil_l.place(
    x       = 630,
    y       = 458
)

# Halaman 2 (Motor)
p2_motor.configure(bg="#243447")
p2_motor.place(anchor='center', relx=0.5, rely=0.5)

## Layout Parkir
### Border
create_label(border_img, p2_motor, 70, 85, 593, 342)

### Tersedia?
create_label(text2_img, p2_motor, 486, 404, 144, 83)

### Markirr Logo
create_label(markirrl_img, p2_motor, 26, 506, 125, 42)

### Button Parkir
#### Blok E
create_slot(117, 98, 'E', 1, p2_motor)
create_slot(159, 98, 'E', 2, p2_motor)
create_slot(201, 98, 'E', 3, p2_motor)
create_slot(243, 98, 'E', 4, p2_motor)
create_slot(285, 98, 'E', 5, p2_motor)
create_slot(327, 98, 'E', 6, p2_motor)
create_slot(369, 98, 'E', 7, p2_motor)
create_slot(411, 98, 'E', 8, p2_motor)
create_slot(453, 98, 'E', 9, p2_motor)
create_slot(495, 98, 'E', 10, p2_motor)

#### Blok F
create_slot(117, 200, 'F', 1, p2_motor)
create_slot(159, 200, 'F', 2, p2_motor)
create_slot(201, 200, 'F', 3, p2_motor)
create_slot(243, 200, 'F', 4, p2_motor)
create_slot(285, 200, 'F', 5, p2_motor)
create_slot(327, 200, 'F', 6, p2_motor)
create_slot(369, 200, 'F', 7, p2_motor)
create_slot(411, 200, 'F', 8, p2_motor)
create_slot(453, 200, 'F', 9, p2_motor)
create_slot(495, 200, 'F', 10, p2_motor)

#### Blok G
create_slot(117, 268, 'G', 1, p2_motor)
create_slot(159, 268, 'G', 2, p2_motor)
create_slot(201, 268, 'G', 3, p2_motor)
create_slot(243, 268, 'G', 4, p2_motor)
create_slot(285, 268, 'G', 5, p2_motor)
create_slot(327, 268, 'G', 6, p2_motor)
create_slot(369, 268, 'G', 7, p2_motor)
create_slot(411, 268, 'G', 8, p2_motor)
create_slot(453, 268, 'G', 9, p2_motor)
create_slot(495, 268, 'G', 10, p2_motor)

#### Blok H
create_slot(117, 363, 'H', 1, p2_motor)
create_slot(159, 363, 'H', 2, p2_motor)
create_slot(201, 363, 'H', 3, p2_motor)
create_slot(243, 363, 'H', 4, p2_motor)
create_slot(285, 363, 'H', 5, p2_motor)
create_slot(327, 363, 'H', 6, p2_motor)

### Counter Ketersediaan Slot Parkir
tersedia_motor_l = tk.Label(p2_motor, text=str(tersedia_motor), font='Garamond 15', background='#243447',fg='#D5DCEE')
tersedia_motor_l.place(
    x       = 630,
    y       = 407
)

gktersedia_motor_l = tk.Label(p2_motor, text=str(36 - tersedia_motor), font='Garamond 15', background='#243447',fg='#D5DCEE')
gktersedia_motor_l.place(
    x       = 630,
    y       = 459
)

# Halaman 3 (Plat Nomor)
p3.configure(bg="#243447")
p3.place(anchor='center', relx=0.5, rely=0.5)
## Header
create_label(header_img, p3, 0, -32, 760, 231)

## Logo & Slogan
create_label(markirrw_img, p3, 264, 42, 257, 98)

## Instruksi
create_label(text3_img, p3, 227, 285, 304, 21)

## TNKB
### Dropdown Kode Wilayah
kode_wilayah = tk.StringVar(p3)
kode_wilayah.set(plat_nomor[0])
kode_wilayah_menu   = tk.OptionMenu(p3, kode_wilayah, *plat_nomor)
kode_wilayah_menu.place(
    x       = 244,
    y       = 350,
    width   = 53,
    height  = 37
)

## Nopol
nopol       = tk.StringVar(p3)
nopol_menu  = tk.Entry(p3, textvariable=nopol,font='Garamond 15', justify="center")
nopol_menu.place(
    x       = 317,
    y       = 350,
    width   = 68,
    height  = 37
)
nopol.trace("w", lambda *args: entry_limitn(4, nopol, 'numeric'))

## Seri Wilayah
seri_wilayah        = tk.StringVar(p3)
seri_wilayah_menu   = tk.Entry(p3, textvariable=seri_wilayah, font='Garamond 15', justify="center")
seri_wilayah_menu.place(
    x       = 405,
    y       = 350,
    width   = 53,
    height  = 37
)
seri_wilayah_menu.bind("<KeyRelease>", entry_caps)
seri_wilayah.trace("w", lambda *args: entry_limitn(3, seri_wilayah, 'alphabetic'))

## OK1
ok1          = tk.Button(p3, text='OK', 
                        command=lambda:[ok1_clicked()])
ok1.place(
    x       = 470,
    y       = 350,
    width   = 37,
    height  = 37
)

# Halaman 4 (Keluar)
p4.configure(bg="#243447")
p4.place(anchor='center', relx=0.5, rely=0.5)

## Header
create_label(header_img, p4, 0, -32, 760, 231)

## Logo & Slogan
create_label(markirrw_img, p4, 264, 42, 257, 98)

## Durasi
create_label(durasi_img, p4, 55, 266, 250, 97)

## Biaya
create_label(biaya_img, p4, 455, 266, 250, 97)

# Eksekusi perulangan utama
p1.tkraise()
window.mainloop()