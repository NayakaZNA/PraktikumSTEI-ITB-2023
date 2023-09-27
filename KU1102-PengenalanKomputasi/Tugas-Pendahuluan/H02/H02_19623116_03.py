# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 26 September 2023
# Deskripsi : Program menentukan apakah bilangan N dapat dicapai melalui perkalian A dan B

# KAMUS
# a, b, n   : integer
# count     : integer;  variabel untuk menyimpan berapa kali perkalian sudah dilakukan
# pa, pb    : integer;  variabel untuk menyimpan perkalian a dan b, baik dimulai dari a maupun b

# ALGORITMA

# Input
a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
n = int(input("Masukkan bilangan N: "))

# Inisiasi Awal
pa, pb, count = a, b, 1
if a == n or b == n:
    print(f"Bilangan {n} dapat dicapai.")  # Cek apakah A atau B sama dengan N

# While Loop
else:
    while (pa < n and pb < n): # Aksi dilakukan selama hasil perkalian belum mencapai/melebihi N
        # Perkalian dengan a atau b dilakukan secara bergantian
        if count % 2 == 1:
            pa *= b  # Perkalian dengan b
            pb *= a  # Perkalian dengan a
        else:
            pa *= a  # Perkalian dengan a
            pb *= b  # Perkalian dengan b
        count += 1  # Increment count setelah setiap perkalian

    # Cek apakah N dapat dicapai dengan perkalian a dan b
    if pa == n or pb == n:
        print(f"Bilangan {n} dapat dicapai.")
    else:
        print(f"Bilangan {n} tidak dapat dicapai.")
