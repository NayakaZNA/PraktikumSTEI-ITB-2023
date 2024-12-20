/*** ******** ***/
/*** BAGIAN 1 ***/
/*** ******** ***/

/** Deklarasi Fakta **/

/* Untuk pria(X) */
pria(qika).
pria(panji).
pria(shelby).
pria(barok).
pria(aqua).
pria(eriq).
pria(francesco).

/* Untuk wanita(X) */
wanita(hinatsuru).
wanita(makio).
wanita(suma).
wanita(frieren).
wanita(yennefer).
wanita(roxy).
wanita(ruby).
wanita(suzy).
wanita(aihoshino).
wanita(eve).


/* Untuk usia(X, Y) */
usia(hinatsuru, 105).
usia(qika, 109).
usia(makio, 96).
usia(suma, 86).
usia(panji, 124).
usia(frieren, 90).
usia(shelby, 42).
usia(yennefer, 61).
usia(barok, 59).
usia(roxy, 70).
usia(aqua, 66).
usia(ruby, 63).
usia(eriq, 69).
usia(suzy, 23).
usia(francesco, 25).
usia(aihoshino, 48).
usia(eve, 5).

/* Untuk menikah(X, Y) */
menikah(qika, hinatsuru).
menikah(hinatsuru, qika).
menikah(qika, makio).
menikah(makio, qika).
menikah(qika, suma).
menikah(suma, qika).
menikah(panji, frieren).
menikah(frieren, panji).
menikah(barok, roxy).
menikah(roxy, barok).
menikah(ruby, eriq).
menikah(eriq, ruby).
menikah(suzy, francesco).
menikah(francesco, suzy).

/* Untuk anak(X, Y) */
anak(shelby, hinatsuru).
anak(shelby, qika).
anak(yennefer, hinatsuru).
anak(yennefer, qika).
anak(barok, qika).
anak(barok, makio).
anak(suzy, barok).
anak(suzy, roxy).
anak(eve, suzy).
anak(eve, francesco).
anak(aqua, panji).
anak(aqua, frieren).
anak(ruby, panji).
anak(ruby, frieren).
anak(aihoshino, eriq).
anak(aihoshino, ruby).

/* Deklarasi Rules */
% a. saudara(X,Y) 		: X adalah saudara kandung maupun tiri dari Y
saudara(X, Y)           :- anak(X, Ortu), anak(Y, Ortu), X \= Y.
% b. saudaratiri(X,Y) 	: X adalah saudara tiri dari Y
saudaratiri(X, Y)       :- anak(X, Z), anak(Y, Z), menikah(Z, W), anak(X, W), \+anak(Y, W).
% c. kakak(X,Y) 		: X adalah kakak dari Y (kakak kandung maupun tiri)
kakak(X, Y)             :- anak(X, Z), anak(Y, Z), usia(X, A), usia(Y, B), A > B.
% d. keponakan(X,Y) 	: X adalah keponakan dari Y (klarifikasi: gak boleh saudara tiri coy)
keponakan(X, Y)         :- anak(X, Z), (kakak(Y, Z); kakak(Z, Y)), \+ (saudaratiri(Y, Z)).
% e. mertua(X,Y)        : X adalah mertua dari Y
mertua(X, Y)            :- menikah(Y, PasanganY), anak(PasanganY, X), anak(PasanganY, PasanganX), menikah(X, PasanganX).
% f. nenek(X,Y)         : X adalah nenek dari Y
nenek(X, Y)             :- wanita(X), anak(Y, Z), anak(Z, X). 
% g. keturunan(X,Y)	    : X adalah keturunan dari Y (anak, cucu, dan seterusnya)
keturunan(X, Y)         :- anak(X, Y).
keturunan(X, Y)         :- anak(Z, Y), keturunan(X, Z).
% h. lajang(X)		    : X adalah orang yang tidak menikah
lajang(X)               :- (pria(X); wanita(X)), (\+menikah(X, _)).
% i. anakbungsu(X) 	    : X adalah anak paling muda, 
% (klarifikasi: tidak relatif dengan saudara tirinya (damn ini bikin jadi lebih ribet, props to yg nanya di sheets QnA))
% Terus katanya kalau gak punya saudara gak bisa dianggap anakbungsu & anaksulung ()
anakbungsu(X)           :- anak(X, Ayah), pria(Ayah), menikah(Ayah, Ibu), anak(X, Ibu), 
                            \+ (anak(AnakLain, Ayah), pria(Ayah), anak(AnakLain, Ibu), AnakLain \= X, usia(AnakLain, UsiaAnakLain), usia(X, UsiaX), UsiaAnakLain < UsiaX),
                            (anak(SaudaraKandung, Ayah), anak(SaudaraKandung, Ibu), SaudaraKandung \= X).
