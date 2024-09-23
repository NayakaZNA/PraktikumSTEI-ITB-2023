/*
Nama: Nayaka Ganteng
NIM: 13523094
Deskripsi Program: Menghitung jumlah dari seluruh elemen pada suatu barisan n bilangan yang tidak habis dibagi k

KAMUS
n   : int;  panjang barisan
k   : int;  faktor pembagi
a_i : int;  suku ke-i
*/

#include <stdio.h>
int main() {
    int n, k, jumlah, a_i;
    jumlah = 0;
    scanf("%d %d", &n, &k);         // Input n dan k
    int i;                          // Input a_i
    for (i = 0; i < n; i++) {
        scanf("%d", &a_i);
        if (a_i % k != 0) {         // Menjumlahkan a_i jika tidak habis dibagi k
            jumlah = jumlah + a_i
        }
    }
    printf("%d\n", jumlah);
    return 0;
}