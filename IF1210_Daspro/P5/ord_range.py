# FUNGSI maks(a, b)
def maks(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b

# FUNGSI mini(a, b)
def mini(a: int, b: int) -> int:
    if a < b:
        return a
    else:
        return b

# FUNGSI mutlak(x)
def mutlak(x):
    if x < 0:
        return -x
    else:
        return x

# INPUT
n = input()
m = input()

# PROSES
if 65 <= ord(m) <= 90 and 65 <= ord(n) <= 90:
    kecil = mini(ord(m), ord(n))
    besar = maks(ord(m), ord(n))
    jarak1 = mutlak(ord(m) - ord(n)) 
    jarak2 = mutlak(90 - besar) + mutlak(65 - kecil) + 1 

# OUTPUT
    print(mini(jarak1, jarak2))
else:
    print("Tidak valid")