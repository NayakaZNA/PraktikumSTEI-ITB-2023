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
    int n, k, jumlah;
    int *a;
    scanf("%d %d", &n, &k);
    a = (int *) malloc ((n + 1) * sizeof(int));

    // Input A
    int i;
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    // Hitung jumlahna
    jumlah = 0;
    for (i = 0; i < n; i++) {
        if (a[i] % k != 0) {
            jumlah = jumlah + a[i];
        }
    }
    printf("%d\n", jumlah);
    return 0;
}