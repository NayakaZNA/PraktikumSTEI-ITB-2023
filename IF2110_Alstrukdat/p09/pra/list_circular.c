#include <stdio.h>
#include "list_circular.h"

typedef int ElType;
typedef struct node *Address;
typedef struct node { 
	ElType info;
	Address next;
} ElmtList;
typedef struct {
	Address first;
} List;

/* Definisi list : */
/* List kosong : FIRST(l) = NULL */
/* Setiap elemen dengan Address P dapat diacu INFO(P), NEXT(P) */
/* Elemen terakhir list: jika Addressnya Last, maka NEXT(Last)=FIRST(l) */

/* Selektor */
#define INFO(P) (P)->info
#define NEXT(P) (P)->next
#define FIRST(l) ((l).first)

boolean isEmpty(List l) {
    /* Mengirim true jika list kosong. */
    return FIRST(l) == NULL;
}

/****************** PEMBUATAN LIST KOSONG ******************/
void CreateList(List *l) {
    /* I.S. l sembarang             */
    /* F.S. Terbentuk list kosong. Lihat definisi di atas. */
    FIRST(*l) = NULL; 
}

/****************** Manajemen Memori ******************/
Address allocate(ElType val) {
    /* Mengirimkan Address hasil alokasi sebuah elemen */
    /* Jika alokasi berhasil, maka Address tidak NULL, dan misalnya */
    /* menghasilkan P, maka INFO(P)=val, NEXT(P)=NULL */
    /* Jika alokasi gagal, mengirimkan NULL */
    Address p = (Address) malloc(sizeof(ElmtList));
    if (p != NULL) {
        INFO(p) = val;
        NEXT(p) = NULL;
    }
}
void deallocate(Address P){
    /* I.S. P terdefinisi */
    /* F.S. P dikembalikan ke sistem */
    /* Melakukan dealokasi/pengembalian Address P */
    free(P);
    P = NULL;
}

/****************** PENCARIAN SEBUAH ELEMEN LIST ******************/
Address search(List l, ElType val){
    /* Mencari apakah ada elemen list dengan INFO(P)= val */
    /* Jika ada, mengirimkan Address elemen tersebut. */
    /* Jika tidak ada, mengirimkan NULL */
    Address p = FIRST(l);
    if (p == NULL) return p;
    else {
        do {
            if (INFO(p) == val) return p;
            p = NEXT(p);
        } while (p != FIRST(l));
    }
    return NULL;
}

boolean addrSearch(List l, Address p) {
    /* Mencari apakah ada elemen list l yang beralamat p */
    /* Mengirimkan true jika ada, false jika tidak ada */
    Address q = FIRST(l);
    if (q == NULL) return false;
    else {
        do {
            if (q == p) return true;
            q = NEXT(q);
        } while (q != FIRST(l));
    }
    return false;
}

/****************** PRIMITIF BERDASARKAN NILAI ******************/
/*** PENAMBAHAN ELEMEN ***/
void insertFirst(List *l, ElType val) {
    /* I.S. l mungkin kosong */
    /* F.S. Melakukan alokasi sebuah elemen dan */
    /* menambahkan elemen pertama dengan nilai val jika alokasi berhasil */
    Address p = allocate(val);
    if (p != NULL) {
        if (!isEmpty(*l)) {
            Address q = FIRST(*l);
            while (NEXT(q) != FIRST(*l)) {
                q = NEXT(q);
            }
            NEXT(p) = FIRST(*l);
            NEXT(q) = p;
            FIRST(*l) = p;
            
        } else {
            FIRST(*l) = p;
            NEXT(p) = p;
        }
    }
}

void insertLast(List *l, ElType val) {
    /* I.S. l mungkin kosong */
    /* F.S. Melakukan alokasi sebuah elemen dan */
    /* menambahkan elemen list di akhir: elemen terakhir yang baru */
    /* bernilai val jika alokasi berhasil. Jika alokasi gagal: I.S.= F.S. */
    Address p = allocate(val);
    if (p != NULL) {
        if (!isEmpty(*l)) {
            Address q = FIRST(*l);
            while (NEXT(q) != FIRST(*l)) {
                q = NEXT(q);
            }
            NEXT(q) = p;
            NEXT(p) = FIRST(*l);
            
        } else {
            FIRST(*l) = p;
            NEXT(p) = p;
        }
    }
}

/*** PENGHAPUSAN ELEMEN ***/
void deleteFirst(List *l, ElType * val) {
    /* I.S. List l tidak kosong  */
    /* F.S. val adalah elemen pertama list l sebelum penghapusan */
    /*      Elemen list berkurang satu (mungkin menjadi kosong) */
    /*      First element yg baru adalah suksesor elemen pertama yang lama */
    /*      Alamat elemen terakhir di-dealokasi */
    Address first = FIRST(*l);
    Address last = FIRST(*l);
    Address second = NEXT(first);

    if (NEXT(first) == first) {
        *val = INFO(FIRST(*l));
        deallocate(FIRST(*l));
        FIRST(*l) = NULL;
    } else {
        while (NEXT(last) != FIRST(*l)) {
            last = NEXT(last);
        }
        NEXT(last) = second;
        FIRST(*l) = second;
        *val = INFO(first);
        deallocate(first);
    }
}
void deleteLast(List *l, ElType * val) {
    /* I.S. list tidak kosong */
    /* F.S. x adalah elemen terakhir list sebelum penghapusan */
    /*      Elemen list berkurang satu (mungkin menjadi kosong) */
    /*      Last element baru adalah predesesor elemen pertama yg lama, jika ada */
    /*      Alamat elemen terakhir di-dealokasi */
    Address first = FIRST(*l);
    Address last = FIRST(*l);
    Address beforeLast = NULL;

    if (NEXT(first) == first) {
        *val = INFO(FIRST(*l));
        deallocate(FIRST(*l));
        FIRST(*l) = NULL;
    } else {
        while (NEXT(last) != FIRST(*l)) {
            beforeLast = last;
            last = NEXT(last);
        }
        NEXT(beforeLast) = first;
          *val = INFO(last);
        deallocate(last);
    }
}

/****************** PROSES SEMUA ELEMEN LIST ******************/
void displayList(List l) {
    /* I.S. List mungkin kosong */
    /* F.S. Jika list tidak kosong, iai list dicetak ke kanan: [e1,e2,...,en] */
    /* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak: [1,20,30] */
    /* Jika list kosong : menulis [] */
    /* Tidak ada tambahan karakter apa pun di awal, akhir, atau di tengah */
    Address p = FIRST(l);
    if (!isEmpty(l)) {
        printf("[");
        do {
        printf("%d", INFO(p));
        p = NEXT(p);
        if (p != FIRST(l)) {
            printf(",");
        }
        } while (p != FIRST(l));
        printf("]");
    } else {
        printf("[]");
    }
}
