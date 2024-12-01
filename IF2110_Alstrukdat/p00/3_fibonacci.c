/*
Nama: Nayaka Ganteng
NIM: 13523094
Deskripsi Program: Menghasilkan suku ke-n dari deret Fibonacci dengan suku awal a dan b

KAMUS
a   : int;  f(1)
b   : int;  f(2)
n   : int;  urutan suku Fibonacci yang diinginkan
*/

#include <stdio.h>

int main() {
    int n, a, b;
    scanf("%d %d %d", &n, &a, &b);
    // For loop
    int i;
    if (n == 1) {
        b = a;
    } else if (n == 2) {
        a = 0;
    } else {    
        for (i = 2; i < n; i++) {
            int temp;
            temp = b;
            b = b + a;
            a = temp;
        }
    }
    printf("%d\n", b);
    return 0;
}