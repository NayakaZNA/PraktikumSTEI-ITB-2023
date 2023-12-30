# NIM/Nama  : 19623116/Zulfaqqar Nayaka Athadiansyah
# Tanggal   : 19 Oktober 2023
# Deskripsi : Program menentukan banyaknya jumlah potongan list yang merupakan bilangan prima

# KAMUS
# n         : integer
# listt     : array[integer]    ; menampung bilangan yang diinput 
# summ      : integer           ; menjumlahkan potongan list
# z         : integer           ; variabel iterator dalam while loop
# count     : integer           ; menghitung berapa banyak jumlah potongan list yang prima
# prima     : bool              ; bernilai True jika bilangannya prima

# ALGORITMA
## Input N
n = int(input("Masukkan nilai N: "))

## Inisialisasi Awal
listt = [0 for i in range(n)]
count = 0

## Input bilangan ke dalam list
for i in range(n):
    listt[i] = int(input(f"Masukkan bilangan ke {i + 1}: "))

## Proses
### Menghitung tiap kemungkinan jumlah potongan list
for i in range(n):
    for j in range(i, n):
        summ = 0
        for k in range(i,j+1):
            summ += listt[k]
### Mengecek apakah `summ` prima
        if summ <= 1:
            prima = False
        else:
            z = 2
            prima = True
            while(z <= int(summ**0.5) and prima): # Mengecek primalitas n cukup hingga sqrt(n) saja
                # Jika ada satu saja z yang habis membagi `summ` maka `summ` bukan prima
                if summ % z == 0:
                    prima = False
                z += 1
### Increment nilai count jika `summ` prima
        if prima:
            count += 1
### Reset nilai `summ` untuk iterasi berikutnya
        

if count == 0:
    print("Tidak ada potongan list yang jumlahnya prima.")
else: # count != 0
    print(f"Terdapat {count} potongan list yang jumlahnya prima.")

"""
Semoga AC :D
Semangat mengkoreksi, Kak Asprak!
~ Nayaka Ganteng
"""
