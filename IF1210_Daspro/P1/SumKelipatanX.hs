module SumKelipatanX where
-- Definisi dan Spesifikasi
    yKelipatanx :: Int -> Int -> Int
    {- Memberikan 1 jika y adalah kelipatan x, 0 sebaliknya -}

-- Realisasi
    yKelipatanx y x
     | mod y x == 0 = y
     | otherwise = 0

-- Definisi dan Spesifikasi
    sumKelipatanX :: Int -> Int -> Int -> Int
    {- Menghitung banyaknya kelipatan X dalam selang [m, n] -}

-- Realisasi
    sumKelipatanX m n x
     | m == n + 1 = 0
     | otherwise = yKelipatanx m x + sumKelipatanX (m + 1) n x