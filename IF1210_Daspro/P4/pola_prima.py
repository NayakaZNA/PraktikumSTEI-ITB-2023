# Fungsi isPrime(n)
# Ide: bilangan prima di atas 3 dapat dinyatakan sebagai 6k + 1 atau 6k + 5
# 6k, 6k + 2, 6k + 3, 6k + 4 semuanya dapat dibagi 2 atau 3

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
    return True

# Input
n = int(input())

# Validasi input
if n < 1:
    print("Tidak valid")
else:
    # Bikin array primanya
    arr = [0 for i in range(n)]
    arr[0] = 2
    if n > 1:
        arr[1] = 3

    if n > 2:
        i = 5
        idx = 2
        while idx < n:
            if isPrime(i) and (idx < n):
                arr[idx] = i
                idx += 1
            if isPrime(i+2) and (idx < n):
                arr[idx] = i + 2
                idx += 1
            i += 6
    
    # Print barisnya
    for i in range(n):
        for j in range(i, 0, -1):
            print(arr[j], end=" ")
        for j in range(n-i-1):
            print(arr[j], end=" ")
        print(arr[n-i-1])
        

