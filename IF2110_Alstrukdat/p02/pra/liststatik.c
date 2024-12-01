#include <stdio.h>
#include "liststatik.h"
#include "boolean.h"

/* ********** KONSTRUKTOR ********** */
/* Konstruktor : create List kosong  */
void CreateListStatik(ListStatik *l)
/* I.S. l sembarang */
/* F.S. Terbentuk List l kosong dengan kapasitas CAPACITY */
/* Proses: Inisialisasi semua elemen List l dengan MARK */
{
    int i;
    for (i = 0; i < CAPACITY; i++) {
        ELMT(*l, i) = MARK;
    }
}

/* ********** SELEKTOR (TAMBAHAN) ********** */
/* *** Banyaknya elemen *** */
int listLength(ListStatik l)
/* Mengirimkan banyaknya elemen efektif List */
/* Mengirimkan nol jika List kosong */
{
    int i, hitung;
    hitung = 0;
    for (i = 0; i < CAPACITY; i++) {
        if (ELMT(l, i) != MARK) {
            hitung++;
        }
    }
    return hitung;
}

/* *** Selektor INDEKS *** */
IdxType getFirstIdx(ListStatik l)
/* Prekondisi : List l tidak kosong */
/* Mengirimkan indeks elemen l pertama */
{
    return IDX_MIN;
}

IdxType getLastIdx(ListStatik l)
/* Prekondisi : List l tidak kosong */
/* Mengirimkan indeks elemen l terakhir */
{
    return listLength(l) - 1;
}

/* ********** Test Indeks yang valid ********** */
boolean isIdxValid(ListStatik l, IdxType i)
/* Mengirimkan true jika i adalah indeks yang valid utk kapasitas List l */
/* yaitu antara indeks yang terdefinisi utk container*/
{
    return (IDX_MIN <= i && i <= CAPACITY - 1);
}
boolean isIdxEff(ListStatik l, IdxType i)
/* Mengirimkan true jika i adalah indeks yang terdefinisi utk List l */
/* yaitu antara 0..length(l)-1 */
{
    return (0 <= i && i <= listLength(l) - 1);
}

/* ********** TEST KOSONG/PENUH ********** */
/* *** Test List kosong *** */
boolean isEmpty(ListStatik l)
/* Mengirimkan true jika List l kosong, mengirimkan false jika tidak */
{
    return listLength(l) == 0;
}
/* *** Test List penuh *** */
boolean isFull(ListStatik l)
/* Mengirimkan true jika List l penuh, mengirimkan false jika tidak */
{
    return listLength(l) == CAPACITY;
}

/* ********** BACA dan TULIS dengan INPUT/OUTPUT device ********** */
/* *** Mendefinisikan isi List dari pembacaan *** */
void readList(ListStatik *l)
/* I.S. l sembarang */
/* F.S. List l terdefinisi */
/* Proses: membaca banyaknya elemen l dan mengisi nilainya */
/* 1. Baca banyaknya elemen diakhiri enter, misalnya n */
/*    Pembacaan diulangi sampai didapat n yang benar yaitu 0 <= n <= CAPACITY */
/*    Jika n tidak valid, tidak diberikan pesan kesalahan */
/* 2. Jika 0 < n <= CAPACITY; Lakukan n kali: 
          Baca elemen mulai dari indeks 0 satu per satu diakhiri enter */
/*    Jika n = 0; hanya terbentuk List kosong */

{
    CreateListStatik(l);
    int i, nelmt;
    scanf("%d", &nelmt);
    while (nelmt < 0 || nelmt > CAPACITY)
    {
        // printf("salah cik"); tidak dijelaskan apa pesan errornya :((
        scanf("%d", &nelmt);
    }

    for (i = 0; i < nelmt; i++) {
        scanf("%d", &ELMT(*l, i));
    }
}

void printList(ListStatik l)
/* Proses : Menuliskan isi List dengan traversal, List ditulis di antara kurung 
   siku; antara dua elemen dipisahkan dengan separator "koma", tanpa tambahan 
   karakter di depan, di tengah, atau di belakang, termasuk spasi dan enter */
