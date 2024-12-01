# Input
n = int(input())

# Validasi n biar gk haus validasi
if 0 < n <= 100:
    # Input array dan x
    arr = list(map(int, input("").split()))
    x = int(input())

    # Ubah semua elemen yang <= x menjadi angka yg sangat besar (melebihi batas, > 1000) untuk mempermudah 
    # mencari nilai minimumnya
    for i in range(n):
        if arr[i] <= x:
            arr[i] = 177013
    
    # Mencari nilai terkecil yg lebih dari x
    min_indeks = 0
    for i in range(n):
        if arr[i] < arr[min_indeks]:
            min_indeks = i
    arr[min_indeks] = 69420
    
    # Mencari nilai terkecil dari array sekarang
    min = 9999
    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    
    print(min if min != 9999 else -1)

else:
    print("Tidak valid")