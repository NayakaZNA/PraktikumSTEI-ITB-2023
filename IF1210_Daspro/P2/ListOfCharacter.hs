module ListOfCharacter where
    -- DEFINISI DAN SPESIFIKASI LIST
    {- type List of Char: [ ] atau [e o List] atau [List o e]
       Definisi type List of Char
       Basis: List of Char kosong adalah list of Char
       Rekurens: 
       List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Char di awal 
       sebuah list atau
       dibuat dengan menambahkan sebuah elemen bertype Char di akhir sebuah list -}

    -- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
    konso :: Char -> [Char] -> [Char]
    {- konso e lc menghasilkan sebuah list of character dari e (sebuah character)  
       dan lc (list of integer), dengan cc sebagai elemen pertama: e o lc -> lc' -}
    -- REALISASI
    konso e lc = [e] ++ lc

    konsDot :: [Char] -> Char -> [Char]
    {- konsDot(lc,cc) menghasilkan sebuah list of character dari lc (list of 
       character) dan e (sebuah character), dengan e sebagai elemen terakhir: 
       lc o e -> lc' -}
    -- REALISASI
    konsDot lc e = lc ++ [e]

    -- DEFINISI DAN SPESIFIKASI SELEKTOR
    -- head :: [Char] -> Char
    -- head l menghasilkan elemen pertama list l, l tidak kosong

    -- tail :: [Char] -> [Char]
    -- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

    -- last :: [Char] -> Char
    -- last l  menghasilkan elemen terakhir list l, l tidak kosong

    -- init :: [Char] -> [Char]
    -- init(l) menghasilkan list tanpa elemen terakhir list l, l tidak kosong

    -- DEFINISI DAN SPESIFIKASI PREDIKAT
    isEmpty :: [Char] -> Bool
    -- isEmpty l true jika list of character l kosong
    -- REALISASI
    isEmpty l = null l

    isOneElmt :: [Char] -> Bool
    -- isOneElmt l true jika list of character l hanya mempunyai satu elemen
    -- REALISASI
    isOneElmt l = (length l) == 1 

-- ================================
-- ===========   SOAL   ===========
-- ================================

    -- NOMOR 1
    konkat :: [Char] -> [Char] -> [Char]
    konkat lc1 lc2 = lc1 ++ lc2
    
    -- NOMOR 2
    isPalindrom :: [Char] -> Bool
    isPalindrom li
     | length li <= 1 = True
     | head li /= last li = False
     | otherwise = isPalindrom (tail (init li))
    
    -- NOMOR 8
    pajakMakan :: [Char] -> [Int] -> [Char]
    pajakMakan dhahar harga
     | null dhahar || null harga = ""
     | 1.1 * (fromIntegral (head harga) :: Double) > 200 = pajakMakan (tail dhahar) (tail harga)
     | otherwise = head dhahar : pajakMakan (tail dhahar) (tail harga)
    
    -- NOMOR 9
    oddArr :: [Char] -> [Char]
    oddArr t
         | isEmpty t = t
         | mod (length t) 2 == 0 = oddArr(init t)
         | otherwise = konsDot (oddArr(init t)) (last t)
    
    evenArr :: [Char] -> [Char]
    evenArr t
         | isEmpty t = t
         | mod (length t) 2 == 0 = konsDot (evenArr(init t)) (last t)
         | otherwise = evenArr(init t)
    
    splitAlternate :: [Char] -> ([Char],[Char])
     {- splitAlternate l menghasilkan dua buah list, misalnya l1 dan l2. 
        l1 berisi semua elemen l pada posisi ganjil, l2 berisi semua elemen
        l pada posisi genap. l mungkin kosong. -}
    splitAlternate a = (oddArr a, evenArr a)