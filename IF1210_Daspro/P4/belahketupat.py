# Prosedur GambarBelahKetupat(n)
def GambarBelahKetupat(n):
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan panjang diagonal mendatar sebesar N sesuai spesifikasi soal
    for i in range(n//2):
        for j in range((n - 2*i)//2):
            print(end=" ")
        for k in range(2*i + 1):
            print("*", end="")
        print()
    for i in range(n - n//2):
        for j in range(i):
            print(end=" ")
        for k in range(n - 2*i):
            print("*", end="")
        print()

# Fungsi isValid(n)
def isValid(n):
    # menghasilkan true jika N positif dan ganjil, false jika tidak
    if n <= 0 or n % 2 == 0:
        return False
    return True

# Input
n = int(input())

# Cek apakah input valid
if isValid(n):
    GambarBelahKetupat(n)
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")