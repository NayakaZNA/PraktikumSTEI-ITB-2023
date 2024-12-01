
# Inisialisasi awal
num = 0
count = 0
arr = [0 for i in range(10)]

# Input angka
while count < 100:
    num = int(input())
    if num < 0:
        break
    else:
        count += 1
        if num == 0:
            arr[0] += 1
        else:
            while num > 0:
                arr[num % 10] += 1
                num //= 10

# Output
if count == 0: 
    print(0)
else:
    print(count)
    for i in range(10):
        if arr[i] != 0:
            print(str(i) + " : " + str(arr[i]))