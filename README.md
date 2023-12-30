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
Mata Kuliah                                                 |Semester   |SKS|
|-----------------------------------------------------------|-----------|---|
[KU1102 Pengenalan Komputasi](./KU1102-Pengkom)             |1          |3  |
[IF1210 Dasar Pemrograman](./IF1210_Daspro/)                |2          |2  |
[IF2110 Algoritma dan Struktur Data](./IF2110_Alstrukdat/)  |3          |4  |

## Penulis
Nayaka [19623116]