% j. anaksulung(X) 	    : X adalah anak paling tua
% (klarifikasi: tidak relatif dengan saudara tirinya (damn ini bikin jadi lebih ribet, props to yg nanya di sheets QnA))
% Terus katanya kalau gak punya saudara gak bisa dianggap anakbungsu & anaksulung
anaksulung(X)           :- anak(X, Ayah), pria(Ayah), menikah(Ayah, Ibu), anak(X, Ibu), 
                            \+ (anak(AnakLain, Ayah), pria(Ayah), anak(AnakLain, Ibu), AnakLain \= X, usia(AnakLain, UsiaAnakLain), usia(X, UsiaX), UsiaAnakLain > UsiaX),
                            (anak(SaudaraKandung, Ayah), anak(SaudaraKandung, Ibu), SaudaraKandung \= X).
% k. yatimpiatu(X)		: X adalah orang yang orang tuanya tidak terdefinisi
yatimpiatu(X)           :- (pria(X); wanita(X)), (\+anak(X, _)).


/*** ******** ***/
/*** BAGIAN 2 ***/
/*** ******** ***/

% 1. Exponent
exponent(A, 0, 1) :- A > 0, !.
exponent(0, B, 0) :- B > 0, !.
exponent(A, B, X) :- PrevB is B - 1, exponent(A, PrevB, PrevX), PrevX is A * X. %exponent(A, B) = A * exponent(A, B-1)

% 2. Growth
punyaFaktor(N, D) :- N mod D =:= 0, !.
punyaFaktor(N, D) :- D * D =< N, NextD is D + 1, punyaFaktor(N, NextD). % Ngecek apakah N punya faktor di rentang [D, sqrt(N)]

isPrima(2) :- !.
isPrima(3) :- !.
isPrima(X) :- X > 3, \+ punyaFaktor(X, 2).

growth(I, _, _, 0, I) :- I > 0, !.
growth(I, G, H, T, X) :- T > 0, PrevT is T - 1, growth(I, G, H, PrevT, PrevX), (isPrima(T) -> X is PrevX + G; X is PrevX - H).

% 3. Si Imut Anak Nakal
harvestFruits(N, Fruits, TreeNumber, Fruits) :- TreeNumber > N, !.
harvestFruits(_, Fruits, _, 0) :- Fruits =< 0, write('Si Imut pulang sambil menangis :('), nl, !.
harvestFruits(N, Fruits, TreeNumber, FinalFruits) :-    (TreeNumber mod 3 =:= 0 -> Mod3 is 2; Mod3 is 0),
                                                        (TreeNumber mod 4 =:= 0 -> Mod4 is -5; Mod4 is 0),
                                                        (TreeNumber mod 5 =:= 0 -> Mod5 is 3; Mod5 is 0),
                                                        (isPrima(TreeNumber) -> Prima is -10; Prima is 0),
                                                        NextFruits is Fruits + Mod3 + Mod4 + Mod5 + Prima,
                                                        NextTreeNumber is TreeNumber + 1,
                                                        harvestFruits(N, NextFruits, NextTreeNumber, FinalFruits).

% 4. KPK
fpb(A, 0, A) :- !. % basis
fpb(A, B, X) :- NextA is B, NextB is A mod B, fpb(NextA, NextB, X). % algoritma Euklides
kpk(A, B, X) :- fpb(A, B, Y), X is (A * B) / Y. % kpk(A, B) * fpb(A, B) = A * B.

% 5. Faktorial
factorial(0, 1) :- !. % basis
factorial(N, X) :- PrevN is N - 1, factorial(PrevN, PrevX), X is N * PrevX. % n! = n * (n-1)!

% 6. Make Pattern
%% Fungsi utamanya
makePattern(N) :- makePatternBaris(0, N).

%% Buat bikin pola per baris
%%% Stop ketika I = N (basis)
makePatternBaris(I, N) :- I = N, !.
%%% Mencetak pola dari suatu baris, terus lanjut ke baris selanjutnya (rekursi)
makePatternBaris(I, N) :- printElmtBaris(I, N, 0), nl, NextI is I + 1, makePatternBaris(NextI, N). 

%% Buat mencetak tiap elemen dari suatu baris
%%% Stop ketika J = N (basis)
printElmtBaris(_, N, J) :- J = N, !.
printElmtBaris(I, N, J) :- 
min2(I, J, MinIJ), min2(N - I - 1, N - J - 1, MinNINJ), min2(MinIJ, MinNINJ, Min),
Val is Min + 1,
write(Val), write(' '),
NextJ is J + 1,
printElmtBaris(I, N, NextJ).



/*** ******** ***/
/*** BAGIAN 3 ***/
/*** ******** ***/

% 1. List Statistic
%% 1a. min (di sini diimplementasikan sebagai minL)
%%% Fungsi antara min2
min2(X, Y, Min) :- (X < Y -> Min is X; Min is Y). 

