#ifndef LISTREC_H
#define LISTREC_H

#include "boolean.h"
#include <stdio.h>

#define NIL NULL

typedef int ElType;
typedef struct node* Address;
typedef struct node { 
    ElType info;
    Address next;
} Node;

typedef Address List;

/* Selektor */
#define INFO(p) (p)->info
#define NEXT(p) (p)->next

/* Manajemen Memori */

/* Mengirimkan address hasil alokasi sebuah elemen */
/* Jika alokasi berhasil, maka address tidak NIL, dan misalnya
   menghasilkan p, maka INFO(p)=x, NEXT(p)=NIL */
/* Jika alokasi gagal, mengirimkan NIL */
Address newNode(ElType x);

/* Pemeriksaan Kondisi List */

/* Mengirimkan true jika l kosong dan false jika l tidak kosong */
boolean isEmpty(List l);

/* Mengirimkan true jika l berisi 1 elemen dan false jika > 1 elemen atau kosong */
boolean isOneElmt(List l);

/* Primitif-Primitif Pemrosesan List */

/* Mengirimkan elemen pertama sebuah list l yang tidak kosong */
ElType head(List l);

/* Mengirimkan list l tanpa elemen pertamanya, mungkin mengirimkan list kosong */
List tail(List l);

/* Mengirimkan list l dengan tambahan e sebagai elemen pertamanya. e dialokasi terlebih dahulu. 
   Jika alokasi gagal, mengirimkan l */
List konso(List l, ElType e);

/* Mengirimkan list l dengan tambahan e sebagai elemen terakhirnya */
/* e harus dialokasi terlebih dahulu */
/* Jika alokasi e gagal, mengirimkan l */ 
List konsb(List l, ElType e);

/* Mengirimkan salinan list Ll (menjadi list baru) */
/* Jika ada alokasi gagal, mengirimkan l */ 
List copy(List l);

/* Mengirimkan salinan hasil konkatenasi list l1 dan l2 (menjadi list baru) */
/* Jika ada alokasi gagal, menghasilkan NIL */
List concat(List l1, List l2);

/* Fungsi dan Prosedur Lain */

/* Mengirimkan banyaknya elemen list l, mengembalikan 0 jika l kosong */
int length(List l);

/* Mengirimkan true jika x adalah anggota list l dan false jika tidak */
boolean isMember(List l, ElType x);

/* I.S. List l mungkin kosong */
/* F.S. Jika list tidak kosong, nilai list dicetak ke bawah */
/*      Dipisahkan dengan newline (\n) dan diakhiri dengan newline */
/* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak:
  1
  20
  30
 */
/* Jika list kosong, tidak menuliskan apa-apa  */
void displayList(List l);

#endif