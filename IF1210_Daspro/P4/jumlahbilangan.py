# Input
x = int(input(""))
y = int(input(""))

# Inisialisasi awal
count = 0

# Proses (loop dari x ke y inklusif)
for num in range(x, y + 1):
    # Memeriksa apakah bilangan tersebut habis dibagi 3 atau 4
    if num % 3 == 0 or num % 4 == 0:
        # Jika ya, count di increment
        count += 1

# Output
if count == 0:
    print("Tidak Ada")
else:
    print(count)