# Input
num = int(input())

# Inisialisasi awal
if num < 0:
    neg = True
    num = -1*num
else:
    neg = False
revnum = 0


# Proses
while num > 0:
    revnum = 10*revnum + (num % 10)
    num //= 10

# Output
print(-revnum if neg else revnum)