/* I.S. l boleh kosong */
/* F.S. Jika l tidak kosong: [e1,e2,...,en] */
/* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak: [1,20,30] */
/* Jika List kosong : menulis [] */
{
    int i;
    printf("[");
    for (i = 0; i < listLength(l); i++) {
        printf("%d", ELMT(l, i));
        if (i < listLength(l) - 1) {
            printf(",");
        }
    }
    printf("]");
}

/* ********** OPERATOR ARITMATIKA ********** */
/* *** Aritmatika List : Penjumlahan, pengurangan, perkalian, ... *** */
ListStatik plusMinusList(ListStatik l1, ListStatik l2, boolean plus)
/* Prekondisi : l1 dan l2 berukuran sama dan tidak kosong */
/* Jika plus = true, mengirimkan  l1+l2, yaitu setiap elemen l1 dan l2 pada 
       indeks yang sama dijumlahkan */
/* Jika plus = false, mengirimkan l1-l2, yaitu setiap elemen l1 dikurangi 
       elemen l2 pada indeks yang sama */
{
    ListStatik res_l; CreateListStatik(&res_l);
    int i;
    for (i = 0; i < listLength(l1); i++) {
        if (plus) {
            ELMT(res_l, i) = ELMT(l1, i) + ELMT(l2, i);
        } else {
            ELMT(res_l, i) = ELMT(l1, i) - ELMT(l2, i);
        }
    }

    return res_l;
}

/* ********** OPERATOR RELASIONAL ********** */
/* *** Operasi pembandingan List: *** */
boolean isListEqual(ListStatik l1, ListStatik l2)
/* Mengirimkan true jika l1 sama dengan l2 yaitu jika ukuran l1 = l2 dan semua 
   elemennya sama */
{
    boolean eq = true;
    // Cek panjangnya sama atau tidak dulu
    if (listLength(l1) != listLength(l2)) goto retf;
    int i = 0;
    while (eq && i < listLength(l1)) {
        if (ELMT(l1, i) != ELMT(l2, i)) {
            goto retf;
        }
        i++;
    }
    return true;
    retf: return false;
}

/* ********** SEARCHING ********** */
/* ***  Perhatian : List boleh kosong!! *** */
int indexOf(ListStatik l, ElType val)
/* Search apakah ada elemen List l yang bernilai val */
/* Jika ada, menghasilkan indeks i terkecil, dengan ELMT(l,i) = val */
/* Jika tidak ada atau jika l kosong, mengirimkan IDX_UNDEF */
/* Skema Searching yang digunakan bebas */
{
    // Pakai linear search
    int i;
    i = 0;
    boolean ketemu;
    ketemu = false;
    while (!ketemu && i < listLength(l)) {
        if (ELMT(l, i) == val) {
            ketemu = true;
        } else {
            i++;
        }
    }
    if (ketemu) {
        return i;
    } else {
        return IDX_UNDEF;
    }
}

boolean contains(ListStatik l, ElType val) {
    int i = 0;
    while (ELMT(l, i) != MARK) {
        if (ELMT(l, i) == val) {
            return true;
        }
        i++;
    }
    return false;
}

/* ********** NILAI EKSTREM ********** */
void extremeValues(ListStatik l, ElType *max, ElType *min)
/* I.S. List l tidak kosong */
/* F.S. Max berisi nilai terbesar dalam l;
        Min berisi nilai terkecil dalam l */
{
    int i;
    *min = ELMT(l, 0);
    *max = ELMT(l, 0);
    for (i = 0; i < listLength(l); i++) {
        if (ELMT(l, i) > *max) {*max = ELMT(l, i);}
        if (ELMT(l, i) < *min) {*min = ELMT(l, i);}
    }
}

/* ********** MENAMBAH ELEMEN ********** */
/* *** Menambahkan elemen terakhir *** */
void insertFirst(ListStatik *l, ElType val)
/* Proses: Menambahkan val sebagai elemen pertama List */
/* I.S. List l boleh kosong, tetapi tidak penuh */
/* F.S. val adalah elemen pertama l yang baru */
/* *** Menambahkan elemen pada index tertentu *** */
{
    // Mundurin semua elemen list ke kanan sebesar 1 indeks
    int i;
    for (i = listLength(*l); i > 0; i--) {
        ELMT(*l, i) = ELMT(*l, i-1);
    }
    // Sisipkan val di indeks 0
    ELMT(*l, 0) = val;
}

