#include <stdio.h>
#include "listlinier.h"
#include "hapus-duplikat.h"

boolean hasDuplikat(ElType x, List l) {
    Address p = FIRST(l);
    int count = 0;
    while (p != NULL) {
        if (INFO(p) == x) {
            count++;
            if (count >= 2) return true;
        }
        p = NEXT(p);
    }
    return false;
}

List hapusDuplikat(List l) {
    /**
     * Menerima masukan sebuah list l yang terurut mengecil
     * Mengembalikan list yang merupakan hasil penghapusan elemen yang mempunyai duplikat pada list l, terurut membesar
     * Contoh: hapusDuplikat(3->3->2->1) = 1->2 (-> adalah panah next pada list linear)
     */
    List L;
    CreateList(&L);

    if (isEmpty(l)) return L;
    
    Address p = FIRST(l);
    while (p != NULL) {
        if (!hasDuplikat(INFO(p), l)) {
            insertFirst(&L, INFO(p));
            }
        p = NEXT(p);
    }
    return L;
}