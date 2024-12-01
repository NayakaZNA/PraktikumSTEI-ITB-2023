# Input
ip  = float(input())
pot = float(input())

# Inisialisasi awal
cat = 0

if ip >= 3.5:
    cat = 4
elif ip < 3.5 and pot < 1.0:
    cat = 1
elif ip < 3.5 and (1.0 <= pot < 5.0):
    if ip >= 2.0:
        cat = 3
    else:
        cat = 2

print(cat)