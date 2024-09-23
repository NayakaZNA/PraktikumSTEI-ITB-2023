/*
Nama: Nayaka Ganteng
NIM: 13523094
Deskripsi Program: Mencetak barisan bilangan pada selang [a, b] dengan aturan tertentu

KAMUS
a   : int;  batas bawah selang
b   : int;  batas atas selang
num : int;  elemen barisan
*/

#include <stdio.h>

int main() {
    int a, b, num;
    scanf("%d %d", &a, &b);
    num = a;
    while (num <= b) {
        if (num == a) {
            printf("%d", num);
        } else {
            printf(" %d", num);
        }
        
        if (num % 2 == 1) {
            num = num + 1;
        } else {
            num = num * 2;
        }
    };
    printf("\n");
    return 0;
}