void insertAt(ListStatik *l, ElType val, IdxType idx)
/* Proses: Menambahkan val sebagai elemen pada index idx List */
/* I.S. List l tidak kosong dan tidak penuh, idx merupakan index yang valid di l */
/* F.S. val adalah elemen yang disisipkan pada index idx l */
/* *** Menambahkan elemen terakhir *** */
{
    // Mundurin elemen list di kanan indeks yang mau disisipkan
    int i;
    for (i = listLength(*l); i > idx; i--) {
        ELMT(*l, i) = ELMT(*l, i-1);
    }
    // Sisipkan val di indeks ke-idx
    ELMT(*l, idx) = val;
}

void insertLast(ListStatik *l, ElType val)
/* Proses: Menambahkan val sebagai elemen terakhir List */
/* I.S. List l boleh kosong, tetapi tidak penuh */
/* F.S. val adalah elemen terakhir l yang baru */
{
    ELMT(*l, listLength(*l)) = val;
}

/* ********** MENGHAPUS ELEMEN ********** */
/* *** Menghapus elemen pertama *** */
void deleteFirst(ListStatik *l, ElType *val)
/* Proses : Menghapus elemen pertama List */
/* I.S. List tidak kosong */
/* F.S. val adalah nilai elemen pertama l sebelum penghapusan, */
/*      Banyaknya elemen List berkurang satu */
/*      List l mungkin menjadi kosong */
{
    int i;
    if (!isEmpty(*l)) {
        *val = ELMT(*l, 0);
        for (i = 0; i < listLength(*l) - 1; i++) {
            ELMT(*l, i) = ELMT(*l, i+1);
        }
    }
    ELMT(*l, listLength(*l) - 1) = MARK;
}

/* *** Menghapus elemen pada index tertentu *** */
void deleteAt(ListStatik *l, ElType *val, IdxType idx)
/* Proses : Menghapus elemen pada index idx List */
/* I.S. List tidak kosong, idx adalah index yang valid di l */
/* F.S. val adalah nilai elemen pada index idx l sebelum penghapusan, */
/*      Banyaknya elemen List berkurang satu */
/*      List l mungkin menjadi kosong */
/* *** Menghapus elemen terakhir *** */
{
    int i;    
    if (!isEmpty(*l)) {
        *val = ELMT(*l, idx);
        for (i = idx; i < listLength(*l) - 1; i++) {
            ELMT(*l, i) = ELMT(*l, i+1);
        }
    }
    ELMT(*l, listLength(*l) - 1) = MARK;
}

void deleteLast(ListStatik *l, ElType *val)
/* Proses : Menghapus elemen terakhir List */
/* I.S. List tidak kosong */
/* F.S. val adalah nilai elemen terakhir l sebelum penghapusan, */
/*      Banyaknya elemen List berkurang satu */
/*      List l mungkin menjadi kosong */
{
    if (!isEmpty(*l)) {
        *val = ELMT(*l, listLength(*l)-1);
        ELMT(*l, listLength(*l) - 1) = MARK;
    }
}

/* ********** SORTING ********** */
void sortList(ListStatik *l, boolean asc)
/* I.S. l boleh kosong */
/* F.S. Jika asc = true, l terurut membesar */
/*      Jika asc = false, l terurut mengecil */
/* Proses : Mengurutkan l dengan salah satu algoritma sorting,
   algoritma bebas */
{
    // Menggunakan Bubble Sort
    int i, j, n;
    n = listLength(*l);
    boolean swap;
    for (i = 0; i < n - 1; i++) {
        swap = false;
        for (j = 0; j < n - i - 1; j++) {
            if ((asc && ELMT(*l, j) > ELMT(*l, j+1)) || (!asc && (ELMT(*l, j) < ELMT(*l, j+1)))) {
                // swapping dua elemen bersebelahan
                int temp;
                temp = ELMT(*l, j);
                ELMT(*l, j) = ELMT(*l, j+1);
                ELMT(*l, j+1) = temp;
                swap = true;
            }
        }
        if (!swap) {
            break;
        }
    }
}