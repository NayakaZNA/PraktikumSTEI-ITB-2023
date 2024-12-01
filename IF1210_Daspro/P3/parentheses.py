def kurarr(teks: str) -> bool:
    # Maaf saya kurang tahu apakah boleh pakai dictionary atau tidak
    kurung = {")": "(", "}": "{", "]": "["}
    stack = ['' for i in range(len(teks))] # Untuk keep track kurung buka: ({[
    stack_size = 0  # keep track panjang array stack
    for i in teks:
        if i == "(" or i == "{" or i == "[":
            stack[stack_size] = i  # masukkan kurung buka ke array stack
            stack_size += 1
        elif i == ")" or i == "}" or i == "]":
            # Kalau stack kosong atau 
            if (kurung[i] != stack[stack_size - 1]):
                return False
            stack_size -= 1
    # Kalau stacknya tidak kosong berarti ada tanda kurung yang tidak berpasangan
    return stack_size == 0

# Input
teks = input()

# Output
print("valid" if kurarr(teks) else "tidak valid")