%%% Fungsi utama minL
minL([X], X) :- !.
minL([Head|Tail], Min) :- minL(Tail, MinTail), min2(Head, MinTail, Min).

%% 1b. max (di sini diimplementasikan sebagai maxL)
%%% Fungsi antara max2
max2(X, Y, Maks) :- (X > Y -> Maks is X; Maks is Y). 

%%% Fungsi utama maxL
maxL([X], X) :- !.
maxL([Head|Tail], Maks) :- maxL(Tail, MaksTail), max2(Head, MaksTail, Maks).

%% 1c. range
range(List, Range) :- minL(List, Min), maxL(List, Maks), Range is Maks - Min.

%% 1d. count
count([], 0):- !.
count([_|Tail], Count) :- count(Tail, PrevCount), Count is PrevCount + 1.

%% 1e. sum
sum([X], X) :- !.
sum([Head|Tail], Sum) :- sum(Tail, PrevSum), Sum is PrevSum + Head.

% 2. List Manipulation
%% 2a. mergeSort
%%% Basis
mergeSort([], [], []).
mergeSort(List, [], List).
mergeSort([], List, List).
%%% Rekursi (bagi kasus)
mergeSort([HeadA|TailA], [HeadB|TailB], [HeadA|Result]) :- HeadA =< HeadB, mergeSort(TailA, [HeadB|TailB], Result), !.
mergeSort([HeadA|TailA], [HeadB|TailB], [HeadB|Result]) :- HeadB =< HeadA, mergeSort([HeadA|TailA], TailB, Result), !.


%% 2b. filterArray
%%% Fungsi antara passFilter
passFilter(X, Element1, Element2) :- X > Element1, X mod Element2 =:= 0.

%%% Fungsi utama filterArray
%%%% basis
filterArray([], _, _, []). 
%%%% Kasus 1: Lolos filter
filterArray([Head|Tail], Element1, Element2, [Head|Result]) :- passFilter(Head, Element1, Element2), filterArray(Tail, Element1, Element2, Result).
%%%% Kasus 2: Gagal filter
filterArray([Head|Tail], Element1, Element2, Result) :- \+ passFilter(Head, Element1, Element2), filterArray(Tail, Element1, Element2, Result).


%% 2c. reverse (diimplementasikan sebagai reverseL)
%%% Fungsi antara reverse_antara
reverse_antara([], L2, L2) :- !.
reverse_antara([H|T], L2, Result) :- reverse_antara(T, L2, [H|Result]).

%%% Fungsi utama reverseL
reverseL(L1, L2) :- reverse_antara(L1, L2, []).


%% 2d. cekPalindrom
cekPalindrom(L) :- reverseL(L, L), !.


%% 2e. rotate
%%% Fungsi antara insertLast buat nambahin elemen dari akhir
insertLast(Elmt, [], [Elmt]) :- !.
insertLast(Elmt, [Head|Tail], [Head|Res]) :- insertLast(Elmt, Tail, Res), !.
%%% Fungsi pembantu rotateSekali
rotateSekali([], []).
rotateSekali([H|T], Result) :- insertLast(H, T, Result).

%%% Fungsi utama rotate
rotate([], _, []) :- !.
rotate(List, 0, List) :- !.
rotate(List, N, Result) :- count(List, L), Neff is (N + L) mod L,
rotateSekali(List, Temp),
NextN is Neff - 1,
rotate(Temp, NextN, Result).


%% 2f. Mapping
%%% Fungsi pembantu insertFirst
insertFirst(Elmt, [], [Elmt]) :- !.
insertFirst(Elmt, List, [Elmt|List]) :- !.

%%% Fungsi pembantu mapNilai
mapNilai(Angka, Huruf) :- 
(
    Angka >= 80 -> Huruf = 'A';
    Angka >= 70 -> Huruf = 'B';
    Angka >= 60 -> Huruf = 'C';
    Angka >= 50 -> Huruf = 'D';
    Huruf = 'E'
).

%%% Fungsi pembantu mapArrayNilai
mapArrayNilai([], []).
mapArrayNilai([Head|Tail], [Indeks|Res]) :- mapNilai(Head, Indeks), mapArrayNilai(Tail, Res).

%%% Fungsi pembantu rerata
rerata(L, Rata) :- sum(L, Sum), count(L, Count), Rata is Sum / Count.

%%% Fungsi utama prosesMahasiswa
prosesMahasiswa(Name, Grades, Result) :- 
insertLast(Name, [], PreResult1), 
mapArrayNilai(Grades, Indeks), insertLast(Indeks, PreResult1, PreResult2), 
rerata(Grades, Rata), insertLast(Rata, PreResult2, PreResult3),
(Rata >= 80, Status = 'Pass'; Status = 'Fail'), insertLast(Status, PreResult3, Result).