#include <stdio.h>
#include <math.h>
#include "complex.h"

/* ***************************************************************** */
/* DEFINISI PRIMITIF                                                 */
/* ***************************************************************** */
/* KELOMPOK VALIDASI TERHADAP TYPE                                   */
/* ***************************************************************** */
boolean IsCOMPLEXValid(float Re, float Im) {
    /* Mengirim true jika Re dan Im valid untuk membentuk COMPLEX */
    /* Dalam konteks kompleks, semua bilangan real adalah valid */
    return true;
}
/* *** Konstruktor: Membentuk sebuah COMPLEX dari komponen-komponennya *** */
void CreateComplex(COMPLEX *C, float Re, float Im){
    /* Membentuk sebuah COMPLEX dari komponen-komponennya */
    Real(*C) = Re;
    Imag(*C) = Im;
}

/* ***************************************************************** */
/* KELOMPOK BACA/TULIS                                               */
/* ***************************************************************** */
void BacaCOMPLEX(COMPLEX *C) {
    /* I.S. : C tidak terdefinisi */
    /* F.S. : C terdefinisi */
    /* Proses : Membaca komponen Re dan Im dari pengguna */
    scanf("%f %f", &Real(*C), &Imag(*C));
}

void TulisCOMPLEX(COMPLEX C) {
    /* I.S. : C sembarang */
    /* F.S. : Nilai C ditulis dengan format "a + bi" atau "a - bi" (tanpa spasi) dan diakhiri newline */
    /* Proses : Menulis nilai Re dan Im ke layar */
    if (Imag(C) < 0) {
        printf("%.2f-%.2fi\n", Real(C), -1*Imag(C));
    } else {
        printf("%.2f+%.2fi\n", Real(C), Imag(C));
    }
}

/* ***************************************************************** */
/* KELOMPOK OPERASI ARITMATIKA TERHADAP TYPE                         */
/* ***************************************************************** */
COMPLEX AddCOMPLEX(COMPLEX C1, COMPLEX C2){
    /* Mengirim hasil penjumlahan C1 + C2 */
    COMPLEX C3;
    CreateComplex(&C3, Real(C1) + Real(C2), Imag(C1) + Imag(C2));
    return C3;
}

COMPLEX SubtractCOMPLEX(COMPLEX C1, COMPLEX C2) {
    /* Mengirim hasil pengurangan C1 - C2 */
    COMPLEX C3;
    CreateComplex(&C3, Real(C1) - Real(C2), Imag(C1) - Imag(C2));
    return C3;
}

COMPLEX MultiplyCOMPLEX(COMPLEX C1, COMPLEX C2) {
    /* Mengirim hasil perkalian C1 * C2 */
    /* Rumus: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i */
    COMPLEX C3;
    float a, b, c, d;
    a = Real(C1);
    b = Imag(C1);
    c = Real(C2);
    d = Imag(C2);
    CreateComplex(&C3, a * c - b * d, a * d + b * c);
    return C3;
}

COMPLEX DivideCOMPLEX(COMPLEX C1, COMPLEX C2) {
    /* Mengirim hasil pembagian C1 / C2 */
    /* Rumus: (a + bi) / (c + di) = [(a + bi)(c - di)] / (c^2 + d^2) */
    /* Jika denominator pecahan bernilai 0, maka kembalikan nilai 0+0i*/
    COMPLEX C3;
    float a, b, c, d, denominator;
    a = Real(C1); b = Imag(C1); c = Real(C2); d = Imag(C2);
    denominator = c * c + d * d;
    if (denominator == 0) {
        CreateComplex(&C3, 0, 0);
    } else {
        CreateComplex(&C3, c, -1 * d);
        C3 = MultiplyCOMPLEX(C1, C3);
        Real(C3) = Real(C3) / denominator;
        Imag(C3) = Imag(C3) / denominator;
    }
    return C3;
}
/* ***************************************************************** */
/* KELOMPOK OPERASI LAIN TERHADAP TYPE                               */
/* ***************************************************************** */
float AbsCOMPLEX(COMPLEX C){
    /* Mengirim nilai absolut (modulus) dari C */
    /* Rumus: |C| = sqrt(Re^2 + Im^2) */
    return sqrt(Real(C) * Real(C) + Imag(C) * Imag(C));
}

COMPLEX ConjugateCOMPLEX(COMPLEX C) {
/* Mengirim hasil konjugasi dari C */
/* Rumus: Conj(C) = Re - i*Im */
    COMPLEX conjC;
    CreateComplex(&conjC, Real(C), -1*Imag(C));
    return conjC;
}

/* *** Kelompok Operator Relational *** */
boolean CEQ(COMPLEX C1, COMPLEX C2) {
    /* Mengirimkan true jika C1 = C2 (Re dan Im sama) */
    return (Real(C1) == Real(C2) && Imag(C1) == Imag(C2));
}

boolean CNEQ(COMPLEX C1, COMPLEX C2){
    /* Mengirimkan true jika C1 tidak sama dengan C2 */
    return !CEQ(C1, C2);
}
/* ***************************************************************** */
