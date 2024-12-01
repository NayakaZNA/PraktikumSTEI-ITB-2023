#include "garis.h"

/* ***************************************************************** */
/* DEFINISI PRIMITIF                                                 */
/* ***************************************************************** */
/* *** Konstruktor membentuk GARIS *** */
void CreateGaris(GARIS *L, POINT P1, POINT P2){
    /* I.S. P1 dan P2 terdefinisi */
    /* F.S. L terdefinisi dengan L.PAw = P1 dan L.PAkh = P2 */
    /* Membentuk sebuah L dari komponen-komponennya */
    PAwal(*L) = P1;
    PAkhir(*L) = P2;
}

/* ***************************************************************** */
/* KELOMPOK INTERAKSI DENGAN I/O DEVICE, BACA/TULIS                  */
/* ***************************************************************** */
void BacaGARIS(GARIS *L) {
    /* I.S. sembarang */
    /* F.S. L terdefinisi sebagai GARIS yang valid */
    /* Proses : mengulangi membaca dua buah nilai P1 dan P2 sehingga dapat
        membentuk GARIS yang valid
       GARIS disebut valid jika titik awal tidak sama dengan titik akhirnya. */
    /* Jika pembacaan garis tidak valid, diberikan pesan kesalahan:
       "Garis tidak valid" */
    /* Contoh:
        2 3
        2 3
        Garis tidak valid
        2 3
        3 3
       --> terbentuk garis L dengan L.PAw = <2,3> dan L.PAkh = <3,3> */
    BacaPOINT(&PAwal(*L));
    BacaPOINT(&PAkhir(*L));
}

void TulisGARIS(GARIS L) {
/* I.S. L terdefinisi */
/* F.S. L tertulis di layar dengan format "((x1,y1),(x2,y2))"
    tanpa tambahan karakter apa pun di depan, di tengah, atau di belakang,
    termasuk spasi dan enter */
    printf("(");
    TulisPOINT(PAwal(L));
    printf(",");
    TulisPOINT(PAkhir(L));
    printf(")");
}

/* *** Kelompok operasi garis *** */
float PanjangGARIS(GARIS L) { 
    /* Menghitung panjang garis L : berikan rumusnya */
    /* Menggunakan fungsi Panjang dari point.h */
    return Panjang(PAwal(L), PAkhir(L));
}
float Gradien(GARIS L) {
    /* Mengembalikan Gradien (m) dari L */
    /* Gradien garis yang melalui (x1,y1) dan (x2,y2) adalah: (y2-y1)/(x2-x1) */
    /* Prekondisi : x1 != x2 */
    int x1, x2, y1, y2;
    x1 = Absis(PAwal(L));
    y1 = Ordinat(PAwal(L));
    x2 = Absis(PAkhir(L));
    y2 = Ordinat(PAkhir(L));
    return (y2 - y1) / (x2 - x1);
}

void GeserGARIS(GARIS *L, float deltaX, float deltaY) {
    /* I.S. L terdefinisi */
    /* F.S. L digeser sebesar deltaX ke arah sumbu X dan sebesar deltaY ke arah sumbu Y */
    /* Proses : PAw dan PAkh digeser. */
    Geser(&PAwal(*L), deltaX, deltaY);
    Geser(&PAkhir(*L), deltaX, deltaY);
}

/* *** Kelompok predikat *** */
boolean IsTegakLurus(GARIS L1, GARIS L2) {
    /* Menghasilkan true jika L1 tegak lurus terhadap L2 */
    /* Dua garis saling tegak lurus jika hasil perkalian kedua gradiennya = -1 */
    return Gradien(L1) * Gradien(L2) == -1;
}

boolean IsSejajar(GARIS L1, GARIS L2) {
    /* Menghasilkan true jika L "sejajar" terhadap L1 */
    /* Dua garis saling sejajar jika memiliki gradien yang sama */
    return Gradien(L1) == Gradien(L2);
}

/* *** Kelompok operasi garis dan point *** */
float JarakGARIS(GARIS L, POINT P) {
    /* Menghasilkan jarak terdekat antara titik P dan garis L */
    /* Bentuklah persamaan dari garis L menjadi ax + by + c = 0 */
    /* Jarak terdekat dari titik P ke garis L dapat didefinisikan sebagai d = |a * x + b * y + c| / akar kuadrat dari a * a + b * b */
    int a, b, c, x, y;
    a = Gradien(L);
    b = -1;
    c = Ordinat(PAwal(L)) - a * Absis(PAwal(L));
    x = Absis(P);
    y = Ordinat(P);
    return(fabs(a * x + b * y + c) / sqrt(a * a + b * b));
}

boolean IsPointMemenuhiGaris(GARIS L, POINT P) {
    /* Menghasilkan true jika  titik P terletak di garis L */
    /* Bentuklah persamaan dari garis L menjadi ax + by + c = 0 */
    /* Titik P terletak di garis L jika dan hanya jika P memenuhi persamaan garis L, yaitu ax + by + c = 0 */
    int a, b, c, x, y;
    a = Gradien(L);
    b = -1;
    c = Ordinat(PAwal(L)) - a * Absis(PAwal(L));
    x = Absis(P);
    y = Ordinat(P);
    return a * x + b * y + c == 0;
}