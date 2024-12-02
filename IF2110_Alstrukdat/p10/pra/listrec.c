#include <stdio.h>
#include "boolean.h"
#include "listrec.h"

/* Manajemen Memori */

Address newNode(ElType x) {
    Address p = (Address) malloc(sizeof(Node));
    if (p == NIL) return p;
    INFO(p) = x;
    NEXT(p) = NIL;
}

/* Pemeriksaan Kondisi List */

boolean isEmpty(List l) {
    return l == NIL;
}

boolean isOneElmt(List l) {
    return l != NIL && NEXT(l) == NIL;
}

/* Primitif-Primitif Pemrosesan List */
ElType head(List l) {
    return INFO(l);
}

List tail(List l) {
    return NEXT(l);
}

List konso(List l, ElType e) {
    Address p = newNode(e);
    if (p == NIL) return l;
    NEXT(p) = l;
    return p;
}

List konsb(List l, ElType e) {
    if (isEmpty(l)) return newNode(e);
    NEXT(l) = konsb(tail(l), e);
    return l;
}

List copy(List l) {
    if (isEmpty(l)) return NIL;
    return konso(copy(tail(l)), head(l));
}

List concat(List l1, List l2) {
    if (isEmpty(l1)) return copy(l2);
    return konso(concat(tail(l1), l2), head(l1));
}

/* Fungsi dan Prosedur Lain */
int length(List l) {
    if (isEmpty(l)) return 0;
    return 1 + length(tail(l));
}

boolean isMember(List l, ElType x) {
    if (isEmpty(l)) return false;
    return (head(l) == x) || isMember(tail(l), x);
}

void displayList(List l) {
    if (!isEmpty(l)) {
        printf("%d\n", head(l));
        displayList(tail(l));
    }
}