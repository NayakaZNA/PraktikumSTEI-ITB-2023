/*
Nama: Nayaka Ganteng
NIM: 13523094
Deskripsi Program: Mencetak segitiga terbalik dengan tinggi n

KAMUS
n:  int; tinggi segitiga
*/

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    // For loop
    int i;
    for (i = 0; i < n; i++) {
        // Space
        int j;
        for (j = 0; j < i; j++) {           // Mencetak spasi sebanyak i
            printf(" ");
        }
        // Bintang
        for (j = 0; j < 2*(n-i) - 1; j++) { // Mencetak bintang sebanyak 2*(n-1) - 1
            printf("*");
        }
        // Newline
        printf("\n");
    }
    return 0;
}