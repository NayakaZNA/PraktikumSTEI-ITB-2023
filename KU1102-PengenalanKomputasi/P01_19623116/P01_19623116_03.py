# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 21 September 2023
# Deskripsi : Program menentukan banyaknya baju yang bisa dibuat berdasarkan ketersediaan bahan

# KAMUS
# kain, pita : float
# s, m, l, n : integer

# ALGORITMA

# Input
kain = float(input("Jumlah Kain: "))
pita = float(input("Jumlah Pita: "))

# Proses
# Membuat satu baju untuk setiap ukuran
kain -= 1.2 + 1.5 + 2
pita -= 0.8 + 1   + 1.3

# Menentukan apakah bahan cukup untuk membuat baju
if (kain < 0) or (pita < 0): # bahan tidak cukup
    print("Bahan tidak cukup untuk membuat baju.")
else: # bahan cukup
    s, m, l, n = 1, 1, 1, 0
    # Membuat baju dari bahan yang tersisa  
    ## Baju L
    if (kain >= 2 and pita >= 1.3): # Menentukan kecukupan bahan untuk membuat baju L
        # ambil minimum
        if (kain // 2) < (pita // 1.3):
            n = kain // 2
        else:
            n = pita // 1.3 
        # Menambah jumlah baju L yang dapat dibuat
        l    += n
        # Mengurangi bahan setelah dipakai untuk membuat baju L
        kain -= n * 2
        pita -= n * 1.3

    # Baju M
    if (kain >= 1.5 and pita >= 1): # Menentukan kecukupan bahan untuk membuat baju M
        # ambil minimum
        if (kain // 1.5) < (pita // 1):
            n = int(kain // 1.5)
        else:
            n = int(pita // 1)
        # Menambah jumlah baju M yang dapat dibuat
        m    += n
        # Mengurangi bahan setelah dipakai untuk membuat baju M
        kain -= n * 1.5
        pita -= n

    # Baju S
    if (kain >= 1.2 and pita >= 0.8): # Menentukan kecukupan bahan untuk membuat baju S
        # ambil minimum
        if (kain // 1.2) < (pita // 0.8):
            n = int(kain // 1.2)
        else:
            n = int(pita // 0.8)
        # Menambah jumlah baju S yang dapat dibuat
        s    += n
        # Mengurangi bahan setelah dipakai untuk membuat baju S
        kain -= n * 1.2
        pita -= n * 0.8

# Output
    print(f"Nona Deb dapat membuat {int(s)} ukuran S, {int(m)} ukuran M, {int(l)} ukuran L.")
