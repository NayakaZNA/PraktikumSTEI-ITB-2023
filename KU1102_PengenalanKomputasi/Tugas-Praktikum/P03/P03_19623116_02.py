# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 19 Oktober 2023
# Deskripsi : Program menentukan banyaknya jumlah potongan list yang merupakan bilangan prima

# KAMUS
# n         : integer
# listt     : array[integer]    ; menampung bilangan yang diinput 
# count     : int               ; menghitung berapa banyak jumlah potongan list yang prima
# summ      : int               ; menjumlahkan potongan list
# primaGak  : bool              ; bernilai True jika bilangannya prima

# ALGORITMA
## Input N
n = int(input("Masukkan nilai N: "))

## Inisialisasi Awal
listt = [0 for i in range(n)]
count = 0
summ = 0

## Input bilangan
for i in range(n):
    listt[i] = int(input(f"Masukkan bilangan ke {i + 1}: "))

## Mengecek apakah ada elemen yang merupakan bilangan prima
for i in range(n):
    if listt[i] <= 1:
        primaGak = False
    else: # listt[i] > 1
        primaGak = True
        for j in range(2, int(listt[i] ** (0.5)) + 1): # Mengecek primalitas bilangan n cukup hingga sqrt(n) saja
            # Jika ada satu saja j yang habis membagi i maka j bukan prima
            if listt[i] % j == 0:
                primaGak = False
                # Break
                j = listt[i]
        # Kalau listt[i] prima, count di-increment
        if primaGak == True:
            count += 1

## Menghitung semua kemungkinan jumlah potongan list sambil mengecek apakah dia prima

for i in range(n):
    summ = listt[i]
    for l in range(i + 1, n):
        summ += listt[l]
        ### Mengecek apakah `summ` prima
        for k in range(summ):
            if summ <= 1:
                primaGak = False
            else: # summ > 1
                primaGak = True
                for j in range(2, int(summ ** (0.5)) + 1): # Mengecek primalitas n cukup hingga sqrt(n) saja
                    # Jika ada satu saja j yang habis membagi `summ` maka j bukan prima
                    if summ % j == 0:
                        primaGak = False
                        # Break
                        j = summ
                # Kalau summ prima, count di-increment
                if primaGak == True:
                    count += 1
if count == 0:
    print("Tidak ada potongan list yang jumlahnya prima.")
else: # count != 0
    print(f"Terdapat {count} potongan list yang jumlahnya prima.")

"""
Saya menyerah kak T_T
"""