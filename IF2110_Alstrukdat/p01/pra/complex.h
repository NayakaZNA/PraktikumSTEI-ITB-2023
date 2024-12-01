/* File: complex.h */
/* Tanggal: 20 September 2024 */
/* Definisi ADT COMPLEX */
/* Catatan: Gunakan %.2f pada printf serta %f untuk scanf untuk mengeluarkan dan membaca float */

#ifndef COMPLEX_H
#define COMPLEX_H

#include "boolean.h"
#include <math.h>

/* *** Definisi TYPE COMPLEX *** */
typedef struct {
    float Re; 
    float Im;
} COMPLEX;

/* *** Notasi Akses: selektor COMPLEX *** */
#define Real(C) (C).Re
#define Imag(C) (C).Im

/* ***************************************************************** */
/* DEFINISI PRIMITIF                                                 */
/* ***************************************************************** */
/* KELOMPOK VALIDASI TERHADAP TYPE                                   */
/* ***************************************************************** */
boolean IsCOMPLEXValid(float Re, float Im);
/* Mengirim true jika Re dan Im valid untuk membentuk COMPLEX */
/* Dalam konteks kompleks, semua bilangan real adalah valid */

/* *** Konstruktor: Membentuk sebuah COMPLEX dari komponen-komponennya *** */
void CreateComplex(COMPLEX *C, float Re, float Im);
/* Membentuk sebuah COMPLEX dari komponen-komponennya */

/* ***************************************************************** */
/* KELOMPOK BACA/TULIS                                               */
/* ***************************************************************** */
void BacaCOMPLEX(COMPLEX *C);
/* I.S. : C tidak terdefinisi */
/* F.S. : C terdefinisi */
/* Proses : Membaca komponen Re dan Im dari pengguna */

void TulisCOMPLEX(COMPLEX C);
/* I.S. : C sembarang */
/* F.S. : Nilai C ditulis dengan format "a + bi" atau "a - bi" (tanpa spasi) dan diakhiri newline */
/* Proses : Menulis nilai Re dan Im ke layar */

/* ***************************************************************** */
/* KELOMPOK OPERASI ARITMATIKA TERHADAP TYPE                         */
/* ***************************************************************** */
COMPLEX AddCOMPLEX(COMPLEX C1, COMPLEX C2);
/* Mengirim hasil penjumlahan C1 + C2 */

COMPLEX SubtractCOMPLEX(COMPLEX C1, COMPLEX C2);
/* Mengirim hasil pengurangan C1 - C2 */

COMPLEX MultiplyCOMPLEX(COMPLEX C1, COMPLEX C2);
/* Mengirim hasil perkalian C1 * C2 */
/* Rumus: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i */

COMPLEX DivideCOMPLEX(COMPLEX C1, COMPLEX C2);
/* Mengirim hasil pembagian C1 / C2 */
/* Rumus: (a + bi) / (c + di) = [(a + bi)(c - di)] / (c^2 + d^2) */
/* Jika denominator pecahan bernilai 0, maka kembalikan nilai 0+0i*/

/* ***************************************************************** */
/* KELOMPOK OPERASI LAIN TERHADAP TYPE                               */
/* ***************************************************************** */
float AbsCOMPLEX(COMPLEX C);
/* Mengirim nilai absolut (modulus) dari C */
/* Rumus: |C| = sqrt(Re^2 + Im^2) */

COMPLEX ConjugateCOMPLEX(COMPLEX C);
/* Mengirim hasil konjugasi dari C */
/* Rumus: Conj(C) = Re - i*Im */

/* *** Kelompok Operator Relational *** */
boolean CEQ(COMPLEX C1, COMPLEX C2);
/* Mengirimkan true jika C1 = C2 (Re dan Im sama) */

boolean CNEQ(COMPLEX C1, COMPLEX C2);
/* Mengirimkan true jika C1 tidak sama dengan C2 */

/* ***************************************************************** */

#endif