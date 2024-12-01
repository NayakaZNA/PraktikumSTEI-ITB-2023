module NbKelipatanX where
-- Definisi dan Spesifikasi
    yKelipatanx :: Int -> Int -> Int
    {- Memberikan 1 jika y adalah kelipatan x, 0 sebaliknya -}

-- Realisasi
    yKelipatanx y x
     | mod y x == 0 = 1
     | otherwise = 0

-- Definisi dan Spesifikasi
    nbKelipatanX :: Int -> Int -> Int -> Int
    {- Menghitung banyaknya kelipatan X dalam selang [m, n] -}

-- Realisasi
    nbKelipatanX m n x
     | m == n + 1 = 0
     | otherwise = yKelipatanx m x + nbKelipatanX (m + 1) n x