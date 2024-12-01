module ListOfInteger where
    -- DEFINISI DAN SPESIFIKASI LIST
    {- type List of Int: [ ] atau [e o List] atau [List o e]  
       Definisi type List of Int
       Basis: List of Int kosong adalah list of Int 
       Rekurens: 
       List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di awal 
       sebuah list atau
       dibuat dengan menambahkan sebuah elemen bertype Int di akhir sebuah list -}

    -- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
    konso :: Int -> [Int] -> [Int]
    {- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
       (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
    -- REALISASI
    konso e li = [e] ++ li

    konsDot :: [Int] -> Int -> [Int]
    {- konsDot li e menghasilkan sebuah list of integer dari li (list of integer) dan 
       e (sebuah integer), dengan e sebagai elemen terakhir: li o e -> li' -}
    -- REALISASI
    konsDot li e = li ++ [e]

    -- DEFINISI DAN SPESIFIKASI SELEKTOR
    -- head :: [Int] -> Int
    -- head l menghasilkan elemen pertama list l, l tidak kosong

    -- tail :: [Int] -> [Int]
    -- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

    -- last :: [Int] -> Int
    -- last l menghasilkan elemen terakhir list l, l tidak kosong

    -- init :: [Int] -> [Int]
    -- init l menghasilkan list tanpa elemen terakhir list l, l tidak kosong

    -- DEFINISI DAN SPESIFIKASI PREDIKAT
    isEmpty :: [Int] -> Bool
    -- isEmpty l  true jika list of integer l kosong
    -- REALISASI
    isEmpty l = null l

    isOneElmt :: [Int] -> Bool
    -- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
    -- REALISASI
    isOneElmt l = (length l) == 1 

-- ================================
-- ===========   SOAL   ===========
-- ================================

    -- NOMOR 3
    isMember :: [Int] -> Int -> Bool
    isMember li x
     | null li = False 
     | head li == x = True
     | otherwise = isMember (tail li) x

    -- NOMOR 4
    isEqual :: [Int] -> [Int] -> Bool 
     {- isEqual l1 l2 menghasilkan true jika l1 sama dengan l2,     yaitu jika banyaknya elemen l1 = banyaknya elemen l2 dan jika tiap elemen pada urutan yang sama adalah sama.     l1 dan l2 mungkin koson -}
    isEqual l1 l2 
     | null l1 && null l2 = True 
     | null l1 || null l2 = False
     | head l1 == head l2 = isEqual (tail l1) (tail l2)
     | otherwise = False

    -- NOMOR 5
    maxList :: [Int] -> Int
    maxList li
     | length li == 1 = head li
     | head li > maxList (tail li) = head li
     | otherwise = maxList (tail li)

    nbX :: Int -> [Int] -> Int
    nbX x li
     | null li = 0
     | head li == x = 1 + nbX x (tail li)
     | otherwise = nbX x (tail li)

    maxNb :: [Int] -> (Int, Int)
    maxNb li = (maxList li, nbX (maxList li) li)

    -- NOMOR 6
    minList :: [Int] -> Int
    minList li
     | length li == 1 = head li
     | head li < minList (tail li) = head li
     | otherwise = minList (tail li)

    jmlMin :: [Int] -> (Int, Int)
    jmlMin li = (minList li, nbX (minList li) li)

    --NOMOR 10

    filterList :: [Int] -> (Int -> Bool) -> [Int]
    filterList li f
     | null li = li
     | f (head li) = (head li) : filterList (tail li) f 
     | otherwise = filterList (tail li) f

    isPosZero :: Int -> Bool
    isPosZero x = x >= 0

    isNeg :: Int -> Bool
    isNeg x = x < 0

    pecahListPosNeg :: [Int] -> ([Int], [Int])
    pecahListPosNeg li = (filterList li isPosZero, filterList li isNeg)
