# Praktikum STEI ITB 2023
```assembly
section        .text         
global         _start          
_start:
    mov edx, len 
    mov ecx, msg 
    mov ebx, 1
    mov eax, 4
    int 0x80
    mov eax, 1
    int 0x80
section        .data             
    msg        db "Sugeng rawuh, rencang-rencang sedaya!", 0xa
    len        equ $ -msg
```
## Deskripsi
Repositori ini berisi file soal dan dokumentasi pekerjaan saya dalam praktikum selama belajar di Sekolah Teknik Elektro dan Informatika Institut Teknologi Bandung (STEI ITB). Mudah-mudahan bisa bermanfaat bagi rekan-rekan sekalian. :D

## Daftar Mata Kuliah
- [KU1102 Pengenalan Komputasi](./KU1102-PengenalanKomputasi)
- IF1210 Dasar Pemrograman (belum semester 2, tunggu ya)
- Algoritma dan Struktur Data (belum masuk IF)

## Penulis
Nayaka [19623116]
