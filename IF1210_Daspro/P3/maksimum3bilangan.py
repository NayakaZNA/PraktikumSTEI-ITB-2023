# Input
a = int(input())
b = int(input())
c = int(input())

# Inisialisasi awal
max_ab = 0
max_abc = 0

# Proses
## Mencari maksimum antara a dan b
if a > b:
    max_ab = a
else:
    max_ab = b

## Mencari maksimum antara a, b, dan c
if max_ab > c:
    max_abc = max_ab
else:
    max_abc = c

# Output
print(max_abc)