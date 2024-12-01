def romdes(romawi: str) -> int:
    if romawi == "I": return 1
    elif romawi == "V": return 5
    elif romawi == "X": return 10
    elif romawi == "L": return 50
    elif romawi == "C": return 100
    elif romawi == "D": return 500
    elif romawi == "M": return 1000
    else: return 0
    return 0

# Input
rom_num = input()

# Inisialisasi awal
des_num = 0
n = 0
rom_arr = [0 for i in range(len(rom_num))]

# Proses
## Convert dulu angka romawinya ke desimal terus simpan ke array
for i in range(len(rom_num)):
    rom_arr[i] = romdes(rom_num[i])

## Mengolah menjadi desimal
i = 0
while i < (len(rom_num)):
    if i == len(rom_num) - 1:
        des_num += rom_arr[i]
        i += 1
    else:
        if rom_arr[i] >= rom_arr[i+1]:
            des_num += rom_arr[i]
            i += 1
        else:
            des_num += rom_arr[i+1] - rom_arr[i]
            i += 2

# Output
print(des_num)